import rclpy

def main(args=None):

    rclpy.init(args=args)

    node = rclpy.create_node("logger_node")

    rate = node.create_rate(0.5)
    counter = 0

    while rclpy.ok():
        node.get_logger().info(f"hello {counter}")

        counter += 1

        rclpy.spin_once(node)

        rate.sleep()

if __name__ == "__main__":
    main()
