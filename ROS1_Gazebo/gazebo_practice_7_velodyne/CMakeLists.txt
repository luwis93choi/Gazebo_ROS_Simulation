cmake_minimum_required(VERSION 2.8.3)
project(gazebo_practice_7_velodyne)

# Find Gazebo
find_package(gazebo REQUIRED)
include_directories(${GAZEBO_INCLUDE_DIRS})
link_directories(${GAZEBO_LIBRARY_DIRS})
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${GAZEBO_CXX_FLAGS}")

# Build Gazebo Plugin
add_library(gazebo_practice_7_velodyne SHARED src/velodyne_plugin.cc)
target_link_libraries(gazebo_practice_7_velodyne ${GAZEBO_LIBRARIES})