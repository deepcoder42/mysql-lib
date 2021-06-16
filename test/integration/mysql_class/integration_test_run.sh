#!/bin/bash
# Integration testing program for the module.
# This will run all the integration tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo "Unit test: mysql_class"  
test/integration/mysql_class/fetch_global_var.py
test/integration/mysql_class/fetch_sys_var.py
test/integration/mysql_class/server_chg_db.py
test/integration/mysql_class/server_cmd_sql.py
test/integration/mysql_class/server_col_sql.py
test/integration/mysql_class/server_connect.py
test/integration/mysql_class/server_disconnect.py
test/integration/mysql_class/server_get_name.py
test/integration/mysql_class/server_init.py
test/integration/mysql_class/server_is_connected.py
test/integration/mysql_class/server_reconnect.py
test/integration/mysql_class/server_set_pass_config.py
test/integration/mysql_class/server_set_srv_binlog_crc.py
test/integration/mysql_class/server_set_srv_gtid.py
test/integration/mysql_class/server_setup_ssl.py
test/integration/mysql_class/server_sql.py
test/integration/mysql_class/server_upd_srv_perf.py
test/integration/mysql_class/server_upd_srv_stat.py
test/integration/mysql_class/server_vert_sql.py

