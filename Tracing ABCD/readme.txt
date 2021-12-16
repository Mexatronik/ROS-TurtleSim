ROS distribution used: "ROS-Kinetic" on Ubuntu 16.04 
You can use ROS Melodic or ROS Noetic
ROS Noetic is RECOMMENDED since its EOL is May, 2025
List of ROS Distributions:  http://wiki.ros.org/Distributions

------------------------------------

move.py contains class WritingTurtle

all other python programs import WritingTurtle from move module 

Create a ros package, build and compile created package (I added rospy and std_msgs dependencies)

Instructions on how to create a package: http://wiki.ros.org/ROS/Tutorials/CreatingPackage

run the program Linux in terminal with ./mce312.sh

-------------------------------------

bash script 

if you are using latest ubuntu change '-e' to '--' in order to execute a command 
for example: 

gnome-terminal -e "rosrun turtlesim letterA.py" is on ubuntu 16.04

gnome-terminal -- rosrun turtlesim letterA.py  is on ubuntu 20.04 

---------------------------------------


