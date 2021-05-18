#!/bin/bash
# Integration test code coverage for module.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=mysql_libs test/integration/mysql_libs/create_instance.py
coverage run -a --source=mysql_libs test/integration/mysql_libs/crt_srv_inst.py
coverage run -a --source=mysql_libs test/integration/mysql_libs/fetch_db_dict.py
coverage run -a --source=mysql_libs test/integration/mysql_libs/fetch_logs.py
coverage run -a --source=mysql_libs test/integration/mysql_libs/fetch_tbl_dict.py
coverage run -a --source=mysql_libs test/integration/mysql_libs/is_cfg_valid.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
 
