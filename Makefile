.PHONY: clean
clean:
	find . \( -name \*.pyc -o -name \*.pyo -o -name __pycache__ \) -prune -exec rm -rf {} +
	rm -rf build/
	rm -rf dist/
	rm -rf pangu.egg-info/

debug:
	pip install --editable .

pkg: clean
	pip install wheel -U
	python setup.py bdist_wheel sdist

publish: pkg
	pip install twine -U
	twine upload dist/*
