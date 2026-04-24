#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_msgs.msg import DroneStatus

class DroneStatusPublisher(Node):
    def __init__(self):
        super().__init__('drone_status_publisher')
        self.publisher_ = self.create_publisher(DroneStatus,'drone_status',10)
        timer_period = 1.0
        self.timer = self.create_timer(timer_period,self.timer_callback)
        self.count_ = 0

    def timer_callback(self):
        msg = DroneStatus()
        msg.drone_id = f"uav_{self.count_}"
        msg.battery_voltage = 11.1 +self.count_ * 0.1
        msg.is_armed = (self.count_ %2 ==0)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing:{msg.drone_id},{msg.battery_voltage}V,Armed={msg.is_armed}')
        self.count_ += 1

def main(args=None):
    rclpy.init(args=args)
    node = DroneStatusPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
   main()
