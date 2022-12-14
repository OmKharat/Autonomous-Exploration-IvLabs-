#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('teleop',anonymous=True)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size= 10)


msg = Twist()
pub.publish(msg)

while not rospy.is_shutdown():
    key = input("Enter Key: ")
    if key == 'w':
        msg.linear.x = 1
        msg.angular.z = 0
        pub.publish(msg)
    elif key == 'a':
        msg.linear.x = 0
        msg.angular.z = 0.5
        pub.publish(msg)
    elif key == 'x':
        msg.linear.x = -1
        msg.angular.z = 0
        pub.publish(msg)
    elif key == 'd':
        msg.linear.x = 0
        msg.angular.z = -0.5
        pub.publish(msg)
    elif key == 's':
        msg.linear.x = 0
        msg.angular.z = 0
        pub.publish(msg)

rospy.spin()
