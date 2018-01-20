.PHONY: clean
clean:
	find . \( -name \*.pyc -o -name \*.pyo -o -name __pycache__ \) -prune -exec rm -rf {} +
	rm -rf build/
	rm -rf dist/
	rm -rf pangu.egg-info/

debug:
	python setup.py develop

publish:
	python setup.py publish
