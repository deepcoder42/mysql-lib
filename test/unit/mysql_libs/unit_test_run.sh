#!/bin/bash
# Unit testing program for the module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo "Unit test: mysql_libs"  
test/unit/mysql_libs/_io_wait_chk.py
test/unit/mysql_libs/_sql_wait_chk.py
test/unit/mysql_libs/analyze_tbl.py
test/unit/mysql_libs/change_master_to.py
test/unit/mysql_libs/checksum.py
test/unit/mysql_libs/check_tbl.py
test/unit/mysql_libs/chg_slv_state.py
test/unit/mysql_libs/create_instance.py
test/unit/mysql_libs/disconnect.py
test/unit/mysql_libs/fetch_db_dict.py
test/unit/mysql_libs/fetch_logs.py
test/unit/mysql_libs/fetch_tbl_dict.py
test/unit/mysql_libs/optimize_tbl.py
test/unit/mysql_libs/purge_bin_logs.py
test/unit/mysql_libs/reset_master.py
test/unit/mysql_libs/reset_slave.py
test/unit/mysql_libs/select_wait_until.py
test/unit/mysql_libs/create_slv_array.py
test/unit/mysql_libs/crt_cmd.py
test/unit/mysql_libs/crt_srv_inst.py
test/unit/mysql_libs/fetch_slv.py
test/unit/mysql_libs/find_name.py
test/unit/mysql_libs/is_cfg_valid.py
test/unit/mysql_libs/is_logs_synced.py
test/unit/mysql_libs/is_rep_delay.py
test/unit/mysql_libs/start_slave_until.py
test/unit/mysql_libs/switch_to_master.py
test/unit/mysql_libs/sync_delay.py
test/unit/mysql_libs/sync_rep_slv.py
test/unit/mysql_libs/wait_until.py

