#!/usr/bin/env python

from move import WritingTurtle
import rospy


if __name__ == '__main__':

	try:
	
		rospy.init_node('turtle2')
		turtle = WritingTurtle('/turtle2/cmd_vel', '/turtle2/pose')
		turtle.letterA()
		
		
	except rospy.ROSInterruptException:
		pass
