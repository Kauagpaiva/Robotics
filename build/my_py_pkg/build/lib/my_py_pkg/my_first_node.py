#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class My_node(Node):
    def __init__(self):
        super().__init__('py_test')
        self.counter_ = 0
        self.get_logger().info("Hello world ros2")
        self.create_timer(0.5, self.timer_callback) # Every 0.5 seconds it calls the timer_callback function

    def timer_callback(self):
        self.counter_ += 1
        self.get_logger().info("hello " + str(self.counter_))

def main(args=None):
    rclpy.init(args=args) # initializing ros2 communication
    node = My_node()
    rclpy.spin(node)
    rclpy.shutdown() # ends ros2 communication

if __name__ == "__main__":
    main()