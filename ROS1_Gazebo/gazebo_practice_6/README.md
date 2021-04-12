# Practice 6 : How to create Gazebo model using URDF and visualize it with Rviz

> Reference Material 1 : Gazebo in 5 minutes by Construct
> https://www.youtube.com/playlist?list=PLK0b4e05LnzbHiGDGTgE_FIWpOCvndtYx

URDF is composed of links and joints. Link is a part of the robot. Joint is virtual connection between links.

When writing URDF XML codes, Xacro (XML Macros) is used to simplify overall structure of URDF. In order to run URDF, xacro command has to be included as a parameter in launch file.

xacro --inorder option is now default run option. No need to include --inorder option for xacro.

Arguments necessary for spawning a Gazebo model (Coordinates, Poses, etc) can be passed to 'spawn_model' node of 'gazebo_ros' package    

<code>
&ltnode name="NODE_NAME" pkg="gazebo_ros" type="spawn_model" 
output="screen" args="-urdf -param ROBOT_DESCRIPTION_NAME -model MODEL_NAME -x $(arg x) -y $(arg y) -z $(arg z)"&gt
</code>
<br></br>

Rviz is used to debug URDF models' integrity and internal TF structures.
