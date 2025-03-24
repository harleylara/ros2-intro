import sys
import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from demo_interfaces.srv import EuclideanDistance
from rclpy.task import Future

class ClientAsync(Node):

    def __init__(self):
        super().__init__("service_client")

        self.client = self.create_client(EuclideanDistance, 'EuclideanDistance')
        while not self.client.wait_for_service(timeout_sec=2.0):
            self.get_logger().info('service not available, waiting again...')

        self.__request = EuclideanDistance.Request()

    def send_request(self) -> Future:
        # some testing values
        self.__request.origin.x = 0.0
        self.__request.origin.y = 0.0
        self.__request.origin.z = 0.0

        self.__request.goal.x = 2.0
        self.__request.goal.y = 2.0
        self.__request.goal.z = 0.0

        return self.client.call_async(self.__request)


def main(args=None):

    rclpy.init(args=args)

    node = ClientAsync()

    try:
        future = node.send_request()

        rclpy.spin_until_future_complete(node, future)

        response = future.result()

        node.get_logger().info(f"Euclidean distance: {response.distance:.4f} m")
    except KeyboardInterrupt:
        pass
    except ExternalShutdownException:
        sys.exit(1)
    finally:
        node.destroy_node()
        rclpy.shutdown()



if __name__ == "__main__":
    main()
