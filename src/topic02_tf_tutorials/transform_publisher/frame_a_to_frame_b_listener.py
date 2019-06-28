#!/usr/bin/env python  
import rospy
import math
import tf
import geometry_msgs.msg
import turtlesim.srv

if __name__ == '__main__':
    rospy.init_node('frame_a_frame_b_listener_node')

    listener = tf.TransformListener()
    rate = rospy.Rate(1.0)
    listener.waitForTransform('/frame_a', '/frame_b', rospy.Time(), rospy.Duration(4.0))
    
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/frame_a', '/frame_b', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        quaternion = rot
        rpy=tf.transformations.euler_from_quaternion(quaternion)
        print 'transformation between frame_a and frame_b detected'
        print 'translation vector: (',trans[0],',',trans[1],',',trans[2],')'
        print 'rotation angles: roll=',rpy[0],' pitch=',rpy[1],' yaw=',rpy[2]


        rate.sleep()