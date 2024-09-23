import rclpy
from rclpy.node import Node
from demo_interfaces.msg import Counter

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__("publisher_node")

        self.__count = 0

        self.__pub = self.create_publisher(Counter, "/count", 10)

        timer = self.create_timer(0.5, self.callback)

    def callback(self):
        msg = Counter()
        msg.count = self.__count
        self.__pub.publish(msg)
        self.get_logger().info(f"Publishing count: {self.__count}")
        self.__count += 1

def main(args=None) -> None:

    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()

    rclpy.shutdown()

if __name__ == "__main__":
    main()
