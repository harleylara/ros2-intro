import sys
import argparse

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from rclpy.utilities import remove_ros_args
from demo_interfaces.msg import Counter

def parse_executable_args(argv):
    parser = argparse.ArgumentParser(description="Simple ROS 2 Parametrized node")
    parser.add_argument("--show-params", default=False, help="Show a initial messages with values for the parameters", action='store_true')
    return parser.parse_args(remove_ros_args(argv)[1:])

class ParameterNode(Node):

    def __init__(self, show_params: bool):
        super().__init__("parameter_node")

        self.declare_parameter("topic", "/counter")
        self.declare_parameter("initial_value", 0)
        self.declare_parameter("hz", 2)

        param_topic = str(self.get_parameter("topic").value)
        param_period_sec = 1/(float(self.get_parameter("hz").value))
        param_initial_value = float(self.get_parameter("initial_value").value)

        if show_params:
            self.get_logger().info(f"topic: {param_topic}")
            self.get_logger().info(f"initial_value: {param_initial_value}")
            self.get_logger().info(f"hz: {float(self.get_parameter('hz').value)}")

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

    exec_args = parse_executable_args(argv)

    rclpy.init(args=argv)

    node = ParameterNode(exec_args.show_params)

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    except ExternalShutdownException:
        sys.exit(1)
    finally:
        rclpy.try_shutdown()


if __name__ == "__main__":
    main()
