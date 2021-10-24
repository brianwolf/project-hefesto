ZIP ?= project.zip

run r:	
	python exec_pipeline.py -p ${PIPELINE} -z ${ZIP}

	
run-template t:
	python exec_template.py -p ${PARAMS} -z ${ZIP} -t ${TEMPLATE}
