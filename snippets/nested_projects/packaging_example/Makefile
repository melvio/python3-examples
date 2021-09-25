

# steps towards pushing a package to testpypi

step1_install_required_python_packages:
	python3 -m pip install --upgrade build twine

step2_build_packages:
	python3 -m build


step3_upload_to_testpypi:
	twine upload --repository testpypi dist/*


# installing the pushed package
step4_install_package:
	python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-pkg-YOUR-melvio

# run the code from the installed package
step5_run_python:
	python3 -c 'from example_package import example ; example.medical_knowledge()'

