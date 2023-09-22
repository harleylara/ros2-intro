# ROS 2 - Introduction

## Installation

```
git clone https://github.com/sea-bass/turtlebot3_behavior_demos.git
cd ros2-intro
```

Get external repos:

```
vcs import < .repos
```

In the ROOT directory of your workspace run (to install dependencies):

```
sudo apt update && rosdep install -r --from-paths . --ignore-src --rosdistro $ROS_DISTRO -y
```

## Launch Simulation

To run the simulation:

```
ros2 launch turtlebot3_gazebo turtlebot3_house.launch.py
```
