import sys
import argparse

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from rclpy.utilities import remove_ros_args
from demo_interfaces.msg import Counter

class ParameterNode(Node):

    __VERSION = "1.0.0"

    @staticmethod
    def parse_executable_args(argv):
        parser = argparse.ArgumentParser(
            description="Simple ROS 2 parameterized node"
        )
        parser.add_argument(
            "--version",
            action="store_true",
            help="Show the current version of this node.",
        )
        return parser.parse_args(remove_ros_args(argv)[1:])

    def __init__(self, show_version: bool = False):
        super().__init__("counter")

        self.declare_parameter("topic", "/counter")
        self.declare_parameter("initial_value", 0)
        self.declare_parameter("hz", 2)

        param_topic = str(self.get_parameter("topic").value)
        param_period_sec = 1/(float(self.get_parameter("hz").value))
        param_initial_value = float(self.get_parameter("initial_value").value)

        if show_version:
            self.get_logger().info(f"current version: {self.__VERSION}")

        # Note: Our Counter.msg is expecting a int64 value
        self.__count = int(param_initial_value)

        self.__pub = self.create_publisher(Counter, param_topic, 10)

        timer = self.create_timer(param_period_sec, self.callback)

    def callback(self):
        msg = Counter()
        msg.count = self.__count
        self.__pub.publish(msg)
        self.get_logger().info(f"Publishing count: {self.__count}")
        self.__count += 1

def main(argv=None):

    argv = sys.argv if argv is None else argv

    rclpy.init(args=argv)

    exec_args = ParameterNode.parse_executable_args(argv)
    node = ParameterNode(show_version=exec_args.version)

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.try_shutdown()


if __name__ == "__main__":
    main()
