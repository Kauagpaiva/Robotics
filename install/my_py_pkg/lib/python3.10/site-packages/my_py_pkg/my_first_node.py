#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args) # initializing ros2 communication

    node = Node('py_test') # creating a node object (the arg is the name of the node)

    node.get_logger().info("Hello world ros2") # print hello world

    rclpy.spin(node)

    rclpy.shutdown() # ends ros2 communication

if __name__ == "__main__":
    main()