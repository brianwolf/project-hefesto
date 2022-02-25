runpipeline rp:	
	python app.py examples/pipeline_ejemplo.yaml

	
runtemplate rt:
	python app.py examples/template_ejemplo.yaml -p texto=hola,nombre_archivo=asd


compile c:
	rm -fr build dist *.spec
	
	pyinstaller app.py \
		--onefile \
		--add-data variables.yaml:. \
		--add-data repo_modules:repo_modules \
		-n hefesto
	
	mv dist/* .
	rm -fr build dist *.spec