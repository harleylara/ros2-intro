import math
import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from rclpy.task import sys
from demo_interfaces.srv import EuclideanDistance

class ServiceNode(Node):

    def __init__(self):
        super().__init__("service_node")

        self.__service = self.create_service(EuclideanDistance, "EuclideanDistance", self.compute_distance)


    def compute_distance(self, request, response):
        self.get_logger().info(f"Got a request: {request}")
        # simple calculation euclidean distance
        dx = request.goal.x - request.origin.x
        dy = request.goal.y - request.origin.y
        dz = request.goal.z - request.origin.z

        distance = math.sqrt(dx**2 + dy**2 + dz**2)
        response.distance = distance

        return response


def main(args=None):

    rclpy.init(args=args)

    node = ServiceNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    except ExternalShutdownException:
        sys.exit(1)
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == "__main__":
    main()
