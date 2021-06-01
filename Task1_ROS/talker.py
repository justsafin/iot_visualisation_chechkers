#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def talker():
    pub = rospy.Publisher('chatter', Int32, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(3) # 10hz
    i = 0
    while not rospy.is_shutdown():
        i +=1
#        rospy.loginfo(i)
        pub.publish(i)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
