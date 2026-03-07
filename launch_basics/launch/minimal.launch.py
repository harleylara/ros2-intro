from launch import LaunchDescription
from launch.actions import LogInfo

def generate_launch_description() -> LaunchDescription:

    ld = LaunchDescription()

    ld.add_action(
        LogInfo(msg="Hello Launch")
    )

    return ld
