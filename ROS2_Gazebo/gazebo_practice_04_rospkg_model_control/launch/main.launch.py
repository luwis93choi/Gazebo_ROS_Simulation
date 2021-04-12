import launch

from launch import LaunchDescription
from launch_ros import actions
from launch_ros.actions import Node

import os

package_name = 'gazebo_practice_04_rospkg_model_control'

WS_current_dir = os.getcwd()
print('Current Workspace Directory : {}'.format(WS_current_dir))

Package_dir = WS_current_dir + '/src/' + package_name
print('Package Directory : {}'.format(Package_dir))

def generate_launch_description():

    # Gazebo launch instance
    gazebo = launch.actions.ExecuteProcess(
        cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so',
             Package_dir + '/world/main_world.world'],
        output='screen'
    )

    spawn_2WD_agent = Node(
        package='gazebo_ros',
        node_executable='spawn_entity.py',
        arguments=['-entity', 'agent_gazebo', '-file',
                   Package_dir + '/models/2WD_agent/model.sdf'],
        output='screen'
    )

    return LaunchDescription([
        gazebo, 
        spawn_2WD_agent,
    ])