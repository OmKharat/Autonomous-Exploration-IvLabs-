#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import atan2

def position(msg3):
    global x0, y0, theta
    pose = msg3
    x0 = round(pose.x,4)
    y0 = round(pose.y,4)
    theta = pose.theta

rospy.init_node('gotogoal',anonymous=True)
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size= 10)
sub = rospy.Subscriber('/turtle1/pose', Pose, position)
pose = Pose()

x = float(input("Enter the x co-ordinate: "))
y = float(input("Enter the y co-ordinate: "))

distance = ((x-x0)**2 + (y-y0)**2)**(0.5)
angle = atan2((y-y0),(x-x0))
speed = 1.5*(distance)
ang_speed = 6*(angle-theta)
msg1 = Twist()
msg1.linear.x = 0
msg1.angular.z = 0
rate = rospy.Rate(10)
pub.publish(msg1)
while(distance > 0.1):
    msg1.linear.x = 1.5*(distance)
    msg1.angular.z = 6*(angle-theta)
    pub.publish(msg1)
    distance = ((x-x0)**2 + (y-y0)**2)**(0.5)
    angle = atan2((y-y0),(x-x0))
    rate.sleep()
msg1.linear.x = 0
msg1.angular.z = 0
x0 = x
y0 = y
pub.publish(msg1)


rospy.spin()

