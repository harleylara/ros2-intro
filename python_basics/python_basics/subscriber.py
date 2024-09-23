import rclpy
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

    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()

    rclpy.shutdown()

if __name__ == "__main__":
    main()
