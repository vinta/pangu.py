clean:
	find . -name '*.pyc' -delete
	find . -name '*.py~' -delete
	find . -name '*.pyo' -delete

publish:
	python setup.py sdist bdist_wheel upload