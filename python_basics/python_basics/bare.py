import rclpy

def main(args=None):

    rclpy.init(args=args)

    node = rclpy.create_node("bare_node")

    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
