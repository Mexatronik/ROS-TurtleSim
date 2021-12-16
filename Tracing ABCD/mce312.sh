#!/bin/bash

echo '-----------Starting ROSCORE...---------'
gnome-terminal -e roscore
echo "ROSMASTER running" 
sleep 2
echo '---------Launching TurtleSim...--------'
gnome-terminal -e "rosrun turtlesim turtlesim_node"
echo "TurtleSim is running"
sleep 1
rosservice call turtle1/set_pen 0 0 0 3 on
rosservice call turtle1/teleport_absolute 3.7 5.5 0
rosservice call turtle1/set_pen 200 0 0 3 off
rosservice call /spawn 1 5.5 0 'turtle2'
rosservice call /spawn 7.1 5.5 0 'turtle3'
rosservice call /spawn 8.5 5.5 0 'turtle4'
rosservice call /spawn 0.5 4.5 0 'turtle5'
rosservice call turtle5/set_pen 0 0 200 3 off
rosservice call turtle3/set_pen 0 200 0 3 off
rosservice call turtle4/set_pen 10 10 10 3 off
rosrun turtle_sim2 letterA.py & rosrun turtle_sim2 letterB.py & rosrun turtle_sim2 letterC.py & rosrun turtle_sim2 letterD.py & rosrun turtle_sim2 rectangle.py 

echo '--------Simulation complete.-----------'





