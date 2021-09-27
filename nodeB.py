
#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
q=0.15
def callback(data):
    data.data=(data.data)/q
    rospy.loginfo(rospy.get_caller_id() + "I received %d", data.data)
    
def NodeB():

    # run simultaneously.
    rospy.init_node('NodeB', anonymous=True)

    rospy.Subscriber("gore", Float32, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    NodeB()