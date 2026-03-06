import rclpy
from rclpy.node import Node
from rclpy.qos import (
    QoSProfile, 
    QoSHistoryPolicy, 
    QoSReliabilityPolicy, 
    QoSDurabilityPolicy,
    qos_profile_sensor_data
)
from demo_interfaces.msg import Counter

class PublisherNode(Node):

    def __init__(self, node_name: str = "publisher") -> None:
        super().__init__(node_name)

        # the default QoS
        # qos = qos_profile_sensor_data

        # sensor-like QoS
        qos = QoSProfile(
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=10,
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
            durability=QoSDurabilityPolicy.VOLATILE
        )

        self.__pub = self.create_publisher(Counter, "/counter", qos)

        self.create_timer(0.1, self.pub_callback)

    def pub_callback(self):
        self.__pub.publish(Counter())


def main(args=None) -> None:

    rclpy.init(args=args)

    node = PublisherNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.try_shutdown()

    rclpy.shutdown()



if __name__ == "__main__":
    main()
