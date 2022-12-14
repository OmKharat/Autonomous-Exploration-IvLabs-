#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('star')

pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

rate = rospy.Rate(2)

while not rospy.is_shutdown():
    msg = Twist()
    msg.linear.x = 3.0
    msg.linear.y = 0.0
    msg.linear.z = 0.0
    msg.angular.x = 0.0
    msg.angular.y = 0.0
    msg.angular.z = -0.1
    pub.publish(msg)
    rate.sleep()
    msg.linear.x = 0.0
    msg.linear.y = 3.0
    msg.linear.z = 0.0
    msg.angular.x = 0.0
    msg.angular.y = 0.0
    msg.angular.z = -0.1
    pub.publish(msg)
    rate.sleep()
    msg.linear.x = -3.0
    msg.linear.y = 0.0
    msg.linear.z = 0.0
    msg.angular.x = 0.0
    msg.angular.y = 0.0
    msg.angular.z = -0.1
    pub.publish(msg)
    rate.sleep()
    msg.linear.x = 0.0
    msg.linear.y = -3.0
    msg.linear.z = 0.0
    msg.angular.x = 0.0
    msg.angular.y = 0.0
    msg.angular.z = -0.1
    pub.publish(msg)
    rate.sleep()