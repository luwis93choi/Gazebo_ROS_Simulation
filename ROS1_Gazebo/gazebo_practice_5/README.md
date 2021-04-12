# Practice 5 : How to use mesh file to create Gazebo model

> Reference Material 1 : Gazebo in 5 minutes by Construct
> https://www.youtube.com/playlist?list=PLK0b4e05LnzbHiGDGTgE_FIWpOCvndtYx

> Reference Material 2 : Download a 3D model and load it into a Gazebo simulation
> https://www.youtube.com/watch?v=aP4sDyrRzpU

Mesh file is 3D modeling data that can used for the visualization and kinematic definition of Gazebo model.

In order to create mesh file, we need 3D modeling tool, such as Sketch-up or Blender. Blender is recommended since it provides COLLADA export functions and full package services for free. Complex 3D designs of Gazebo model are made on 3D modeling tool and they are exported as COLLADA (.dae) file. COLLADA files are imported to Gazebo for simulation.

Also, Google 3D Warehouse provides an abundant source of open 3D modeling data that can be used freely.

With Google 3D Warehouse and Blender (Sketch-up if necessary), we can download 3D modeling designs we need and customize them to our needs   

### How to produce mesh files for Gazebo model
> 1. Download 3D modeling file (Sketch-up or COLLADA (.dae)) from 3D Warehouse
> 2. When working with Blender, import downloded COLLADA file and customize the 3D modeling to one's needs.   
When working with Sketch-up, import downloaded files, customize the design, and export them as COLLADA.
> 3. Place COLLADA files under "~/models/'name of model'/meshes" directory
> 4. At SDF file, use <mesh> tag along with <uri> tag in order to import COLLADA mesh data from COLLADA design file.