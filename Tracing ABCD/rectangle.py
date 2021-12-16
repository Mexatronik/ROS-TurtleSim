#!/usr/bin/env python

from move import WritingTurtle
import rospy


if __name__ == '__main__':
	try:
		rospy.init_node('turtle5')
		turtle = WritingTurtle('/turtle5/cmd_vel', '/turtle5/pose')
		turtle.rectangle()
		
	except rospy.ROSInterruptException:
		pass
