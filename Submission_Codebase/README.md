# Submission Codebase

This folder contains the complete ROS 2 workspaces developed for the assignment.

## Structure

```
Submission_Codebase/
├── ros2_slam_ws/
└── ros2_arm_ws/
```

## Q1 – The Automated Patroller (Nav2 Waypoints)

**Workspace:** `ros2_slam_ws`

**Custom Package:** `nav2_waypoint_patrol`

**Main File:**
- `waypoint_patrol.py`

Implements a ROS 2 Action Client using Nav2's `FollowWaypoints` action to autonomously navigate through three predefined waypoints while providing waypoint status feedback in the terminal.

---

## Q2 – Math to the Rescue (Custom Inverse Kinematics)

**Workspace:** `ros2_arm_ws`

**Custom Package:** `ik_controller`

**Main File:**
- `trajectory_controller.py`

Implements direct robotic arm control by publishing `JointTrajectory` messages using manually derived inverse kinematics joint angles, without using MoveIt.

---

For simplicity, I have included only the src directories, which contain all the custom ROS 2 packages and Python scripts developed for this assignment. The build, install, and log directories have been omitted as they are generated automatically during the build.

---

Thankyou!
