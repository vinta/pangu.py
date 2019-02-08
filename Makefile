.PHONY: clean test debug pack publish

clean:
	find . \( -name \*.pyc -o -name \*.pyo -o -name __pycache__ \) -prune -exec rm -rf {} +
	rm -rf build/
	rm -rf dist/
	rm -rf pangu.egg-info/

test: clean
	python setup.py test

debug: clean
	pip install --editable .

pack: clean
	pip install wheel -U
	python setup.py bdist_wheel sdist

publish: pack
	pip install twine -U
	twine upload dist/*
