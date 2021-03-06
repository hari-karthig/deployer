#!/usr/bin/env python

import os

elb_name = os.popen("aws elb describe-load-balancers --region us-west-2 --query LoadBalancerDescriptions[].LoadBalancerName --output text").read()
elb_sg = os.popen("aws elb describe-load-balancers --region us-west-2 --query LoadBalancerDescriptions[].SecurityGroups --output text").read()

delete_elb = os.system("aws elb delete-load-balancer --region us-west-2 --load-balancer-name %s" %elb_name)
if delete_elb == 0:
    print("# Successfully deleted ELB - %s" %elb_name)
    print("===============================================================================================================================================================")
    print("# Please delete ELB SG %s through console. When VPC started to destroy" %elb_sg)
    print("# This will be deprecated in future release")
    print("===============================================================================================================================================================")
else:
    print("# Failed to delete the ELB - %s" %elb_name)
