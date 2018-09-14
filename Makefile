init:
	virtualenv env
	pip install -r requirements.txt

venv:
	source env/bin/activate

test:
	nosetests tests
