# PX4 软件在环仿真测试手册

## 1. 功能说明
本手册用于指导测试人员搭建 PX4 无人机软件在环仿真环境，并验证飞控与感知算法的集成。

## 2. 软硬件环境
- 操作系统：Ubuntu 22.04
- ROS 版本：ROS 2 Humble
- 飞控固件：PX4-Autopilot（最新版）
- 仿真器：Gazebo Garden
- 地面站：QGroundControl（可选）

## 3. 安装步骤
1. 克隆 PX4 源码：`git clone git@github.com:PX4/PX4-Autopilot.git --recursive`
2. 运行安装脚本：`bash ./PX4-Autopilot/Tools/setup/ubuntu.sh`
3. 安装 MAVROS：`sudo apt install ros-humble-mavros ros-humble-mavros-extras -y`

## 4. 启动仿真
1. 启动 PX4 仿真：`make px4_sitl gz_x500`
2. 启动 MAVROS 桥接：`ros2 launch mavros px4.launch fcu_url:=udp://:14540@127.0.0.1:14557`
3. 运行自定义节点：`ros2 run py_pubsub px4_listener`

## 5. 测试用例
- [ ] PX4 仿真启动正常，Gazebo 显示无人机
- [ ] MAVROS 连接成功，无错误输出
- [ ] 自定义节点能实时打印飞机模式和解锁状态
- [ ] YOLO 检测节点能接收摄像头图像并输出检测结果

## 6. 常见故障排除
- HTTPS 克隆失败 → 改用 SSH
- 子模块下载不全 → 手动 `git submodule update --init`
- 找不到话题 → 用 `ros2 topic list` 检查话题名
