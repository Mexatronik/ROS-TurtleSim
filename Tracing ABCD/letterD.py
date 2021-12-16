#!/usr/bin/env python

from move import WritingTurtle
import rospy


if __name__ == '__main__':

	try:
	
		rospy.init_node('turtle4')
		turtle = WritingTurtle('/turtle4/cmd_vel', '/turtle4/pose')
		turtle.letterD()
		
	except rospy.ROSInterruptException:
	
		pass
