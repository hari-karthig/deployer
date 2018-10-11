#!/usr/bin/env python

import os

elb_name = os.popen("aws elb describe-load-balancers --region us-west-2 --query LoadBalancerDescriptions[].LoadBalancerName --output text").read()
elb_sg = os.popen("aws elb describe-load-balancers --region us-west-2 --query LoadBalancerDescriptions[].SecurityGroups --output text").read()

print("===============================================================================================================================================================")
print("#                                                            STARTED DELETING ENVIRONMENT                                                                     #")
print("===============================================================================================================================================================")
print("# Deleting ELB - %s" %elb_name)

delete_elb = os.system("aws elb delete-load-balancer --region us-west-2 --load-balancer-name %s" %elb_name)
if delete_elb == 0:
    print("# Successfully deleted ELB - %s" %elb_name)
#    delete_sg = os.system("aws ec2 delete-security-group --region us-west-2 --group-id %s" %elb_sg)
#    if delete_sg == 0:
#        print("# Successfully deleted ELB SG - %s" %elb_sg)
#        print("===============================================================================================================================================================")
#    else:
#        print("# Failed to delete the ELB SG - %s" %elb_sg)
#        print("===============================================================================================================================================================")
else:
    print("# Failed to delete the ELB - %s" %elb_name)
    print("===============================================================================================================================================================")
