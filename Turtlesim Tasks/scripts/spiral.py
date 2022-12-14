#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('spiral')

pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

rate = rospy.Rate(2)

x = 0.5

while not rospy.is_shutdown():
    msg = Twist()
    msg.linear.x = x
    msg.linear.y = 0.0
    msg.linear.z = 0.0
    msg.angular.x = 0.0
    msg.angular.y = 0.0
    msg.angular.z = 4.0
    pub.publish(msg)
    rate.sleep()
    x += 0.5