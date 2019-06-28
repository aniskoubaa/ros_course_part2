#!/usr/bin/env python  
import roslib
import rospy
import tf
import time  
import math
import time
#!/usr/bin/env python  
import roslib
import rospy
import tf
import time  
import math
import time

if __name__ == '__main__':
    #init the node
    rospy.init_node('turtle_tf_broadcaster')
    
    time.sleep(2)
    transform_broadcaster = tf.TransformBroadcaster()
    
    while(not rospy.is_shutdown()):
        
        
        #convert 90 degrees to quaternion
        rotation_quaternion = tf.transformations.quaternion_from_euler(0, 0, math.radians(90))

        #translation vector
        translation_vector = (1.2, 1.3, 0)

        #time
        current_time = rospy.Time.now()

        transform_broadcaster.sendTransform(translation_vector, 
            rotation_quaternion,
            current_time, 
            "robot_frame", "world")
        time.sleep(0.5)

    rospy.spin()

    
if __name__ == '__main__':
	#init the node
    rospy.init_node('turtle_tf_broadcaster')
    
    time.sleep(2)

    while(True):
        transform_broadcaster = tf.TransformBroadcaster()
        
        #convert 90 degrees to quaternion
        rotation_quaternion = tf.transformations.quaternion_from_euler(0, 0, math.radians(90))

        #translation vector
        translation_vector = (1.2, 1.3, 0)

        #time
        current_time = rospy.Time.now()

        transform_broadcaster.sendTransform(translation_vector, 
            rotation_quaternion,
            current_time, 
            "robot_frame", "world")
        time.sleep(0.5)

    rospy.spin()

    