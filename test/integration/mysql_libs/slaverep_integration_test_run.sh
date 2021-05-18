#!/bin/bash
# Integration testing program for the module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo "Integration test: mysql_libs"  
test/integration/mysql_libs/chg_slv_state.py
test/integration/mysql_libs/create_slv_array.py
test/integration/mysql_libs/fetch_slv.py
test/integration/mysql_libs/find_name.py
test/integration/mysql_libs/slaverep_create_instance.py
