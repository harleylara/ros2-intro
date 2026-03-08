from launch import LaunchDescription, LaunchContext
from launch.actions import LogInfo, OpaqueFunction
from launch.launch_introspector import LaunchIntrospector

def dump_context(context: LaunchContext, *args, **kwargs):

    print("\nLaunchContext:")
    print(f"context (LaunchContext): {context}")
    print(f"argv: {list(context.argv)}")
    print(f"noninteractive: {context.noninteractive}")
    print(f"is_shutdown: {context.is_shutdown}")
    print(f"launch_configurations: {dict(context.launch_configurations)}")
    print(f"locals: {context.get_locals_as_dict()}")

    # This can be huge
    # print("environment:", dict(context.environment))

    return []

def generate_launch_description() -> LaunchDescription:

    ld = LaunchDescription()

    ld.add_action(LogInfo(msg="Hello Launch"))

    ld.add_action(OpaqueFunction(function=dump_context))

    print("\nLaunch tree:")
    print(LaunchIntrospector().format_launch_description(ld))

    return ld
