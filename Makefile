PIPELINE ?= pipeline_ejemplo.json
ZIP ?= project.zip
TEMPLATE ?= template_ejemplo.json
PARAMS ?= parametros_ejemplo.json

run r:	
	python ./exec_pipeline.py -p examples/${PIPELINE} -z ${ZIP}

	
run-template t:
	python ./exec_template.py -p examples/${PARAMS} -z ${ZIP} -t examples/${TEMPLATE}
