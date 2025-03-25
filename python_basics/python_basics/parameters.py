import sys
import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node

class ParameterNode(Node):

    def __init__(self):
        super().__init__("parameter_node")

def main(args=None):

    rclpy.init(args=args)

    node = ParameterNode()

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
