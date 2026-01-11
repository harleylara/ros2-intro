import sys

import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import ParameterDescriptor

from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster
from geometry_msgs.msg import TransformStamped

class StaticBrodcaster(Node):

    def __init__(self):
        super().__init__("static_broadcaster_demo")

        self.__parent_frame = self.declare_parameter(
            "parent_frame",
            "",
            ParameterDescriptor(description="id of the parent frame.")
        ).get_parameter_value().string_value

        self.__child_frame = self.declare_parameter(
            "child_frame",
            "",
            ParameterDescriptor(description="id of the parent frame.")
        ).get_parameter_value().string_value

        if (self.__parent_frame == ""):
            self.get_logger().error("'parent_frame' parameter is required.")
            sys.exit(1)

        if (self.__child_frame == ""):
            self.get_logger().error("'child_frame' parameter is required.")
            sys.exit(1)

        self.__static_tf = StaticTransformBroadcaster(self)

        self.make_transforms()


    def make_transforms(self):
        self.get_logger().info(f"Starting static brodcaster from {self.__child_frame} -> {self.__parent_frame}")

        t = TransformStamped()

        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = self.__parent_frame
        t.child_frame_id = self.__child_frame

        # Note: Keep in mind that this transform define
        # where is the `child` frame with respect to the `parent` frame

        t.transform.translation.x = 2.0
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.0

        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0

        self.__static_tf.sendTransform(t)


def main(args=None) -> None:

    rclpy.init(args=args)

    node = StaticBrodcaster()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == "__main__":
    main()
