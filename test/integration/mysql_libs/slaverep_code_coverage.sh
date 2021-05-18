#!/bin/bash
# Integration test code coverage for module.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=mysql_libs test/integration/mysql_libs/chg_slv_state.py
coverage run -a --source=mysql_libs test/integration/mysql_libs/create_slv_array.py
coverage run -a --source=mysql_libs test/integration/mysql_libs/fetch_slv.py
coverage run -a --source=mysql_libs test/integration/mysql_libs/find_name.py
coverage run -a --source=mysql_libs test/integration/mysql_libs/slaverep_create_instance.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
 
