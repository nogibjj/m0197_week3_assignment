install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=src test_*.py

format:	
	black *.py 

lint:
	#disable comment to test speed
	#pylint --disable=R,C --ignore-patterns=test_.*?py *.py src/*.py
	#ruff linting is 10-100X faster than pylint
	ruff check *.py src/*.py

run: 
	python3 plots.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint
		
all: install lint test format run
