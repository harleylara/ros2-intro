import rclpy
from rclpy.node import Node
from rclpy.qos import (
    QoSProfile, 
    QoSHistoryPolicy, 
    QoSReliabilityPolicy, 
    QoSDurabilityPolicy,
)
from demo_interfaces.msg import Counter

class SubscriberNode(Node):

    def __init__(self, node_name: str = "subscriber") -> None:
        super().__init__(node_name)

        qos = QoSProfile(
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=10,
            reliability=QoSReliabilityPolicy.RELIABLE,
            durability=QoSDurabilityPolicy.VOLATILE
        )
        # creating the entity
        self.__sub = self.create_subscription(Counter, "/counter", self.counter_callback, qos)

    def counter_callback(self, msg):
        self.get_logger().info(f"Got: {msg.count}")


def main(args=None) -> None:

    rclpy.init(args=args)

    node = SubscriberNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.shutdown()


if __name__ == "__main__":
    main()
