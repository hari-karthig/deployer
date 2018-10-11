PYTHON = python
AIRPORT_VERSOIN = 1.0.1
COUNTRIES_VERSION = 1.0.1

.PHONY: help airports countries clean deploy destroy

help:
	@echo "========================================="
	@echo "# 	HELP make <target>	       #"
	@echo "========================================="
	@echo "#  airports       Exec airports app   	"
	@echo "#  countries      Exec countries app  	"
	@echo "#  clean          Remove app containers  "
	@echo "#  deploy         Deploy EKS             "
	@echo "#  destroy        Destroy EKS            "
	@echo "========================================="
