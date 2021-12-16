#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


def get_pose_info(info):
	
	current_position.x = info.x
	current_position.y = info.y
	current_position.theta = info.theta
	
	

def move(pos_x): # a function to move a turtle based on desired linear.x position. Turtle has to da face x - dir, arguement is x position not distance to travel
	
	while not rospy.is_shutdown():
		rospy.Subscriber('/turtle1/pose', Pose, get_pose_info) # request turtle's current position
		goal_x = abs(current_position.x - pos_x) # caculating the distance to the desired position.x in absolute terms
				
		if (goal_x > 0.01):
			vel.linear.x = 1
			pub.publish(vel)	
		
		else:
			vel.linear.x = 0
			pub.publish(vel)
			break
		rate.sleep()

'''
def move_distance(distance, True):
			
	while not rospy.is_shutdown():
		
		rospy.Subscriber('/turtle1/pose', Pose, get_pose_info) # requests turtle's current position
		if (current_position.x > 0)	:
			
		final_position = abs(current_position.x - 
		if True:
			
	'''
	
	
def print_stuff(dist):
	final_pos = 0
	for i in range(10):
		rospy.Subscriber('/turtle1/pose', Pose, get_pose_info)
		if (current_position.x > 0):
			final_pos = (current_position.x + dist)
			rate.sleep()
			
	print(final_pos)

		
	

if __name__ == '__main__':

	try:
		rospy.init_node('Leonardo')
		pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
		vel = Twist()
		current_position = Pose()
		rate = rospy.Rate(100)
		#move(7)
		#move_distance(2)
		#print(current_position.x)
		
		print_stuff(2)
		
		
	except rospy.ROSInterruptException:
		
		pass


