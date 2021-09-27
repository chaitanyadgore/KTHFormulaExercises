#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float32


def NodeA():
    pub = rospy.Publisher('gore', Float32, queue_size=20)
    rospy.init_node('NodeA', anonymous=True)
    rate = rospy.Rate(20) # 20hz
    n=10000000
    i=0
    k=0
    for i in range(n):
        
        send= k
        print(send)
        k= k+4
        rospy.loginfo(send)
        pub.publish(send)
        rate.sleep()
    
    

if __name__ == '__main__':
    try:
        NodeA()
    except rospy.ROSInterruptException:
        pass