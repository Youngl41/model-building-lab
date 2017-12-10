=================================================================
PEP8 Coding
=================================================================
module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, function_parameter_name, local_var_name



=================================================================
Uploading to TestPyPI
=================================================================
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

=================================================================
Installing from TestPyPI
=================================================================
pip install --index-url https://test.pypi.org/simple/ model-building-lab --upgrade