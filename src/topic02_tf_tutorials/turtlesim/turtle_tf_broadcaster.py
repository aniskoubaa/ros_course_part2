#!/usr/bin/env python  
import roslib
import rospy
import tf
import turtlesim.msg
from turtlesim.msg import Pose

def pose_callback(msg, turtlename):
	#create a transform broadcaster
    transform_broadcaster = tf.TransformBroadcaster()
    #convert 90 degrees to quaternion
    rotation_quaternion = tf.transformations.quaternion_from_euler(0, 0, msg.theta)
    #translation vector
    translation_vector = (msg.x, msg.y, 0)
    #time
    current_time = rospy.Time.now()

    transform_broadcaster.sendTransform(translation_vector, rotation_quaternion,
        current_time, turtlename+"_frame", "world")




if __name__ == '__main__':
	#init the node
    rospy.init_node('turtle_tf_broadcaster')
    #get the parameter of the turtle name 
    turtlename = rospy.get_param('~turtle')
    #subscribe to the Pose topic
    rospy.Subscriber('/%s/pose' % turtlename, Pose, pose_callback, turtlename)
    rospy.spin()