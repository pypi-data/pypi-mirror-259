# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import os

from pathlib import Path

import rerun as rr

from projectaria_tools.core import data_provider, mps
from projectaria_tools.core.mps import MpsDataPathsProvider
from projectaria_tools.core.mps.utils import (
    filter_points_from_confidence,
    filter_points_from_count,
    get_gaze_vector_reprojection,
    get_nearest_eye_gaze,
    get_nearest_pose,
)
from projectaria_tools.core.sensor_data import SensorDataType, TimeDomain
from projectaria_tools.core.stream_id import StreamId

from projectaria_tools.utils.rerun_helpers import AriaGlassesOutline, ToTransform3D
from tqdm import tqdm


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--vrs",
        type=str,
        help="path to VRS file",
    )
    # Add options for the MPS Artifacts
    # - They can be specified individually,
    # - Or globally as a 'mps_folder' path
    parser.add_argument(
        "--trajectory",
        nargs="+",
        type=str,
        help="path(s) to MPS closed loop trajectory files",
    )
    parser.add_argument(
        "--points",
        nargs="+",
        type=str,
        help="path(s) to the MPS global point file",
    )
    parser.add_argument(
        "--eyegaze",
        type=str,
        help="path to the MPS eye gaze file",
    )
    parser.add_argument(
        "--mps_folder",
        type=str,
        help="path to the MPS folder (will overwrite default value <vrs_file>/mps)",
    )

    # Add options that does not show by default, but still accessible for debugging purpose
    parser.add_argument(
        "--down_sampling_factor", type=int, default=4, help=argparse.SUPPRESS
    )
    parser.add_argument("--jpeg_quality", type=int, default=75, help=argparse.SUPPRESS)

    return parser.parse_args()


