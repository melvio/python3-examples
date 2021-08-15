SHELL=/bin/bash

create_venv:
	python3 -m venv venv  \
	echo "run: source ./venv/bin/active to active this virtual environment"

install_requirements:
	@if [[ -n "${VIRTUAL_ENV}" ]] ; then\
		python3 -m pip install -r requirements.txt;\
	else\
		echo "virtual env not active: use 'source ./venv/bin/activate'";\
	fi\




