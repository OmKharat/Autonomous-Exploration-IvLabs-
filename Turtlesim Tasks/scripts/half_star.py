#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('half_star')

pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

rate = rospy.Rate(2)

while not rospy.is_shutdown():
    msg = Twist()