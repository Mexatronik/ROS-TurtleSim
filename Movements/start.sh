#!/bin/bash

gnome-terminal -- roscore
sleep 2
gnome-terminal -- rosrun turtlesim turtlesim_node
sleep 2
gnome-terminal -- rostopic echo /turtle1/pose

