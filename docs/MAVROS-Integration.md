# MAVROS 集成记录

## 环境
- ROS 2 Humble
- PX4 SITL (Gazebo Garden, X500)
- MAVROS

## 安装与启动
1. sudo apt install ros-humble-mavros ros-humble-mavros-extras
2. ros2 launch mavros px4.launch fcu_url:=udp://:14540@127.0.0.1:14557

## 踩坑笔记
- PX4 启动后报“No connection to the GCS”，连接 MAVROS 后自动消失。
- 第一次忘记 source 工作空间，导致 mavros 启动失败。

## 验证
ros2 topic list | grep mavros 可见 /mavros/state, /mavros/imu 等话题。
