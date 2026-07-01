#!/usr/bin/env python3

import rclpy

from rclpy.node import Node

from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint

from builtin_interfaces.msg import Duration


class IKTrajectoryPublisher(Node):

    def __init__(self):

        super().__init__("ik_trajectory_publisher")

        self.publisher = self.create_publisher(
            JointTrajectory,
            "/arm_controller/joint_trajectory",
            10
        )

        self.timer = self.create_timer(1.0, self.publish_trajectory)


    def publish_trajectory(self):


        msg = JointTrajectory()

        msg.joint_names = [
            "shoulder_pan_joint",
            "shoulder_lift_joint",
            "elbow_joint",
            "wrist_joint",
        ]

        point = JointTrajectoryPoint()

        # Joint angles obtained from Part A
        point.positions = [
            0.464,
            0.242,
            1.456,
            -1.698,
        ]

        point.velocities = [0.0, 0.0, 0.0, 0.0]

        point.time_from_start = Duration(
            sec=5,
            nanosec=0
        )

        msg.points.append(point)

        self.publisher.publish(msg)

        self.get_logger().info("========================================")
        self.get_logger().info("Publishing trajectory point...")
        self.get_logger().info("Target Coordinate : (0.30, 0.15, 0.35)")

        self.get_logger().info(
            f"Shoulder Pan  : {point.positions[0]:.3f} rad"
        )
        self.get_logger().info(
            f"Shoulder Lift : {point.positions[1]:.3f} rad"
        )
        self.get_logger().info(
            f"Elbow         : {point.positions[2]:.3f} rad"
        )
        self.get_logger().info(
            f"Wrist         : {point.positions[3]:.3f} rad"
        )

        self.get_logger().info("Trajectory published successfully.")
        self.get_logger().info("========================================")


def main(args=None):

    rclpy.init(args=args)

    node = IKTrajectoryPublisher()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
