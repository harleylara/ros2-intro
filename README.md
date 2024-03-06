# ROS 2 - Introduction

## Installation

In the `src` folder of your workspace:
```
git clone https://github.com/harleylara/ros2-intro.git
cd ros2-intro
```

Get external repos:

```
sudo apt install python3-vcstool
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
