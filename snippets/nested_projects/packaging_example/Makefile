

# steps towards pushing a package to testpypi

step1_install_required_python_packages:
	python3 -m pip install --upgrade build twine

step2_build_packages:
	python3 -m build


step3_uplaod_to_testpypi:
	twine upload --repository testpypi dist/*
