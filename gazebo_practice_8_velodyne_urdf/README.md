# Practice 8 : Use URDF for Velodyne 3D modeling and Control it through ROS

## URDF vs SDF

**URDF (Unified Robot Description Format)** is currently the standard description method for 3D models in ROS. As a result, when using Gazebo along with ROS, we have to use URDF in order to control Gazebo models through ROS-based programs. URDF can only define 3D modeling characteristics of robot models.

**SDF (Simulation Description Format)** is another standard description method for 3D models used by Gazebo. Although SDF can define robot models and world environment models, it cannot be directly controlled by ROS. In some cases, SDF is converted to URDF, so it can be utilized by ROS.

## Using URDF

Like SDF, URDF elements are defined as < robot >. Each < robot > must carry "name" as its required attribute. < robot > is composed of various < link > and < joint >. Each < link > represents individual physical elements of the robot. < joint > describes how each < link > interacts with each other.

When writing URDF for 3D models, we must include < inertia >, < collision >, < visual > tags in < link >. 

> According to ROS wiki (http://wiki.ros.org/urdf/XML/link), even though < inertia > is described as an optional element, in Gazebo with version lower than 9.15., Gazebo crashes if it is not written in URDF.   
>> **Reference : https://answers.gazebosim.org//question/21441/the-minimum-corner-of-the-box-must-be-less-than-or-equal-to-maximum-corner/**

- < inertia > that defines physical characteristics of the model must include < mass > and  < inertial >.
   - < mass > is the value for the weight of the robot. This value cannot be below 0. If it is wronly defined, Gazebo's physical engine crashes, which eventually leads to crashing Gazebo.

      > According to ROS wiki (http://wiki.ros.org/urdf/XML/link), < mass > is not specifically designated as a required element. Since < inertia > is consided as a required element in Gazebo with version lower than 9.15., < mass > must be correctly defined.

   - < inertial > describes how the robot or model will react to external force. 

      > According to ROS wiki (http://wiki.ros.org/urdf/XML/link), < inertial > is not specifically designated as a required element. Since < inertia > is consided as a required element in Gazebo with version lower than 9.15., < inertial > must be correctly defined.

- < collision > that defines collision characteristics of the model must include < geometry > that defines the overall description of the model's collision box.

- < visual > that defines visual description of the model must include < geometry > that defines what model looks like.

## When to use URDF? When to use SDF?

- URDF is used to write XML-based codes for 3D models that need to be controlled by ROS.

- SDF is used to write XML-based codes for 3D simulation environment.
  > This is due to URDF's limitations in describing the entire description of simulation environment.

## How to launch URDF models and SDF environment using ROS launch?

- URDF elements can be launched through 'spawn_model' node from 'gazebo_ros' package. Parameters for launching the models have to be passed using Xacro commands.

- SDF elements can be launched by including 'empty_world.world' from 'gazebo_ros' package in the launch file.

- URDF launch command XML codes and SDF launch command XML codes can be used in a single roslaunch file.

  > **However, just because launch codes of certain nodes are written at the back of the roslaunch, that does not mean that those nodes will be launched later. roslaunch file does not guarantee the sequence of node launches according to the sequence that they are written in launch code.** 