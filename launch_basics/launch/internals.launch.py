from launch import LaunchDescription
from launch.actions import LogInfo
from launch.launch_introspector import LaunchIntrospector

def generate_launch_description() -> LaunchDescription:

    ld = LaunchDescription()

    ld.add_action(
        LogInfo(msg="Hello Launch")
    )

    print("Raw entities:", ld.entities)
    print()
    print("Tree view:")
    print(LaunchIntrospector().format_launch_description(ld))

    return ld
