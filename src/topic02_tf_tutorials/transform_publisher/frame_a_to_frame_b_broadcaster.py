#!/usr/bin/env python  
import roslib
import rospy
import tf
import time  
import math
import time

if __name__ == '__main__':
	#init the node
    rospy.init_node('frame_a_frame_b_broadcaster_node')
    
    time.sleep(2)
    #create a transformation broadcaster (publisher)
    transform_broadcaster = tf.TransformBroadcaster()

    while(not rospy.is_shutdown()):

        #create a quaternion
        rotation_quaternion = tf.transformations.quaternion_from_euler(0.2, 0.3, 0.1)

        #translation vector
        translation_vector = (1.0, 2.0, 3.0)

        #time
        current_time = rospy.Time.now()

        transform_broadcaster.sendTransform(
            translation_vector, 
            rotation_quaternion,
            current_time, 
            "frame_b", "frame_a") #child frame, parent frame
        time.sleep(0.5)

    rospy.spin()

    