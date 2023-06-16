package p:
	rm -fr build dist *.spec
	
	pyinstaller app.py \
		--onefile \
		--add-data logic/apps/repo_modules/:logic/apps/repo_modules/ \
		-n hefesto
	
	mv dist/* .
	rm -fr build dist *.spec
		

install i: p
	sudo mv hefesto /usr/local/bin/ 