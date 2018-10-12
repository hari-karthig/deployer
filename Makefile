SHELL := /bin/bash

.PHONY: help

help:
	@echo "========================================="
	@echo "# 	HELP make <target>	       #"
	@echo "========================================="
	@echo "#  airports       Exec airports app   	"
	@echo "#  countries      Exec countries app  	"
	@echo "#  clean          Remove local containers  "
	@echo "#  deploy         Deploy EKS             "
	@echo "#  destroy        Destroy EKS             "
	@echo "========================================="

airports:
	bash -c "sudo docker build -t airports luna-apps/airports/"
	bash -c "sudo docker run -d -p 8085:8080 airports"

countries:
	bash -c "sudo docker build -t countries luna-apps/countries/"
	bash -c "sudo docker run -d -p 8090:8080 countries"

clean:
	bash -c "sudo docker rm -f $(shell sudo docker ps -a -q)"

deploy:
	bash -c "cd terraform-eks && terraform plan"
#	bash -c "aws eks update-kubeconfig --name lunatech --region us-west-2"
#	bash -c "kubectl create -f terraform-eks/cm.yml"
	@echo "==============================================================================================================================================================="
	@echo "# 			                                        CLUSTER IS INITIATING........					                             #"
	@echo "==============================================================================================================================================================="
	bash -c "# PLease wait for a minute ........"
	bash -c "sleep 60"
	bash -c "python bin/create_addons.py"
	@echo "==============================================================================================================================================================="
	@echo "# 			                                    CLUSTER HAS INITIATED SUCCESSFULLY		                                                     #"
	@echo "==============================================================================================================================================================="

destroy:
	bash -c "python bin/destroy_elb.py"
	bash -c "cd terraform-eks && terraform destroy --auto-approve"
	@echo "==============================================================================================================================================================="
	@echo "# 			                                    CLUSTER HAS DESTROYED SUCCESSFULLY		                                                     #"
	@echo "==============================================================================================================================================================="
