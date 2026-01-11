#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "tf2_ros/static_transform_broadcaster.h"
#include "geometry_msgs/msg/transform_stamped.hpp"

// #include "tf2/LinearMath/Quaternion.h" // usefull utility for Quaternion operations


class StaticBroadcasterNode : public rclcpp::Node {
public:
  explicit StaticBroadcasterNode()
  : Node("static_broadcaster_demo") {

    parent_frame_ = declare_parameter<std::string>("parent_frame", "");
    child_frame_ = declare_parameter<std::string>("child_frame", "");

    if (parent_frame_.empty()) {
      RCLCPP_ERROR_STREAM(
          this->get_logger(),
          "'parent_frame' parameter is required"
      );
    }

    if (child_frame_.empty()) {
      RCLCPP_ERROR_STREAM(
          this->get_logger(),
          "'child_frame' parameter is required"
      );
    }

    static_tf_ = std::make_shared<tf2_ros::StaticTransformBroadcaster>(this);
    geometry_msgs::msg::TransformStamped t_;

    this->make_transforms();
  }

private:

  void make_transforms() {
    t_.header.stamp = this->get_clock()->now();
    t_.header.frame_id = parent_frame_;
    t_.child_frame_id = child_frame_;

    t_.transform.translation.x = 0.5;
    t_.transform.translation.y = 0.0;
    t_.transform.translation.z = 1.0;

    t_.transform.rotation.x = 0.0;
    t_.transform.rotation.y = 0.0;
    t_.transform.rotation.z = 0.0;
    t_.transform.rotation.w = 1.0;

    static_tf_->sendTransform(t_);
  }

  std::string parent_frame_;
  std::string child_frame_;

  std::shared_ptr<tf2_ros::StaticTransformBroadcaster> static_tf_;
  geometry_msgs::msg::TransformStamped t_;
};


int main(int argc, char* argv[]) {

  rclcpp::init(argc, argv);

  auto node = std::make_shared<StaticBroadcasterNode>();

  rclcpp::spin(node);
  rclcpp::shutdown();

  return 0;
}
