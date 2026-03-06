import rclpy
from rclpy.node import Node
from rclpy.qos import (
    QoSProfile,
    QoSHistoryPolicy,
    QoSReliabilityPolicy,
    QoSDurabilityPolicy
)
from demo_interfaces.msg import Counter


class LatchedPub(Node):
    def __init__(self):
        super().__init__("latched_pub")

        qos = QoSProfile(
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=1,
            reliability=QoSReliabilityPolicy.RELIABLE,
            durability=QoSDurabilityPolicy.TRANSIENT_LOCAL,
        )

        self.pub = self.create_publisher(Counter, "/counter", qos)

        # Publish once, then keep spinning so late-joiners can get the cached sample.
        msg = Counter()
        msg.count = 0
        self.pub.publish(msg)
        self.get_logger().info("Published counter value once; staying alive for late subscribers.")

        self.timer = self.create_timer(1.0, lambda: None)


def main(args=None):

    rclpy.init(args=args)

    node = LatchedPub()

    try:
        rclpy.spin(node)
    finally:
        rclpy.shutdown()


if __name__ == "__main__":
    main()
