#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_msgs.msg import String



class WritingTurtle:

	def __init__(self, publisher_name, subscriber_name):
		
		self.subscriber_name = subscriber_name
		self.publisher_name = publisher_name
		self.pub = rospy.Publisher(publisher_name, Twist, queue_size=10)
		self.rate = rospy.Rate(100)
		self.vel = Twist()
		self.pose = Pose()
		

#---------------------------------


	def pose_update(self, data): # callback function to read data (x, y, theta) from topic called '/turtle1/pose'	
		self.pose.x = data.x
		self.pose.y = data.y
		self.pose.theta = data.theta
	

#---------------------------------------------------------------------


	def move_up(self, pos, speed):
			
		while not rospy.is_shutdown():
				
			rospy.Subscriber(self.subscriber_name, Pose, self.pose_update)	# subscribes to topic called /turtle1/pose'	
					
			if (self.pose.x < pos):						
				self.vel.linear.x = speed
				self.pub.publish(self.vel)
				
			if (self.pose.y < pos):
				self.vel.linear.x = speed
				self.pub.publish(self.vel)
				
			else:
				self.vel.linear.x = 0
				self.pub.publish(self.vel)
				break
				
			self.rate.sleep()
		

#---------------------------------------------------------------------
	def move_down(self, pos, speed):
	
		while not rospy.is_shutdown():	
		
			rospy.Subscriber(self.subscriber_name, Pose, self.pose_update)
			
			if (self.pose.x > pos):
				self.vel.linear.x = speed
				self.pub.publish(self.vel)
				
			if (self.pose.y > pos):
				self.vel.linear.x = 1
				self.pub.publish(self.vel)
				
			else:
				self.vel.linear.x = 0
				self.pub.publish(self.vel)
				break
				
			self.rate.sleep()

#---------------------------------------------------------------------------

	def move_right(self, pos, speed):
	
		while not rospy.is_shutdown():
			
			rospy.Subscriber(self.subscriber_name, Pose, self.pose_update)
			
			if (self.pose.x < pos):
				self.vel.linear.x = speed 
				self.pub.publish(self.vel)
				
			else:
				self.vel.linear.x = 0
				self.pub.publish(self.vel)
				break
				
			self.rate.sleep()

#----------------------------------------------------------------------------

	def move_left(self, pos, speed):
	
		while not rospy.is_shutdown():	
		
			rospy.Subscriber(self.subscriber_name, Pose, self.pose_update)
			
			if (self.pose.x > pos):
				self.vel.linear.x = speed
				self.pub.publish(self.vel)
				
			else:
				self.vel.linear.x = 0
				self.pub.publish(self.vel)
				break
				
			self.rate.sleep()

#----------------------------------------------------------------------------

	def rotate_left(self, angle_degree): # COUNTERCLOCKWISE rotation
	
		angle_rad = angle_degree * (math.pi/180)
		
		while not rospy.is_shutdown():
		
			rospy.Subscriber(self.subscriber_name, Pose, self.pose_update)
			
			if (self.pose.theta < angle_rad):	# from 0 to 2pi	
				self.vel.linear.x = 0
				self.vel.angular.z = 1
				self.pub.publish(self.vel)
				
			else: 
				self.vel.linear.x = 0
				self.vel.angular.z = 0
				self.pub.publish(self.vel)
				break
				
			self.rate.sleep()


#---------------------------------------------------------------------------

	def rotate_right(self, angle_degree): # CLOCKWISE rotation
	
		angle_rad = angle_degree * (math.pi/180)
		
		while not rospy.is_shutdown():
		
			rospy.Subscriber(self.subscriber_name, Pose, self.pose_update)
			
			if (self.pose.theta >= angle_rad):					
				self.vel.linear.x = 0
				self.vel.angular.z = -1
				self.pub.publish(self.vel)	
				
			else: 
				self.vel.linear.x = 0
				self.vel.angular.z = 0
				self.pub.publish(self.vel)
				break
				
			self.rate.sleep()



#------------------------------------------------------------------------------

	def turn_left(self, vel_x, vel_z):
	
		while not rospy.is_shutdown():
		
			rospy.Subscriber(self.subscriber_name, Pose, self.pose_update)
			
			if (self.pose.theta < math.pi):		# theta is in radians 
				self.vel.linear.x = vel_x
				self.vel.angular.z = vel_z
				self.pub.publish(self.vel)
				
			else:
				self.vel.linear.x = 0
				self.vel.angular.z = 0
				self.pub.publish(self.vel)
				break
				
			self.rate.sleep()

#----------------------------------------------------------------------------

	def turn_right(self, vel_x, vel_z):
	
		while not rospy.is_shutdown():
		
			rospy.Subscriber(self.subscriber_name, Pose, self.pose_update)
			
			if (self.pose.theta > 0):			
				self.vel.linear.x = vel_x
				self.vel.angular.z = -vel_z
				self.pub.publish(self.vel)
				
			else:
				self.vel.linear.x = 0
				self.vel.angular.z = 0
				self.pub.publish(self.vel)
				break
				
			self.rate.sleep()

		
#--------------------------

	def letterA(self):
	
		self.rotate_left(75)
		self.move_up(8.5, 1)
		self.rotate_left(285)
		self.move_down(5.5, 1)
		self.rotate_right(105)
		self.move_up(6.5, 1)
		self.rotate_left(180)
		self.move_left(1, 1)
		self.rotate_right(0)

		
	def letterB(self):
	
		self.turn_left(1, 1)
		self.rotate_right(10) # rotating to 10 degrees
		self.turn_left(0.5, 1)
		self.rotate_left(270)
		self.move_down(5.5, 1)
		self.rotate_left(359)

		
		
	def letterC(self):
		self.rotate_left(180)
		self.turn_right(1.5, 1)

				
		
		
	def letterD(self):
	
		self.turn_left(1.5, 1)
		self.rotate_left(270)
		self.move_down(5.5, 1)
		self.rotate_left(359)

		
		
	def rectangle(self):
	
		self.move_right(10.5, 3)
		self.rotate_left(90)
		self.move_up(9.2, 3)
		self.rotate_left(179.5)
		self.move_left(0.5, 3)
		self.rotate_left(270)
		self.move_down(4.5, 3)
		self.rotate_left(359)


#===================================================================================




