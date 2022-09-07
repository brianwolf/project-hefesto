compile c:
	rm -fr build dist *.spec
	
	pyinstaller app.py \
		--onefile \
		--add-data logic/apps/repo_modules/:logic/apps/repo_modules/ \
		-n hefesto
	
	mv dist/* .
	rm -fr build dist *.spec
		