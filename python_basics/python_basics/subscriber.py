import sys
import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from demo_interfaces.msg import Counter

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__("subscriber_node")

        self.__sub = self.create_subscription(Counter, "/count", self.callback, 10)

    def callback(self, msg) -> None:
        self.get_logger().info(f"Got count: {msg.count}")


def main(args=None) -> None:

    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    try:
        rclpy.spin(minimal_subscriber)
    except KeyboardInterrupt:
        pass
    except ExternalShutdownException:
        sys.exit(1)
    finally:
        minimal_subscriber.destroy_node()
        rclpy.try_shutdown()

if __name__ == "__main__":
    main()
