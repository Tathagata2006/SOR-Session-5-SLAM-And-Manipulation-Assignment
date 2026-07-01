# Submission Codebase

This folder contains the complete ROS 2 workspaces developed for the assignment.

## Structure

```
Submission_Codebase/
├── ros2_slam_ws/
└── ros2_arm_ws/
```

## Q1 – Automated Patroller

**Workspace:** `ros2_slam_ws`

**Custom Package:** `nav2_waypoint_patrol`

**Main File:**
- `waypoint_patrol.py`

Implements a ROS 2 Action Client using Nav2's `FollowWaypoints` action to autonomously navigate through three predefined waypoints while providing waypoint status feedback in the terminal.

---

## Q2 – Custom Inverse Kinematics

**Workspace:** `ros2_arm_ws`

**Custom Package:** `ik_controller`

**Main File:**
- `trajectory_controller.py`

Implements direct robotic arm control by publishing `JointTrajectory` messages using manually derived inverse kinematics joint angles, without using MoveIt.

---

Thankyou!
