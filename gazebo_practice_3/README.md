# Practice 3 : How to spawn a robot in Gazebo

In order to spawn a robot with Gazebo running, we need model files that define Gazebo model we want to spawn and 'spawn_model' node from 'gazebo_ros' package.

When spawning a robot, xacro command is used to pass related arguments, such as spawning pose and positions.

Custom model files have to be positioned under current pacakage directory.
