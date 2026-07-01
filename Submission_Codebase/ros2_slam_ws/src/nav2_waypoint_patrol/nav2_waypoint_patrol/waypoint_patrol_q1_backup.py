#!/usr/bin/env python3

import math

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from nav2_msgs.action import FollowWaypoints
from geometry_msgs.msg import PoseStamped
from builtin_interfaces.msg import Time


class WaypointPatrol(Node):

    def __init__(self):
        super().__init__('waypoint_patrol')

        self.client = ActionClient(
            self,
            FollowWaypoints,
            '/follow_waypoints'
        )

        self.last_feedback = -1

        self.get_logger().info("Waiting for Nav2 FollowWaypoints server...")

        self.client.wait_for_server()

        self.get_logger().info("Connected!")

        self.send_waypoints()


    def make_pose(self, x, y, yaw):

        pose = PoseStamped()

        pose.header.frame_id = "map"
        pose.header.stamp = Time()

        pose.pose.position.x = x
        pose.pose.position.y = y
        pose.pose.position.z = 0.0

        pose.pose.orientation.z = math.sin(yaw / 2.0)
        pose.pose.orientation.w = math.cos(yaw / 2.0)

        return pose

    def send_waypoints(self):

        goal_msg = FollowWaypoints.Goal()

        goal_msg.poses = [

            self.make_pose(0.626, -0.576, -0.264),

            self.make_pose(1.222, 1.117, -0.865),

            self.make_pose(1.943, 0.429, -0.347),

        ]

        self.get_logger().info("Sending 3 patrol waypoints...")

        future = self.client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )

        future.add_done_callback(self.goal_response_callback)


    def goal_response_callback(self, future):

        self.goal_handle = future.result()

        if not self.goal_handle.accepted:

            self.get_logger().info("Goal rejected")
            return

        self.get_logger().info("Goal accepted!")

        result_future = self.goal_handle.get_result_async()

        result_future.add_done_callback(self.result_callback)


    def feedback_callback(self, feedback_msg):

        current = feedback_msg.feedback.current_waypoint

        if current != self.last_feedback:

            if self.last_feedback != -1:

                self.get_logger().info(
                    f"Waypoint {self.last_feedback + 1} Reached!"
                )

            self.get_logger().info(
                f"Navigating to Waypoint {current + 1}..."
            )

            self.last_feedback = current

    def result_callback(self, future):

        if self.last_feedback != -1:

            self.get_logger().info(
                f"Waypoint {self.last_feedback + 1} Reached!"
            )

        result = future.result().result

        if len(result.missed_waypoints) == 0:

            self.get_logger().info("Patrol Complete!")

        else:

            self.get_logger().warn(
                f"Missed waypoints: {result.missed_waypoints}"
            )

        rclpy.shutdown()

def main(args=None):

    rclpy.init(args=args)

    node = WaypointPatrol()

    rclpy.spin(node)


if __name__ == "__main__":
    main()
