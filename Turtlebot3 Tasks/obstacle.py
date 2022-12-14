#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import statistics


global right, left, front1, front2

right = 0
left = 0
front1 = 0
front2 = 0

def region(msg):
    global right, left, front1, front2

    right = statistics.mode(msg.ranges[300:340])                       #msg.ranges[0]       
    front1 = statistics.mode(msg.ranges[0:20])
    front2 = statistics.mode(msg.ranges[340:359])                          #msg.ranges[30]      
    left  = statistics.mode(msg.ranges[20:60])                         #msg.ranges[330]     
    

rospy.init_node('obstacle_avoidance',anonymous=True)
sub = rospy.Subscriber('/scan', LaserScan, region)
pub = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=10)

msg1 = Twist()
pub.publish(msg1)

while not rospy.is_shutdown():
    if (front1 > 0.2 or front2 > 0.2) and left > 0.2 and right > 0.2:
        msg1.linear.x = 0.15
        msg1.angular.z = 0
        pub.publish(msg1)
    elif (front1 > 0.2 or front2 > 0.2) and left > 0.2 and right < 0.2:
        msg1.linear.x = 0
        msg1.angular.z = 0.6
        pub.publish(msg1)
        print('Obstalce Detected right')
    elif (front1 > 0.2 or front2 > 0.2) and left < 0.2 and right > 0.2:
        msg1.linear.x = 0
        msg1.angular.z = -0.6
        pub.publish(msg1)
        print('Obstalce Detected left')
    elif (front1 < 0.2 or front2 > 0.2) and left > 0.2 and right > 0.2:
        msg1.linear.x = 0
        msg1.angular.z = -0.6
        pub.publish(msg1)
        print('Obstalce Detected f-left')
    elif (front1 > 0.2 or front2 < 0.2) and left > 0.2 and right > 0.2:
        msg1.linear.x = 0
        msg1.angular.z = 0.6
        pub.publish(msg1)
        print('Obstalce Detected f-right')
    elif (front1 < 0.2 or front2 < 0.2) and left > 0.2 and right < 0.2:
        msg1.linear.x = 0
        msg1.angular.z = 0.6
        pub.publish(msg1)
        print('Obstalce Detected')
    elif (front1 < 0.2 or front2 < 0.2) and left < 0.2 and right > 0.2:
        msg1.linear.x = 0
        msg1.angular.z = -0.6
        pub.publish(msg1)
        print('Obstalce Detected')
    elif (front1 > 0.2 or front2 > 0.2) and left < 0.2 and right < 0.2:
        msg1.linear.x = 0.15
        msg1.angular.z = 0
        pub.publish(msg1)
        print('Obstalce Detected')
    elif (front1 < 0.2 or front2 < 0.2) and left < 0.2 and right < 0.2:
        msg1.linear.x = 0
        msg1.angular.z = -0.6
        pub.publish(msg1)
        print('Obstalce Detected')

rospy.spin()

