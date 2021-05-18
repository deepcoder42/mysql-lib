#!/bin/bash
# Integration testing program for the module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo "Integration test: mysql_libs"  
test/integration/mysql_libs/create_instance.py
test/integration/mysql_libs/crt_srv_inst.py
test/integration/mysql_libs/fetch_db_dict.py
test/integration/mysql_libs/fetch_logs.py
test/integration/mysql_libs/fetch_tbl_dict.py
test/integration/mysql_libs/is_cfg_valid.py
