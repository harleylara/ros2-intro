import rclpy
from rclpy.node import Node
from rclpy.duration import Duration
from demo_interfaces.msg import Counter

from rclpy.qos import QoSProfile, QoSHistoryPolicy, QoSReliabilityPolicy
from rclpy.event_handler import SubscriptionEventCallbacks


class DeadlineSub(Node):
    def __init__(self) -> None:
        super().__init__("deadline_sub")

        qos = QoSProfile(
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=10,
            reliability=QoSReliabilityPolicy.RELIABLE,
            deadline=Duration(seconds=0.2),  # expect data at least every 200ms
        )

        def on_deadline(event):
            # event is an rmw_requested_deadline_missed_status_t-like object
            total = getattr(event, "total_count", "?")
            delta = getattr(event, "total_count_change", "?")
            self.get_logger().warn(f"DEADLINE MISSED (total={total}, +{delta})")

        ev = SubscriptionEventCallbacks(deadline=on_deadline)

        self.sub = self.create_subscription(
            Counter,
            "/deadline_topic",
            self.cb,
            qos,
            event_callbacks=ev,
        )

    def cb(self, msg: Counter):
        self.get_logger().info(f"RX: {msg.count}")


def main(args=None) -> None:

    rclpy.init(args=args)
    node = DeadlineSub()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.shutdown()


if __name__ == "__main__":
    main()
