#include "rclcpp/rclcpp.hpp"

using namespace std::chrono_literals;

class Logger : public rclcpp::Node {
    public:
        Logger() : Node("logger_node") {
            counter_ = 0;
            timer_ = this->create_wall_timer(500ms, std::bind(&Logger::timer_callback, this));
        }

    private:
        void timer_callback() {
            RCLCPP_INFO(this->get_logger(), "Hello %d", counter_);
            counter_++;
        }
        rclcpp::TimerBase::SharedPtr timer_;
        int counter_;

};

int main(int argc, char *argv[]) {

    rclcpp::init(argc, argv);

    auto node = std::make_shared<Logger>();

    rclcpp::spin(node);

    rclcpp::shutdown();

    return 0;
}
