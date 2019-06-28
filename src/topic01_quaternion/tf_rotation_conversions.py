#!/usr/bin/env python

#this script converts between Roll-Pitch-Yaw angles and Quaternions

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math
import tf

print('-----------------------------------------')
print('Roll-Pitch-Yaw Conversion to Quaternions')
print('-----------------------------------------')
#we define some random angles roll, pitch and yaw in radians
roll = math.radians(30)
pitch = math.radians(42)
yaw = math.radians(58)

#we print these three angles
print 'roll = ', math.degrees(roll), 'pitch = ', math.degrees(pitch),'yaw = ', math.degrees(yaw)

#convert the roll-pitch-yaw angles to a quaternion using ROS TF Library
quaternion = tf.transformations.quaternion_from_euler(roll, pitch, yaw)
print('-----------------------------------------')
print 'The resulting quaternion using "quaternion_from_euler" function: '
for i in range(4):
	print quaternion[i]


#quaternion[0] = -3.88256895463e-06
#quaternion[1] = 0.0015896463485
#quaternion[2] = 0.001397167245
#quaternion[3] = 0.999997760464

#perform the opposite converion
rpy = tf.transformations.euler_from_quaternion(quaternion)
roll_from_quaternion = rpy[0]
pitch_from_quaternion = rpy[1]
yaw_from_quaternion = rpy[2]

print('-----------------------------------------')
print 'convert back to roll-pitch-yaw using "euler_from_quaternion" function: '
print 'roll = ', math.degrees(roll_from_quaternion), 'pitch = ', math.degrees(pitch_from_quaternion),'yaw = ', math.degrees(yaw_from_quaternion)
print('we get the same initial roll-picth-roll values')
print('-----------------------------------------')
#define a new quaternion
print('define a new quaternion manually as a list')
q=(-3.88256895463e-06, 0.0015896463485, 0.001397167245, 0.0)

#perform the opposite converion
rpy = tf.transformations.euler_from_quaternion(q)
roll_from_quaternion = rpy[0]
pitch_from_quaternion = rpy[1]
yaw_from_quaternion = rpy[2]
print('-----------------------------------------')
print 'convert back to roll-pitch-yaw using "euler_from_quaternion" function: '
print 'roll = ', math.degrees(roll_from_quaternion), 'pitch = ', math.degrees(pitch_from_quaternion),'yaw = ', math.degrees(yaw_from_quaternion)
print('-----------------------------------------')
print('you can change these values in the file to make other converions')


