#!/usr/bin/env python

from move import WritingTurtle
import rospy


if __name__ == '__main__':

	try:
	
		rospy.init_node('turtle1')
		turtle = WritingTurtle('/turtle1/cmd_vel', '/turtle1/pose') # two arguments: 1) name of the publisher. 2) name of the subscriber
		turtle.letterB()
		
	except rospy.ROSInterruptException:
	
		pass
