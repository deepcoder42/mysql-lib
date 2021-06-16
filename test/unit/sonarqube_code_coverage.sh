#!/bin/bash
# Unit test code coverage for SonarQube to cover all library modules.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=mysql_class test/unit/mysql_class/fetch_global_var.py
coverage run -a --source=mysql_class test/unit/mysql_class/fetch_sys_var.py
coverage run -a --source=mysql_class test/unit/mysql_class/flush_logs.py
coverage run -a --source=mysql_class test/unit/mysql_class/show_master_stat.py
coverage run -a --source=mysql_class test/unit/mysql_class/show_slave_hosts.py
coverage run -a --source=mysql_class test/unit/mysql_class/show_slave_stat.py
coverage run -a --source=mysql_class test/unit/mysql_class/slave_start.py
coverage run -a --source=mysql_class test/unit/mysql_class/slave_stop.py
coverage run -a --source=mysql_class test/unit/mysql_class/gtidset_or.py
coverage run -a --source=mysql_class test/unit/mysql_class/gtidset_init.py
coverage run -a --source=mysql_class test/unit/mysql_class/gtidset_str.py
coverage run -a --source=mysql_class test/unit/mysql_class/gtidset_union.py
coverage run -a --source=mysql_class test/unit/mysql_class/gtidset_eq.py
coverage run -a --source=mysql_class test/unit/mysql_class/gtidset_ge.py
coverage run -a --source=mysql_class test/unit/mysql_class/gtidset_gt.py
coverage run -a --source=mysql_class test/unit/mysql_class/gtidset_le.py
coverage run -a --source=mysql_class test/unit/mysql_class/gtidset_lt.py
coverage run -a --source=mysql_class test/unit/mysql_class/gtidset_ne.py
coverage run -a --source=mysql_class test/unit/mysql_class/masterrep_connect.py
coverage run -a --source=mysql_class test/unit/mysql_class/masterrep_init.py
coverage run -a --source=mysql_class test/unit/mysql_class/masterrep_showslvhosts.py
coverage run -a --source=mysql_class test/unit/mysql_class/masterrep_getloginfo.py
coverage run -a --source=mysql_class test/unit/mysql_class/masterrep_updmststatus.py
coverage run -a --source=mysql_class test/unit/mysql_class/position_cmp.py
coverage run -a --source=mysql_class test/unit/mysql_class/rep_fetchdodb.py
coverage run -a --source=mysql_class test/unit/mysql_class/rep_fetchigndb.py
coverage run -a --source=mysql_class test/unit/mysql_class/rep_getservid.py
coverage run -a --source=mysql_class test/unit/mysql_class/rep_init.py
coverage run -a --source=mysql_class test/unit/mysql_class/rep_showslvhosts.py
coverage run -a --source=mysql_class test/unit/mysql_class/rep_showslvstate.py
coverage run -a --source=mysql_class test/unit/mysql_class/rep_startslave.py
coverage run -a --source=mysql_class test/unit/mysql_class/rep_stopslave.py
coverage run -a --source=mysql_class test/unit/mysql_class/server_chg_db.py
coverage run -a --source=mysql_class test/unit/mysql_class/server_connect.py
coverage run -a --source=mysql_class test/unit/mysql_class/server_disconnect.py
coverage run -a --source=mysql_class test/unit/mysql_class/server_fetchlogs.py
coverage run -a --source=mysql_class test/unit/mysql_class/server_fetchmstrepcfg.py
coverage run -a --source=mysql_class test/unit/mysql_class/server_fetchslvrepcfg.py
coverage run -a --source=mysql_class test/unit/mysql_class/server_flushlogs.py
coverage run -a --source=mysql_class test/unit/mysql_class/server_getname.py
coverage run -a --source=mysql_class test/unit/mysql_class/server_init.py
coverage run -a --source=mysql_class test/unit/mysql_class/server_is_connected.py
coverage run -a --source=mysql_class test/unit/mysql_class/server_reconnect.py
coverage run -a --source=mysql_class test/unit/mysql_class/server_set_pass_config.py
coverage run -a --source=mysql_class test/unit/mysql_class/server_set_ssl_config.py
coverage run -a --source=mysql_class test/unit/mysql_class/server_setsrvbinlogcrc.py
coverage run -a --source=mysql_class test/unit/mysql_class/server_setsrvgtid.py
coverage run -a --source=mysql_class test/unit/mysql_class/server_setup_ssl.py
coverage run -a --source=mysql_class test/unit/mysql_class/server_updlogstats.py
coverage run -a --source=mysql_class test/unit/mysql_class/server_updmstrepstat.py
coverage run -a --source=mysql_class test/unit/mysql_class/server_updsrvperf.py
coverage run -a --source=mysql_class test/unit/mysql_class/server_updslvrepstat.py
coverage run -a --source=mysql_class test/unit/mysql_class/server_updsrvstat.py
coverage run -a --source=mysql_class test/unit/mysql_class/server_vertsql.py
coverage run -a --source=mysql_class test/unit/mysql_class/slaverep_connect.py
coverage run -a --source=mysql_class test/unit/mysql_class/slaverep_init.py
coverage run -a --source=mysql_class test/unit/mysql_class/slaverep_fetchdotbl.py
coverage run -a --source=mysql_class test/unit/mysql_class/slaverep_fetchigntbl.py
coverage run -a --source=mysql_class test/unit/mysql_class/slaverep_updslvstatus.py
coverage run -a --source=mysql_class test/unit/mysql_class/slaverep_geterrstat.py
coverage run -a --source=mysql_class test/unit/mysql_class/slaverep_getloginfo.py
coverage run -a --source=mysql_class test/unit/mysql_class/slaverep_getothers.py
coverage run -a --source=mysql_class test/unit/mysql_class/slaverep_getthrstat.py
coverage run -a --source=mysql_class test/unit/mysql_class/slaverep_gettime.py
coverage run -a --source=mysql_class test/unit/mysql_class/slaverep_isslaveup.py
coverage run -a --source=mysql_class test/unit/mysql_class/slaverep_isslverror.py
coverage run -a --source=mysql_class test/unit/mysql_class/slaverep_isslvrunning.py
coverage run -a --source=mysql_class test/unit/mysql_class/slaverep_showslvstate.py
coverage run -a --source=mysql_class test/unit/mysql_class/slaverep_startslave.py
coverage run -a --source=mysql_class test/unit/mysql_class/slaverep_stopslave.py
coverage run -a --source=mysql_class test/unit/mysql_class/slaverep_updslvstate.py
coverage run -a --source=mysql_class test/unit/mysql_class/slaverep_updslvtime.py
coverage run -a --source=mysql_class test/unit/mysql_class/slaverep_updgtidpos.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/_io_wait_chk.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/_sql_wait_chk.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/analyze_tbl.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/change_master_to.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/checksum.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/check_tbl.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/chg_slv_state.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/create_instance.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/disconnect.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/fetch_db_dict.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/fetch_logs.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/fetch_tbl_dict.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/optimize_tbl.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/purge_bin_logs.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/reset_master.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/reset_slave.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/select_wait_until.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/create_slv_array.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/crt_cmd.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/crt_srv_inst.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/fetch_slv.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/find_name.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/is_cfg_valid.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/is_logs_synced.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/is_rep_delay.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/start_slave_until.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/switch_to_master.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/sync_delay.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/sync_rep_slv.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/wait_until.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
coverage xml -i

