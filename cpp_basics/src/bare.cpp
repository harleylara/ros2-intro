#include <memory>
#include "rclcpp/rclcpp.hpp"

int main(int argc, char *argv[]) {
    
    rclcpp::init(argc, argv);

    // 1. Very cpp way
    // std::shared_ptr<rclcpp::Node> node = std::shared_ptr<rclcpp::Node>(new rclcpp::Node("bare_node"));

    // 2. Still cpp way but just a bit better
    // std::shared_ptr<rclcpp::Node> node = std::make_shared<rclcpp::Node>("bare_node");

    // 3. Using some RCLCPP helpers
    // rclcpp::Node::SharedPtr node = std::make_shared<rclcpp::Node>("bare_node");

    // 4. Automatic type deduction
    // auto node = std::make_shared<rclcpp::Node>("bare_node");
    
    // 5. Best of both worlds CPP and RCLCPP
    auto node = rclcpp::Node::make_shared("bare_node");

    rclcpp::spin(node);

    rclcpp::shutdown();

    return 0;
}
