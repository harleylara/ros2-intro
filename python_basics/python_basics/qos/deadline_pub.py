import rclpy
from rclpy.node import Node
from demo_interfaces.msg import Counter

from rclpy.qos import QoSProfile, QoSHistoryPolicy, QoSReliabilityPolicy

class DeadlinePub(Node):

    def __init__(self):
        super().__init__("deadline_pub")

        self.__counter_msg = Counter()

        qos = QoSProfile(
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=10,
            reliability=QoSReliabilityPolicy.RELIABLE,
        )

        self.pub = self.create_publisher(Counter, "deadline_topic", qos)
        self.timer = self.create_timer(1.0, self.tick)  # 1 Hz (slow)

    def tick(self):
        self.pub.publish(self.__counter_msg)
        self.__counter_msg.count += 1


def main(args=None):

    rclpy.init(args=args)

    node = DeadlinePub()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.shutdown()


if __name__ == "__main__":
    main()
