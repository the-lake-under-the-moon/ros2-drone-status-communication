#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_msgs.msg import DroneStatus

class DroneStatusSubscriber(Node):
    def __init__(self):
        super().__init__('drone_status_subscriber')
        self.subscription = self.create_subscription(
            DroneStatus,
            'drone_status',
            self.listener_callback,
            10)
        self.subscription  # 防止被垃圾回收

    def listener_callback(self, msg):
        self.get_logger().info(f'Received: {msg.drone_id}, Voltage={msg.battery_voltage}V, Armed={msg.is_armed}')

def main(args=None):
    rclpy.init(args=args)
    node = DroneStatusSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
