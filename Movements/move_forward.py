#!/usr/bin/env python3

import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_msgs.msg import String


def get_pose_info(info):
    current_position.x = info.x
    current_position.y = info.y
    current_position.theta = info.theta


def get_initial_position():
	initial_position = 0
	for i in range(10):
		rospy.Subscriber('/turtle1/pose', Pose, get_pose_info)
		initial_position = current_position.x
		rate.sleep()
	return initial_position
		 

def move_forward(distance):
	print('Turtle needs to move {} units forward in X direction'.format(distance))
	print('The initial X position is:', round(get_initial_position(), 1))
	desired_position = (get_initial_position() + distance)
	while not rospy.is_shutdown():
		goal = abs(current_position.x - desired_position)
		if(goal > 0.01):
			vel.linear.x = 1
			pub.publish(vel)
		
		else:
			vel.linear.x = 0
			pub.publish(vel)
			break
		rate.sleep()
	print('The final X position is : ', round(current_position.x, 1))	



	
if __name__ == '__main__':
    try:
        rospy.init_node('Leonardo')
        pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
        vel = Twist()
        current_position = Pose()
        rate = rospy.Rate(100)

        move_forward(2.5)

        

    except rospy.ROSInterruptException:
        pass
