# Practice 1 : How to launch your first Gazebo World using ROS

> Reference Materials : Gazebo in 5 minutes by Construct
> https://www.youtube.com/playlist?list=PLK0b4e05LnzbHiGDGTgE_FIWpOCvndtYx

In order to set up Gazebo simulation, we need 3 elements : Launch File / World File / Model File
- Launch File : Invoke Gazebo_ROS to start the program and Load world setting defined by World File
- World File : Define how the simulation environment is set up and designed
- Model File : Define each model used for the simulation

World File defines what will exhibit within the simulation environment and how it will interact with others
     
Use "include" tag in order to add objects in the simulation environment
     
In order for the objects to be included, Model Files have to be positioned at the right default file path : "/usr/share/gazebo-9/models" or "/home/000/.gazebo/models".
     
**By default, "/usr/share/gazebo-9/models" is referred as "model://" value in "uri" tag.**

> file:// = "/usr/share/gazebo-9"

> model:// = "/usr/share/gazebo-9/models"

**If it is not positioned properly, Gazebo_ROS will freeze.**

Therefore, in order to keep 3rd party Model Files in Gazebo_ROS, those files have to be moved to above file directory path.

**If we want to keep model files under current project directory, we have to change PATH variable of Gazebo by using < env > tag in launch file.**   

<code>
&ltenv name="GAZEBO_MODEL_PATH" value="$(find 'project_name')"/&gt
</code>   
<br></br>

**This will make Gazebo to look for alternate PATH when loading custom models.**

> (Reference 1 : "How to get the gazebo models after initial install" : https://gist.github.com/awesomebytes/982166e825aa23ecdaf9acf34fa0a330 )

> (Reference 2 : "How do I start Nautilus (Ubuntu File Directory Program) as root?" : https://askubuntu.com/questions/156998/how-do-i-start-nautilus-as-root )

> (Reference 3 : "OSRF (Open Source Robotics Foundation) Gazebo Model Package" : https://bitbucket.org/osrf/gazebo_models/src/default/ )
