#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

rospy.init_node("sq_spiral")
rospy.loginfo("Square spiral is being traced")

pub = rospy.Publisher('turtle1/cmd_vel',Twist, queue_size=10)

x,y = 1,1
rate = rospy.Rate(2)
while not rospy.is_shutdown():
    msg = Twist()
    msg.linear.x = x
    msg.linear.y = 0
    msg.linear.z = 0
    msg.angular.x = 0
    msg.angular.y = 0
    msg.angular.z = 0.0
    pub.publish(msg)
    rate.sleep()
    msg.linear.x = 0
    msg.linear.y = y
    msg.linear.z = 0
    msg.angular.x = 0
    msg.angular.y = 0
    msg.angular.z = 0.0
    pub.publish(msg)
    rate.sleep()
    x += 1
    y += 1
    msg.linear.x = -x
    msg.linear.y = 0
    msg.linear.z = 0
    msg.angular.x = 0
    msg.angular.y = 0
    msg.angular.z = 0.0
    pub.publish(msg)
    rate.sleep()
    msg.linear.x = 0
    msg.linear.y = -y
    msg.linear.z = 0
    msg.angular.x = 0
    msg.angular.y = 0
    msg.angular.z = 0.0
    pub.publish(msg)
    rate.sleep()

    x += 1
    y += 1