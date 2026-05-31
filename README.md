# turtle-sim-project
# turtle-sim-project
# Introduction to ROS2 — Virtual Robot Publisher/Subscriber

**Author:** Shaikh Avesh
**Roll Number:** c2103
**Task:** Robotics Club Intermediate Software Assignment (#3)

## Project Overview
This repository contains a ROS2 (Humble) package demonstrating a foundational Publisher/Subscriber architecture using the Turtlesim simulator. It serves as an introduction to middleware communication in autonomous systems.

## Key Deliverables Completed
- [x] Configured a complete ROS2 Humble environment on Ubuntu 22.04 (WSL2).
- [x] Built a `turtle_publisher` node to stream automated `geometry_msgs/Twist` velocity commands.
- [x] Built a `turtle_subscriber` node to intercept and log real-time telemetry data.
- [x] Successfully visualized the communication pipeline using the Turtlesim simulator.

## Run Instructions
1. Clone this repository into the `src` folder of a valid ROS2 workspace.
2. Build the package: `colcon build --symlink-install`
3. Source the workspace: `source install/setup.bash`
4. Launch the nodes:
   - Node 1: `ros2 run turtlesim turtlesim_node`
   - Node 2: `ros2 run my_robot_controller draw_circle`
   - Node 3: `ros2 run my_robot_controller log_velocity`
