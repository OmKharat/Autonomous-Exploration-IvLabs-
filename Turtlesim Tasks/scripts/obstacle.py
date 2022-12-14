#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


global right, left, front1, front2

right = 0
left = 0
front1 = 0
front2 = 0

def region(msg):
    global right, left, front1, front2

    right = min(min(msg.ranges[300:340]), 10)                       #msg.ranges[0]       
    front1 = min(min(msg.ranges[0:20]), 10)
    front2 = min(min(msg.ranges[340:359]), 10)                          #msg.ranges[30]      
    left  = min(min(msg.ranges[20:60]), 10)                         #msg.ranges[330]     
    

rospy.init_node('obstacle_avoidance',anonymous=True)
sub = rospy.Subscriber('/scan', LaserScan, region)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

msg1 = Twist()
pub.publish(msg1)

while not rospy.is_shutdown():
    if (front1 > 0.4 or front2 > 0.4) and left > 0.4 and right > 0.4:
        msg1.linear.x = 0.5
        msg1.angular.z = 0
        pub.publish(msg1)
    elif (front1 > 0.4 or front2 > 0.4) and left > 0.4 and right < 0.4:
        msg1.linear.x = 0
        msg1.angular.z = 0.6
        pub.publish(msg1)
    elif (front1 > 0.4 or front2 > 0.4) and left < 0.4 and right > 0.4:
        msg1.linear.x = 0
        msg1.angular.z = -0.6
        pub.publish(msg1)
    elif (front1 < 0.4 or front2 > 0.4) and left > 0.4 and right > 0.4:
        msg1.linear.x = 0
        msg1.angular.z = -0.6
        pub.publish(msg1)
    elif (front1 > 0.4 or front2 < 0.4) and left > 0.4 and right > 0.4:
        msg1.linear.x = 0
        msg1.angular.z = 0.6
        pub.publish(msg1)
    elif (front1 < 0.4 or front2 < 0.4) and left > 0.4 and right < 0.4:
        msg1.linear.x = 0
        msg1.angular.z = 0.6
        pub.publish(msg1)
    elif (front1 < 0.4 or front2 < 0.4) and left < 0.4 and right > 0.4:
        msg1.linear.x = 0
        msg1.angular.z = -0.6
        pub.publish(msg1)
    elif (front1 > 0.4 or front2 > 0.4) and left < 0.4 and right < 0.4:
        msg1.linear.x = 0.5
        msg1.angular.z = 0
        pub.publish(msg1)
    elif (front1 < 0.4 or front2 < 0.4) and left < 0.4 and right < 0.4:
        msg1.linear.x = 0
        msg1.angular.z = -0.6
        pub.publish(msg1)

rospy.spin()