def main():
    args = parse_args()

    #
    # Gather data input
    #
    if args.vrs:
        vrs_folder_path = os.path.dirname(args.vrs)
        # - If MPS data has not been provided we try to find them automatically using default folder hierarchy
        if args.points is None and args.eyegaze is None and args.trajectory is None:
            if args.mps_folder:
                mps_data_paths_provider = MpsDataPathsProvider(args.mps_folder)
            else:
                # Try loading from default mps path (<vrs_file>/mps)
                mps_data_paths_provider = MpsDataPathsProvider(
                    str(Path(vrs_folder_path + "/mps"))
                )
            mps_data_paths = mps_data_paths_provider.get_data_paths()

            if not args.trajectory and os.path.exists(
                mps_data_paths.slam.closed_loop_trajectory
            ):
                args.trajectory = [str(mps_data_paths.slam.closed_loop_trajectory)]

            if not args.points and os.path.exists(mps_data_paths.slam.semidense_points):
                args.points = [str(mps_data_paths.slam.semidense_points)]

            if not args.eyegaze and os.path.exists(
                mps_data_paths.eyegaze.personalized_eyegaze
            ):
                args.eyegaze = mps_data_paths.eyegaze.personalized_eyegaze
            if not args.eyegaze and os.path.exists(
                mps_data_paths.eyegaze.general_eyegaze
            ):
                args.eyegaze = mps_data_paths.eyegaze.general_eyegaze

    mps_data_available = args.trajectory or args.points or args.eyegaze

    print(
        f"""
    Trying to load the following list of files:
    - vrs: {args.vrs}
    - trajectory/closed_loop_trajectory: {args.trajectory}
    - trajectory/point_cloud: {args.points}
    - eye_gaze/general_eye_gaze: {args.eyegaze}
    """
    )

    if mps_data_available is None and args.vrs is None:
        print("Nothing to display.")
        exit(1)

    # Initializing Rerun viewer
    rr.init("MPS Data Viewer", spawn=True)
    rr.log("world", rr.ViewCoordinates.RIGHT_HAND_Z_UP, timeless=True)

    #
    # Log device trajectory (reduce sample count for display)
    #
    if args.trajectory:
        print("Loading and logging trajectory(ies)...")
        trajectory_list_size = len(args.trajectory)
        i = 0
        for trajectory_file in args.trajectory:
            print(f"Loading: {trajectory_file}")
            trajectory_data = mps.read_closed_loop_trajectory(trajectory_file)
            device_trajectory = [
                it.transform_world_device.translation()[0] for it in trajectory_data
            ][0::80]
            rr.log(
                "world/device_trajectory"
                if trajectory_list_size == 1
                else f"world/device_trajectory_{i}",
                rr.LineStrips3D(device_trajectory, radii=0.008),
                timeless=True,
            )
            i += 1

    #
    # Log Point Cloud(s) (reduce point count for display)
    #
    if args.points:
        print("Loading and logging point cloud(s)...")
        point_cloud_list_size = len(args.points)
        i = 0
        for points_file in args.points:
            points_data = mps.read_global_point_cloud(points_file)
            # Filter out low confidence points
            points_data = filter_points_from_confidence(points_data)
            # Down sample points
            points_data_down_sampled = filter_points_from_count(
                points_data, 500_000 if point_cloud_list_size == 1 else 20_000
            )
            # Retrieve point position
            point_positions = [it.position_world for it in points_data_down_sampled]
            rr.log(
                "world/points" if point_cloud_list_size == 1 else f"world/points_{i}",
                rr.Points3D(point_positions, radii=0.006),
                timeless=True,
            )
            i += 1

    #
    # If we have a VRS file go over RGB timestamps and
    # - Plot camera pose
    # - Plot user eye gaze
    #

    if args.vrs:
        provider = data_provider.create_vrs_data_provider(args.vrs)
        rgb_stream_id = StreamId("214-1")
        rgb_stream_label = provider.get_label_from_stream_id(rgb_stream_id)
        device_calibration = provider.get_device_calibration()
        T_device_CPF = device_calibration.get_transform_device_cpf()
        rgb_camera_calibration = device_calibration.get_camera_calib(rgb_stream_label)

        # Load Trajectory and Eye Gaze data - corresponding to this specific VRS file
        trajectory_data = (
            mps.read_closed_loop_trajectory(str(args.trajectory[0]))
            if args.trajectory
            else None
        )
        eyegaze_data = mps.read_eyegaze(args.eyegaze) if args.eyegaze else None

        #
        # Log RGB camera calibration
        #
        if mps_data_available:
            rr.log(
                f"world/device/{rgb_stream_label}",
                rr.Pinhole(
                    resolution=[
                        rgb_camera_calibration.get_image_size()[0]
                        / args.down_sampling_factor,
                        rgb_camera_calibration.get_image_size()[1]
                        / args.down_sampling_factor,
                    ],
                    focal_length=float(
                        rgb_camera_calibration.get_focal_lengths()[0]
                        / args.down_sampling_factor
                    ),
                ),
                timeless=True,
            )

        #
        # Log Aria Glasses outline
        #
        if mps_data_available:
            aria_glasses_point_outline = AriaGlassesOutline(device_calibration)
            rr.log(
                "world/device/glasses_outline",
                rr.LineStrips3D([aria_glasses_point_outline]),
                timeless=True,
            )

        # Configure the loop for data replay
        deliver_option = provider.get_default_deliver_queued_options()
        deliver_option.deactivate_stream_all()
        deliver_option.activate_stream(rgb_stream_id)  # RGB Stream Id
        rgb_frame_count = provider.get_num_data(rgb_stream_id)

        progress_bar = tqdm(total=rgb_frame_count)
        # Iterate over the data and LOG data as we see fit
        for data in provider.deliver_queued_sensor_data(deliver_option):
            device_time_ns = data.get_time_ns(TimeDomain.DEVICE_TIME)
            rr.set_time_nanos("device_time", device_time_ns)
            rr.set_time_sequence("timestamp", device_time_ns)
            progress_bar.update(1)

            # Camera pose
            if trajectory_data:
                pose_info = get_nearest_pose(trajectory_data, device_time_ns)
                if pose_info:
                    T_world_device = pose_info.transform_world_device
                    T_device_camera = (
                        rgb_camera_calibration.get_transform_device_camera()
                    )
                    rr.log(
                        "world/device",
                        ToTransform3D(T_world_device, False),
                    )
                    rr.log(
                        f"world/device/{rgb_stream_label}",
                        ToTransform3D(T_device_camera, False),
                    )

            if data.sensor_data_type() == SensorDataType.IMAGE:
                img = data.image_data_and_record()[0].to_numpy_array()
                if args.down_sampling_factor > 1:
                    img = img[
                        :: args.down_sampling_factor, :: args.down_sampling_factor
                    ]
                # Note: We configure the QUEUE to return only RGB image, so we are sure this image is corresponding to a RGB frame
                rr.log(
                    f"world/device/{rgb_stream_label}",
                    rr.Image(img).compress(jpeg_quality=args.jpeg_quality),
                )

            #
            # Eye Gaze (vector and image reprojection)
            #
            if eyegaze_data:
                depth_m = 1.0  # Select a fixed depth of 1m
                eye_gaze = get_nearest_eye_gaze(eyegaze_data, device_time_ns)
                if eye_gaze:
                    gaze_vector_in_cpf = mps.get_eyegaze_point_at_depth(
                        eye_gaze.yaw, eye_gaze.pitch, depth_m
                    )
                    # Move EyeGaze vector to CPF coordinate system for visualization
                    rr.log(
                        "world/device/eye-gaze",
                        rr.Arrows3D(
                            origins=[T_device_CPF @ [0, 0, 0]],
                            vectors=[T_device_CPF @ gaze_vector_in_cpf],
                            colors=[[255, 0, 255]],
                        ),
                    )
                    # Compute eye_gaze vector at depth_m reprojection in the image
                    gaze_projection = get_gaze_vector_reprojection(
                        eye_gaze,
                        rgb_stream_label,
                        device_calibration,
                        rgb_camera_calibration,
                        depth_m,
                    )
                    rr.log(
                        f"world/device/{rgb_stream_label}/eye-gaze_projection",
                        rr.Points2D(
                            gaze_projection / args.down_sampling_factor, radii=4
                        ),
                    )


if __name__ == "__main__":
    main()
