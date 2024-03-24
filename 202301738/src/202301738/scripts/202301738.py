#!/usr/bin/env python3

import rospy
import math
from geometry_msgs.msg import Twist

def move():
	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	rospy.init_node('move', anonymous=True)
	rate = rospy.Rate(10)
	
	while not rospy.is_shutdown():
		mycontrol = Twist()
		mycontrol.linear.x = 8
		mycontrol.angular.z = 3
		rospy.loginfo("Linear X cmd vel : %s" %mycontrol.linear.x)
		rospy.loginfo("Angular Z cmd vel(rad) : %s" %mycontrol.angular.z)
		pub.publish(mycontrol)
		rate.sleep()

if __name__ == '__main__':
	try:
		move()
	except rospy.ROSInterruptException:
		pass
