# Deployer

Luna Deployer is an automated module to deploy lunatech applications. Which is running on EKS and deploying the modules through Jenkins.

# Prerequisite

- [terraform](https://releases.hashicorp.com/terraform/0.11.8/terraform_0.11.8_linux_amd64.zip)
- [aws-iam-authenticator](https://amazon-eks.s3-us-west-2.amazonaws.com/1.10.3/2018-07-26/bin/linux/amd64/aws-iam-authenticator)
- [kubectl](https://storage.googleapis.com/kubernetes-release/release/v1.12.0/bin/linux/amd64/kubectl)
- python 2.7 or above
- docker

Addition to above you'll have to configure aws credentials

# Execution

`git clone https://github.com/hari-karthig/lunatech.git`

`make airports`

This will build airports application from luna-apps/airports/Dockerfile and it'll run as a container locally. Service exposed via host port 8085.
(Please allow port 8085 in your firewalls or change the port in Makefile under airports option as per need)

`make countries`
 
This will build countries application from luna-apps/countries/Dockerfile and it'll run as a container locally. Service exposed via host port 8090.
(Please allow port 8090 in your firewalls or change the port in Makefile under countries option as per need)

`make clean`

This will clean the local containers

`make deploy`

This will create an EKS cluster for you from terraform-eks module with addons mentioned in the kube-addons by executing bin/create_addons.py

Also, addons will create an ELB which has minions in backend

Get the ingresses which are created and add corresponding R53 records for them

Once those are propagated you should be able access Jenkins UI

`make destroy`

This will destroy the EKS cluster

# Known Issues

- ELB's SG won't be destroyed by `make destroy`. You've to delete it through AWS console once VPC started destroying
- Not able to view Jenkins login page
- Route53 entries should be added/updated through AWS console
