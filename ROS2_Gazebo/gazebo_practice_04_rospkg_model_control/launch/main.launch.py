import launch

from launch import LaunchDescription
from launch_ros import actions
from launch_ros.actions import Node

import os

import random

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

    # x, y pose for random model spawn
    random_spawn_x = random.uniform(-3, 3)  
    random_spawn_y = random.uniform(-3, 3)

    spawn_2WD_agent = Node(
        package='gazebo_ros',
        node_executable='spawn_entity.py',
        # spawn_entity.py arguments (https://github.com/ros-simulation/gazebo_ros_pkgs/wiki/ROS-2-Migration:-Spawn-and-delete#spawn-entity-node)
        arguments=['-entity', 'agent_gazebo', 
                   '-x {}'.format(random_spawn_x),  # Random spawn x pose
                   '-y {}'.format(random_spawn_y),  # Random spawn y pose
                   '-z 0', 
                   '-file',
                   Package_dir + '/models/2WD_agent/model.sdf'],
        output='screen'
    )

    return LaunchDescription([
        gazebo, 
        spawn_2WD_agent,
    ])