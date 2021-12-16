#!/usr/bin/env python

from move import WritingTurtle
import rospy


if __name__ == '__main__':

	try:
	
		rospy.init_node('turtle3')
		turtle = WritingTurtle('/turtle3/cmd_vel', '/turtle3/pose')
		turtle.letterC()
		
	except rospy.ROSInterruptException:
	
		pass
