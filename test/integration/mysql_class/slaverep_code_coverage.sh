#!/bin/bash
# Integration test code coverage for module.
# This will run the Python code coverage module against all integration test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=mysql_class test/integration/mysql_class/fetch_global_var.py
coverage run -a --source=mysql_class test/integration/mysql_class/fetch_sys_var.py
coverage run -a --source=mysql_class test/integration/mysql_class/flush_logs.py
coverage run -a --source=mysql_class test/integration/mysql_class/gtidset.py
coverage run -a --source=mysql_class test/integration/mysql_class/masterrep_connect.py
coverage run -a --source=mysql_class test/integration/mysql_class/masterrep_init.py
coverage run -a --source=mysql_class test/integration/mysql_class/masterrep_get_log_info.py
coverage run -a --source=mysql_class test/integration/mysql_class/masterrep_show_slv_hosts.py
coverage run -a --source=mysql_class test/integration/mysql_class/masterrep_upd_mst_status.py
coverage run -a --source=mysql_class test/integration/mysql_class/rep_fetch_do_db.py
coverage run -a --source=mysql_class test/integration/mysql_class/rep_fetch_ign_db.py
coverage run -a --source=mysql_class test/integration/mysql_class/rep_get_serv_id.py
coverage run -a --source=mysql_class test/integration/mysql_class/rep_init.py
coverage run -a --source=mysql_class test/integration/mysql_class/server_chg_db.py
coverage run -a --source=mysql_class test/integration/mysql_class/server_cmd_sql.py
coverage run -a --source=mysql_class test/integration/mysql_class/server_col_sql.py
coverage run -a --source=mysql_class test/integration/mysql_class/server_connect.py
coverage run -a --source=mysql_class test/integration/mysql_class/server_disconnect.py
coverage run -a --source=mysql_class test/integration/mysql_class/server_fetch_log.py
coverage run -a --source=mysql_class test/integration/mysql_class/server_fetch_mst_rep_cfg.py
coverage run -a --source=mysql_class test/integration/mysql_class/server_flush_logs.py
coverage run -a --source=mysql_class test/integration/mysql_class/server_get_name.py
coverage run -a --source=mysql_class test/integration/mysql_class/server_init.py
coverage run -a --source=mysql_class test/integration/mysql_class/server_is_connected.py
coverage run -a --source=mysql_class test/integration/mysql_class/server_reconnect.py
coverage run -a --source=mysql_class test/integration/mysql_class/server_set_srv_binlog_crc.py
coverage run -a --source=mysql_class test/integration/mysql_class/server_set_srv_gtid.py
coverage run -a --source=mysql_class test/integration/mysql_class/server_sql.py
coverage run -a --source=mysql_class test/integration/mysql_class/server_upd_log_stats.py
coverage run -a --source=mysql_class test/integration/mysql_class/server_upd_mst_rep_stat.py
coverage run -a --source=mysql_class test/integration/mysql_class/server_upd_srv_perf.py
coverage run -a --source=mysql_class test/integration/mysql_class/server_upd_srv_stat.py
coverage run -a --source=mysql_class test/integration/mysql_class/server_vert_sql.py
coverage run -a --source=mysql_class test/integration/mysql_class/show_master_stat.py
coverage run -a --source=mysql_class test/integration/mysql_class/show_slave_hosts.py
coverage run -a --source=mysql_class test/integration/mysql_class/show_slave_stat.py
coverage run -a --source=mysql_class test/integration/mysql_class/slave_start.py
coverage run -a --source=mysql_class test/integration/mysql_class/slave_stop.py
coverage run -a --source=mysql_class test/integration/mysql_class/slaverep_connect.py
coverage run -a --source=mysql_class test/integration/mysql_class/slaverep_fetch_do_tbl.py
coverage run -a --source=mysql_class test/integration/mysql_class/slaverep_fetch_ign_tbl.py
coverage run -a --source=mysql_class test/integration/mysql_class/slaverep_get_err_stat.py
coverage run -a --source=mysql_class test/integration/mysql_class/slaverep_get_log_info.py
coverage run -a --source=mysql_class test/integration/mysql_class/slaverep_get_others.py
coverage run -a --source=mysql_class test/integration/mysql_class/slaverep_get_thr_stat.py
coverage run -a --source=mysql_class test/integration/mysql_class/slaverep_get_time.py
coverage run -a --source=mysql_class test/integration/mysql_class/slaverep_init.py
coverage run -a --source=mysql_class test/integration/mysql_class/slaverep_is_slave_up.py
coverage run -a --source=mysql_class test/integration/mysql_class/slaverep_is_slv_error.py
coverage run -a --source=mysql_class test/integration/mysql_class/slaverep_is_slv_running.py
coverage run -a --source=mysql_class test/integration/mysql_class/slaverep_show_slv_state.py
coverage run -a --source=mysql_class test/integration/mysql_class/slaverep_start_slave.py
coverage run -a --source=mysql_class test/integration/mysql_class/slaverep_stop_slave.py
coverage run -a --source=mysql_class test/integration/mysql_class/slaverep_upd_gtid_pos.py
coverage run -a --source=mysql_class test/integration/mysql_class/slaverep_upd_slv_state.py
coverage run -a --source=mysql_class test/integration/mysql_class/slaverep_upd_slv_status.py
coverage run -a --source=mysql_class test/integration/mysql_class/slaverep_upd_slv_time.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
 
