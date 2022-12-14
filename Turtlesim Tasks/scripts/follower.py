#!/usr/bin/env python3

import turtlesim.srv
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import atan2

def position_lead(msg3):
    global pose1
    pose1 = Pose()
    pose1 = msg3
    x0 = round(pose1.x,4)
    y0 = round(pose1.y,4)
    theta0 = pose1.theta

def position_follow(msg4):
    global pose2
    
    pose2 = msg4
    x1 = round(pose2.x,4)
    y1 = round(pose2.y,4)
    theta1 = pose2.theta

rospy.init_node('gotogoal',anonymous=True)
sub_lead = rospy.Subscriber('/turtle1/pose', Pose, position_lead)
rospy.wait_for_service("spawn")
spawner = rospy.ServiceProxy("spawn", turtlesim.srv.Spawn)
spawner(8,2,0,"turtle2")
pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size= 10)
sub_follow = rospy.Subscriber('/turtle2/pose', Pose, position_follow)

pose2 = Pose()


distance = ((pose1.x-pose2.x)**2 + (pose1.y-pose2.y)**2)**(0.5)
angle = atan2((pose1.y-pose2.y),(pose1.x-pose2.x))
speed = 1.5*(distance)
ang_speed = 6*(angle-pose2.theta)
msg1 = Twist()
msg1.linear.x = 0
msg1.angular.z = 0
rate = rospy.Rate(10)
pub.publish(msg1)
while not rospy.is_shutdown():
    while(distance > 0.1):
        msg1.linear.x = 1.5*(distance)
        msg1.angular.z = 6*(angle-pose2.theta)
        distance = ((pose1.x-pose2.x)**2 + (pose1.y-pose2.y)**2)**(0.5)
        angle = atan2((pose1.y-pose2.y),(pose1.x-pose2.x))
        pub.publish(msg1)
        rate.sleep()
    msg1.linear.x = 0
    msg1.angular.z = 0
    distance = ((pose1.x-pose2.x)**2 + (pose1.y-pose2.y)**2)**(0.5)
    angle = atan2((pose1.y-pose2.y),(pose1.x-pose2.x))
    pub.publish(msg1)

rospy.spin()