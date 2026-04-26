#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from mavros_msgs.msg import State

class PX4StateListener(Node):
    def __init__(self):
        super().__init__('px4_state_listener')
        self.subscription = self.create_subscription(
            State,
            '/mavros/state',
            self.state_callback,
            10)
        self.subscription
        self.get_logger().info('PX4 State Listener started.')

    def state_callback(self, msg):
        armed_status = "Armed" if msg.armed else "Disarmed"
        self.get_logger().info(f'Mode: {msg.mode}, Armed: {armed_status}')

def main(args=None):
    rclpy.init(args=args)
    node = PX4StateListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
