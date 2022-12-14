#!/usr/bin/env python3

import turtlesim.srv
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import atan2

def position_lead(msg3):
    global pose1
    pose1 = msg3
    

def position_follow2(msg4):
    global pose2
    pose2 = msg4

def position_follow3(msg4):
    global pose3
    pose3 = msg4

def position_follow4(msg4):
    global pose4
    pose4 = msg4
    

rospy.init_node('gotogoal',anonymous=True)
sub_lead = rospy.Subscriber('/turtle1/pose', Pose, position_lead)
rospy.wait_for_service("spawn")
spawner = rospy.ServiceProxy("spawn", turtlesim.srv.Spawn)
spawner(5.544445,2,0,"turtle2")
spawner(8.8889,2,0,"turtle3")
spawner(8.8889,5.544445,0,"turtle4")
pub2 = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size= 10)
sub_follow2 = rospy.Subscriber('/turtle2/pose', Pose, position_follow2)
pub3 = rospy.Publisher('/turtle3/cmd_vel', Twist, queue_size= 10)
sub_follow3 = rospy.Subscriber('/turtle3/pose', Pose, position_follow3)
pub4 = rospy.Publisher('/turtle4/cmd_vel', Twist, queue_size= 10)
sub_follow4 = rospy.Subscriber('/turtle4/pose', Pose, position_follow4)

pose1 = Pose()
pose2 = Pose()
pose3 = Pose()
pose4 = Pose()
distance = ((pose1.x-pose2.x)**2 + (pose1.y-pose2.y-3.44445)**2)**(0.5)
angle = atan2((pose1.y-pose2.y-3.44445),(pose1.x-pose2.x))
speed = 1.5*(distance)
ang_speed = 6*(angle-pose2.theta)
msg1 = Twist()
msg1.linear.x = 0
msg1.angular.z = 0
rate = rospy.Rate(10)
pub2.publish(msg1)
pub3.publish(msg1)
pub4.publish(msg1)
while not rospy.is_shutdown():
    while(distance > 0.1):
        msg1.linear.x = 1.5*(distance)
        msg1.angular.z = 6*(angle-pose2.theta)
        distance = ((pose1.x-pose2.x)**2 + (pose1.y-pose2.y-3.44445)**2)**(0.5)
        angle = atan2((pose1.y-pose2.y-3.44445),(pose1.x-pose2.x))
        pub2.publish(msg1)
        pub3.publish(msg1)
        pub4.publish(msg1)
        rate.sleep()
    msg1.linear.x = 0
    msg1.angular.z = 0
    distance = ((pose1.x-pose2.x)**2 + (pose1.y-pose2.y-3.44445)**2)**(0.5)
    angle = atan2((pose1.y-pose2.y-3.44445),(pose1.x-pose2.x))
    pub2.publish(msg1)
    pub3.publish(msg1)
    pub4.publish(msg1)

rospy.spin()