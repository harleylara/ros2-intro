from launch import LaunchDescription
from launch.actions import (
    ExecuteProcess,
    LogInfo,
    ExecuteProcess
)

def generate_launch_description() -> LaunchDescription:

    ld = LaunchDescription()

    ld.add_action(ExecuteProcess(
        cmd=['ls', '-las'],
        name='my_ls_process',  # this is optional
        additional_env={'env_variable': 'env_var_value'},
        # condition=IfCondition(LaunchConfiguration('open_gui')),
        output='both',
    ))

    ld.add_action(
        LogInfo(msg="hello")
    )

    return ld
