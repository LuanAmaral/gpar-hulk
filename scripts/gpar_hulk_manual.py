#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

KEYCODE_RIGHT = 0x43
KEYCODE_LEFT = 0x44
KEYCODE_UP = 0x41
KEYCODE_DOWN = 0x42
KEYCODE_SPACE = 0x20

def Move():
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel = Twist()

    vel.linear.x = 0
    vel.linear.y = 0
    vel.linear.z = 0

    vel.angular.x = 0
    vel.angular.y = 0
    vel.angular.z = 0

    while not rospy.is_shutdown()
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break

            if k=='\x1b[A':
                    print "up"
                    vel.linear.x  =  0.2;
                    vel.angular.z =  0.0;

            elif k=='\x1b[B':
                    print "down"
                    vel.linear.x  = -0.2;
                    vel.angular.z =  0.0;

            elif k=='\x1b[C':
                    print "right"
                    vel.linear.x  =  0.0;
                    vel.angular.z =  0.2;

            elif k=='\x1b[D':
                    print "left"
                    vel.linear.x  =  0.0;
                    vel.angular.z = -0.2;
            else:
                    print "not an arrow key!"

            velocity_publisher.publish(vel)
            rospy.loginfo(vel)
            
