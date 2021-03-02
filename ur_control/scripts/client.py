#!/usr/bin/env python

#from server_ur10.srv import *
import rospy
from std_msgs.msg import String
from std_msgs.msg import Bool
import socket
import netifaces as ni
from std_srvs.srv import *
from ur_control.srv import *
def main():
    rospy.wait_for_service('/rg2_gripper/control_width')
    # global target_width
    try:
        val=rospy.ServiceProxy('/rg2_gripper/control_width', RG2)
        request=RG2Request()
        request.target_width.data=100.0

        resp1=val(request)
        
    except rospy.ServiceException, e:
        print e

if __name__ == "__main__":
    #target_width=110.0
    main()