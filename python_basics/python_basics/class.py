import sys
import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node


class MyNode(Node):

    def __init__(self) -> None:
        super().__init__("my_node")

        self.count = 0

        timer = self.create_timer(0.5, self.callback)


    def callback(self) -> None:

        self.get_logger().info(f"Hello {self.count}")

        self.count += 1


def main(args=None) -> None:

    rclpy.init(args=args)

    node = MyNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    except ExternalShutdownException:
        sys.exit(1)
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == "__main__":
    main()
