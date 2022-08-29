#!/usr/bin/env python
import rospy
from nav_msgs.srv import GetMap, GetMapRequest
import sys

rospy.init_node("map_service_client")  # Initialise the node
rospy.wait_for_service("/static_map")  # Wait for service
try:
    # Create the connection to the service (client)
    client = rospy.ServiceProxy("/static_map", GetMap)
    get_map_msg = GetMapRequest()
    service_response = client(get_map_msg)
    # print(service_response)
    if service_response:
        print("SUCCESS!!")

except rospy.ServiceException as error:
    print("Service call failed: %s" % error)
