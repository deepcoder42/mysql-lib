# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [5.2.0] - 2021-05-14
### Fixed
- mysql_class.Server.\_\_init\_\_:  Initialized self.config and self.sql_pass attributes.

### Added
- mysql_class.Server.setup_ssl:  Update the ssl attributes and append to config.
- mysql_class.Server.set_ssl_config:  Append ssl attributes to config.

### Changed
- mysql_class.SlaveRep.\_\_init\_\_:  Added capability to allow SSL attributes to be set.
- mysql_class.MasterRep.\_\_init\_\_:  Added capability to allow SSL attributes to be set.
- mysql_class.Rep.\_\_init\_\_:  Added capability to allow SSL attributes to be set.
- mysql_class.Server.\_\_init\_\_:  Added SSL configuration setting attributes.
- mysql_class.Server.set_pass_config:  Instead of initialize the dictionary, updated the dictionary and removed setting self.sql_pass attribute.


## [5.1.0] - 2021-04-21
- Updated to work in MySQL 8.0 environment.
- Updated to work in MySQL 5.7 environment.

### Fixed
- mysql_class.Server.connect:  Set self.conn_msg to None if login is successful.
- mysql_class.SlaveRep.get_others:  Renamed self.retry to self.tran_retry.
- mysql_class.SlaveRep.upd_slv_status:  Renamed conflicted self.retry to self.conn_retry and self.tran_retry.
- mysql_class.SlaveRep.\_\_init\_\_:  Renamed conflicted self.retry to self.conn_retry and self.tran_retry.

### Added
- mysql_class.Server.set_pass_config:  Set the self.sql_pass and self.config attributes.

### Changed
- mysql_class.Server.\_\_init\_\_:  Added call to set_pass_config method and removed setting of self.sql_pass and self.config attributes.
- mysql_class.SlaveRep.upd_slv_status:  The attributes self.tran_retry and self.run are in different location in MySQL 8.0.
- mysql_class.Server.upd_mst_rep_stat:  Set self.innodb_xa to None if not present in MySQL 8.0.
- mysql_class.Server.upd_srv_stat:  Set self.qry_cache to zero if not present in MySQL 8.0.
- mysql_class.Server.connect:  Added get_server_version call to set server's self.version attribute.
- mysql_class.Server.upd_srv_perf:  Added self.indb_buf_write to capture innodb_buffer_pool_write_requests.
- mysql_class.Server.\_\_init\_\_:  Added self.indb_buf_write attribute to hold MySQL's innodb_buffer_pool_write_requests.
- mysql_class.Server.\_\_init\_\_:  Added self.version attribute to hold MySQL server's version.


## [5.0.4] - 2021-02-05
### Changed
- mysql_libs.create_slv_array:  Added replication user information to mysql_class.SlaveRep instance call.
- mysql_libs:  Removed unnesscary \*\*kwargs from argument lists.
- mysql_class.MasterRep.connect, mysql_class.SlaveRep.connect:  Added silent option connect method call.

### Added
- mysql_libs.disconnect:  Disconnects one or more class database connections.


## [5.0.3] - 2021-01-07
### Changed
- mysql_libs.create_instance:  Added "rep_user" and "rep_japd" to be allowed to be passed to class instance if detected.
- mysql_class.SlaveRep.\_\_init\_\_:  Added self.rep_user and self.rep_japd for replication user information.
- mysql_class.Server.connect:  Set any error connection messages to self.conn_msg.
- mysql_class.Server.connect:  Added "silent" keyword argument to prevent printing any connection error messages.
- mysql_class.Server.\_\_init\_\_:  Added self.conn_msg to handle connection error messages.
- mysql_class.Server.upd_srv_stat:  Replaced percentage equations with calls to gen_libs.pct_int.


## [5.0.2] - 2020-11-16
### Fixed
- mysql_class.SlaveRep.upd_slv_status, mysql_class.SlaveRep.start_slave, mysql_class.SlaveRep.stop_slave, mysql_class.SlaveRep.upd_slv_time:  Added TypeError to exception handler for Seconds_Behind_Master attribute. 


## [5.0.1] - 2020-11-13
- Updated to work with (much older) mysql.connector v1.1.6 library module.

### Changed
- mysql_class.SlaveRep.start_slave, mysql_class.SlaveRep.upd_slv_status, mysql_class.SlaveRep.stop_slave, mysql_class.SlaveRep.upd_slv_time:  Changed Seconds_Behind_Master attribute to handle string or integer datatypes.


## [5.0.0] - 2020-07-28
- Breaking change.
- Changed the "change_master_to" command to use the replication user instead of the system user.

### Fixed
- mysql_class.SlaveRep.is_slave_up, mysql_class.SlaveRep.is_slv_running:  Added call to upd_slv_status to update attributes before check.
- mysql_libs.start_slave_until:  Changed variable name due to naming conflict.
- mysql_class.Server.\_\_init\_\_:  Initialized missing attributes cur_mem_mb and max_mem_mb.
- mysql_libs.select_wait_until: Converted gtid position to a string.
- mysql_libs.select_wait_until:  Changed to server.sql to force a single return.
- mysql_libs.is_cfg_valid:  When extra_def_file is not set.
- mysql_class.Rep.\_\_init\_\_, mysql_class.MasterRep.\_\_init\_\_, mysql_class.SlaveRep.\_\_init\_\_, mysql_class.Server.\_\_init\_\_:  Naming conflict between library module and argument.
- mysql_class.SlaveRep.connect, mysql_class.MasterRep.connect:  Only updates attributes if a connection is successful.

### Changed
- mysql_libs.fetch_tbl_dict, mysql_libs.check_tbl, mysql_libs.checksum, mysql_libs.analyze_tbl, mysql_class.Server.upd_srv_stat, mysql_class.Server.col_sql, mysql_class.Server.vert_sql, mysql_class.Server.chg_db, mysql_class.Server.upd_srv_perf, mysql_libs.optimize_tbl:  Changed variable name to standard naming convention.
- mysql_libs.crt_cmd, mysql_class.Server.is_connected, mysql_class.Server.sql:  Removed unnecessary else clause.
- mysql_class.Server.connect:  Changed database argument from positional to keyword.
- mysql_libs.switch_to_master:  Changed to reference returning list due to change in select_wait_until.
- mysql_libs.change_master_to:  Changed name of class attribute.
- mysql_libs.create_slv_array, mysql_libs.create_instance, mysql_libs.crt_srv_inst:  Changed name of configuration setting.
- mysql_class.MasterRep.\_\_init\_\_, mysql_class.Rep.\_\_init\_\_, mysql_class.Server.\_\_init\_\_, mysql_class.Rep.\_\_init\_\_, mysql_class.SlaveRep.\_\_init\_\_, mysql_class.MasterRep.\_\_init\_\_, mysql_class.SlaveRep.\_\_init\_\_:  Set a number of positional args to keyword args.
- mysql_class.Server.connect:  Added config attribute to connection command.
- mysql_class.Server.\_\_init\_\_:  Added config attribute for connecting to Mysql database.
- mysql_libs.crt_srv_inst:  Set keyword args in mysql_class.Server call.
- mysql_libs.create_instance:  Set keyword args in generic mysql_class class call.
- mysql_libs.create_slv_array:  Set keyword args in mysql_class.SlaveRep call.
- mysql_libs.change_master_to:  Replaced sql_user and sql_pass with rep_user and rep_pswd respectively.
- mysql_class.MasterRep.\_\_init\_\_:  Added rep_user and rep_pswd to the class' attributes.
- Documentation updates.

### Removed
- Removed machine module.


## [4.0.3] - 2020-05-07
### Fixed
- mysql_libs.fetch_logs:  Returning correct data set results from query.

### Changed
- mysql_libs.fetch_slv:  Refactored function to be more generic for general use.
- Documentation updates.


## [4.0.2] - 2019-07-17
### Fixed
- mysql_class.Server.is_connected:  Added check to ensure self.conn has been initialized before checking connection.
- mysql_class.SlaveRep.upd_slv_status:  Correctly referenced several global variables using the fetch_global_var call.
- mysql_class.SlaveRep.upd_gtid_pos:  Correctly referenced the system variable gtid_purged from fetch_sys_var call.
- mysql_class.SlaveRep.\_\_init\_\_:  Added retrieved_gtidset and exe_gtidset attributes, which were not initialized properly.


## [4.0.1] - 2019-07-16
### Fixed
- mysql_libs.create_slv_array:  Added connect call for each slave in array.
- mysql_libs.fetch_tbl_dict:  Changed sql() call to col_sql to produce correct format.

### Updated
- mysql_libs.create_slv_array:  Added new argument to determine whether to add down slave to array.


## [4.0.0] - 2019-07-09
Breaking Change

- Replaced the "MySQLdb" imported module with the "mysql.connector" module as the "MySQLdb" is no longer supported.

### Fixed:
- mysql_libs.sync_delay:  Fixed print syntax command problem.
- mysql_libs.fetch_slv:  Fixed print problem when no slave is found in the list.
- mysql_libs.find_name, mysql_libs.fetch_slv, mysql_libs.create_slv_array, mysql_libs.chg_slv_state, mysql_libs.is_cfg_valid:  Fixed problem with mutable default arguments issue.

### Changed
- Modified a large number of methods and functions:  Modified to use mysql.connector library.
- mysql_class.Server.upd_srv_stat:  Removed indb_add_pool attribute update.
- mysql_class.SlaveRep.upd_gtid_pos:  Removed setting purged_gtidset to none, not required.
- mysql_libs.crt_srv_inst, mysql_libs.chg_slv_state, mysql_libs.find_name:  Changed variable name for readability purposes.
- mysql_libs.is_rep_delay:  Replaced code with calls to \_io_rep_chk and \_sql_rep_chk to reduce factor complexity.
- mysql_libs.sync_delay:  Replaced code with call \_io_delay_chk to reduce factor complexity.
- mysql_libs.wait_until:  Replaced code with calls to \_io_wait_chk and \_sql_wait_chk to reduce factor complexity.
- mysql_class.compare_sets:  Changed argument call to \_inner_compare to include uuid and rngs objects.
- mysql_class.SlaveRep.\_\_init\_\_:  Removed the connection to the replication server.  Moved to SlaveRep.connect() method.
- mysql_class.MasterRep.upd_mst_status:  Replaced log stats update with call to upd_log_stats method.
- mysql_class.MasterRep.show_slv_hosts:  Removed res_set from the function argument list as it is no longer required.
- mysql_class.MasterRep.\_\_init\_\_:  Removed the connection to the replication server.  Moved to MasterRep.connect() method.
- mysql_class.Rep.get_serv_id:  Removed res_set from the function argument list as it is no longer required.
- mysql_class.Server.set_srv_binlog_crc:  Removed setting crc attr to none as its been done in \_\_init\_\_.
- mysql_class.show_slave_hosts, mysql_class.show_master_stat, mysql_class.fetch_global_var, mysql_class.show_slave_stat:  Removed res_set from the function argument list as it is no longer required.
- mysql_class.fetch_sys_var: Removed res_set from the function argument list as it is no longer required.
- mysql_class.Server.sql:  Removed the check to see if the connection is active.
- mysql_class.Server.sql:  Removed the database parameter from the function argument list as it is no longer required.
- mysql_class.Server.disconnect:  Removed returning the connection handler to the calling function.
- mysql_class.Server.connect:  Moved change database to within the connection string.

### Added
- mysql_class.Server.get_name:  Return the server's name.  Replacing the get_name methods in MasterRep and SlaveRep classes.
- mysql_libs.\_sql_rep_chk:  Create private function for is_rep_delay() to reduce factor complexity.
- mysql_libs.\_io_rep_chk:  Create private function for is_rep_delay() to reduce factor complexity.
- mysql_libs.\_io_delay_chk:  Create private function for sync_delay() to reduce factor complexity.
- mysql_libs.\_sql_wait_chk:  Create private function for wait_until() to reduce factor complexity.
- mysql_libs.\_io_wait_chk:  Created private function for wait_until() to reduce factor complexity.
- mysql_class.\_inner_compare:  Created private function for compare_sets() to reduce factor complexity.
- mysql_class.SlaveRep.connect:  Setups a connection to a replication server.
- mysql_class.MasterRep.connect:  Setups a connection to a replication server.
- mysql_class.Server.is_connected:  Checks to see if the connection is still active.
- mysql_class.Server.reconnect:  Reconnects to database if connect is non-active.
- mysql_class.Server.chg_db:  Change to another database.
- mysql_class.Server.cmd_sql:  Method to run command sql.
- mysql_class.Server.col_sql:  Method to run sql code with column definitions and return list of dictionaries.
- mysql_class.Server.vert_sql:  Method to run sql code with vertical definitions and return in dictionary format.

### Removed
- mysql_class.Server.\_\_init\_\_:  Removed reference to innodb_additional_mem_pool_size.  Deprecated in MySQL 5.6.3 and removed in MySQL 5.7.4.
- mysql_class.SlaveRep.get_name:  Replaced by the mysql_class.Server.get_name method.
- mysql_class.MasterRep.get_name:  Replaced by the mysql_class.Server.get_name method.
- mysql_class.Server.Row:  Removed the class it's no longer required.  The "mysql.connector" module has it's own Row iterator.
- mysql_class.compare_sets.inner_compare:  Remove inner function, was replaced by \_inner_compare.


## [3.2.1] - 2018-11-02
### Changed
- Documentation updates.


## [3.2.0] - 2018-09-11
### Removed
- mysql_libs.Is_Rep_Delay
- mysql_libs.Wait_Until
- mysql_libs.Start_Slave_Until
- mysql_libs.Is_Logs_Synced
- mysql_libs.Fetch_Sys_Var
- mysql_libs.Select_Wait_Until
- mysql_libs.Flush_Logs
- mysql_libs.Fetch_Global_Var
- mysql_libs.Show_Slave_Hosts
- mysql_libs.Sync_Delay
- mysql_libs.Start_Slave
- mysql_libs.Stop_Slave
- mysql_libs.Show_Slave_Stat
- mysql_libs.Show_Master_Stat
- mysql_libs.Is_Cfg_Valid
- mysql_libs.Crt_Cmd
- mysql_libs.Create_Instance
- mysql_libs.Fetch_Tbl_Dict
- mysql_libs.Crt_Srv_Inst
- mysql_libs.Create_Slv_Array
- mysql_libs.Crt_Srv_Inst
- mysql_libs.Create_Slv_Array
- mysql_libs.Change_Master_To
- mysql_libs.Chg_Slv_State
- mysql_libs.Sync_Rep_Slv
- mysql_libs.Find_Name
- mysql_libs.Fetch_Slv
- mysql_libs.Switch_To_Master
- mysql_libs.Reset_Slave
- mysql_libs.Reset_Master
- mysql_libs.Purge_Bin_Logs
- mysql_libs.Checksum
- mysql_libs.Check_Tbl
- mysql_libs.Optimize_Tbl
- mysql_libs.Analyze_Tbl
- mysql_libs.Fetch_Logs
- mysql_libs.Fetch_Db_Dict
- mysql_class.Master_Rep
- mysql_class.Slave_Rep


## [3.1.0] - 2018-06-01
### Changed
- mysql_libs.is_cfg_valid:  Refactored code to use the updated gen_libs.chk_crt_file function.
- mysql_libs.py, mysql_class.py:  Changed "gen_libs" calls to new naming schema.
- mysql_libs.py:  Changed "mysql_class" calls to new naming schema.


## [3.0.0] - 2018-03-26
Breaking Change

- Renamed server.py to mysql_class.py - standardize the class naming convention.
- Renamed commands.py to mysql_libs.py - standardize the class naming convention.

### Added
- mysql_libs.is_cfg_valid:  Replaced Is_Cfg_Valid function.
- mysql_libs.Crt_Cmd: Replaced crt_cmd function.
- mysql_libs.create_instance: Replaced Create_Instance function.
- mysql_libs.fetch_tbl_dict: Replaced Fetch_Tbl_Dict function.
- mysql_libs.crt_srv_inst: Replaced Crt_Srv_Inst function.
- mysql_libs.create_slv_array: Replaced Create_Slv_Array function.
- mysql_libs.change_master_to: Replaced Change_Master_To function.
- mysql_libs.wait_until: Replaced Wait_Until function.
- mysql_libs.start_slave_until: Replaced Start_Slave_Until function.
- mysql_libs.is_rep_delay: Replaced Is_Rep_Delay function.
- mysql_libs.sync_delay: Replaced Sync_Delay function.
- mysql_libs.is_logs_synced: Replaced Is_Logs_Synced function.
- mysql_libs.chg_slv_state: Replaced Chg_Slv_State function.
- mysql_libs.sync_rep_slv: Replaced Sync_Rep_Slv function.
- mysql_libs.fetch_slv: Replaced Fetch_Slv function.
- mysql_libs.find_name: Replaced Find_Name function.
- mysql_libs.select_wait_until: Replaced Select_Wait_Until function.
- mysql_libs.switch_to_master: Replaced Switch_To_Master function.
- mysql_libs.reset_slave: Replaced Reset_Slave function.
- mysql_libs.reset_master: Replaced Reset_Master function.
- mysql_libs.purge_bin_logs:  Replaced Purge_Bin_Logs function.
- mysql_libs.checksum:  Replaced Checksum function.
- mysql_libs.check_tbl:  Replaced Check_Tbl function.
- mysql_libs.optimize_tbl:  Replaced Optimize_Tbl function.
- mysql_libs.analyze_tbl:  Replaced Analyze_Tbl function.
- mysql_libs.fetch_logs:  Replaced Fetch_Logs function.
- mysql_class.slave_start:  Replaced mysql_libs.Start_Slave function.
- mysql_class.slave_stop:  Replaced mysql_libs.Stop_Slave function.
- mysql_class.show_slave_stat:  Replaced mysql_libs.Show_Slave_Stat function.
- mysql_class.show_slave_hosts:  Replaced mysql_libs.Show_Slave_Hosts function.
- mysql_class.flush_logs:  Replaced mysql_libs.Flush_Logs function.
- mysql_class.show_master_stat:  Replaced mysql_libs.Show_Master_Stat function.
- mysql_class.fetch_global_var:  Replaced mysql_libs.Fetch_Global_Var function.
- mysql_class.fetch_sys_var:  Replaced mysql_libs.Fetch_Sys_Var function.
- mysql_libs.fetch_db_dict:  Replaced Fetch_Db_Dict function.
- mysql_class.MasterRep:  Replaces Master_Rep class.
- mysql_class.SlaveRep:  Replaces Slave_Rep class.

### Changed
- mysql_libs.switch_to_master:  Changed Change_Master_To to change_master_to.
- mysql_libs.switch_to_master:  Changed Start_Slave to mysql_class.slave_start.
- mysql_libs.switch_to_master:  Changed Stop_Slave to mysql_class.slave_stop.
- mysql_libs.sync_delay:  Changed Wait_Until to wait_until.
- mysql_libs.sync_delay:  Changed Start_Slave_Until to start_slave_until.
- mysql_libs.Sync_Delay:  Changed commands.Start_Slave_Until to Start_Slave_Until.
- mysql_libs.sync_delay:  Changed Is_Rep_Delay to is_rep_delay.
- mysql_libs.sync_rep_slv:  Changed Sync_Delay to sync_delay.
- mysql_libs.sync_rep_slv:  Changed Is_Logs_Synced to is_logs_synced.
- mysql_libs.sync_rep_slv:  Changed Chg_Slv_State to chg_slv_state.
- mysql_libs.fetch_slv:  Changed Find_name call to find_name.
- mysql_libs.switch_to_master:  Changed Select_Wait_Until call to select_wait_until.
- mysql_class.py:  Changed function call from mysql_libs.Start_Slave to slave_start.
- mysql_class.py:  Changed function call from mysql_libs.Stop_Slave to slave_stop.
- mysql_class.py:  Changed function call from mysql_libs.Show_Slave_Stat to show_slave_stat.
- mysql_class.py:  Changed function call from mysql_libs.Show_Slave_Hosts to show_slave_hosts.
- mysql_class.py:  Changed function call from mysql_libs.Flush_Logs to flush_logs.
- mysql_class.py:  Changed function call from mysql_libs.Show_Master_Stat to show_master_stat.
- mysql_class.py:  Changed function call from mysql_libs.Fetch_Global_Var to fetch_global_var.
- mysql_class.py:  Changed function call from mysql_libs.Fetch_Sys_Var to fetch_sys_var.
- mysql_libs.Fetch_Sys_Var, mysql_class.fetch_sys_var:  Changed server to SERVER to avoid class name confusion.
- mysql_libs.py:  Changed function names to standard naming schema.
- mysql_libs.py:  Changed server references to mysql_class references.
- mysql_libs.py:  Change to single-source version control.
- mysql_class.py:  Changed class names to standard naming schema.
- mysql_class.py:  Changed commands references to mysql_libs references.
- mysql_class.py:  Change to single-source version control.

### Deprecated
- mysql_libs.Is_Cfg_Valid:  Replaced by is_cfg_valid function.
- mysql_libs.Crt_Cmd:  Replaced by crt_cmd function.
- mysql_libs.Create_Instance:  Replaced by create_instance function.
- mysql_libs.Fetch_Tbl_Dict:  Replaced by fetch_tbl_dict function.
- mysql_libs.Crt_Srv_Inst:  Replaced by crt_srv_inst function.
- mysql_libs.Create_Slv_Array:  Replaced by create_slv_array function.
- mysql_libs.Change_Master_To:  Replaced by change_master_to function.
- mysql_libs.Wait_Until:  Replaced by wait_until function.
- mysql_libs.Start_Slave_Until:  Replaced by start_slave_until function.
- mysql_libs.Is_Rep_Delay:  Replaced by is_rep_delay function.
- mysql_libs.Sync_Delay:  Replaced by sync_delay function.
- mysql_libs.Is_Logs_Synced:  Replaced by is_logs_synced function.
- mysql_libs.Chg_Slv_State:  Replaced by chg_slv_state function.
- mysql_libs.Sync_Rep_Slv:  Replaced by sync_rep_slv function.
- mysql_libs.Find_Name:  Replaced by find_name function.
- mysql_libs.Fetch_Slv:  Replaced by fetch_slv function.
- mysql_libs.Select_Wait_Until:  Replaced by select_wait_until function.
- mysql_libs.Switch_To_Master:  Replaced by switch_to_master function.
- mysql_libs.Reset_Slave:  Replaced by reset_slave function.
- mysql_libs.Reset_Master:  Replaced by reset_master function.
- mysql_libs.Purge_Bin_Logs:  Replaced by purge_bin_logs function.
- mysql_libs.Checksum:  Replaced by checksum function.
- mysql_libs.Check_Tbl:  Replaced by check_tbl function.
- mysql_libs.Optimize_Tbl:  Replaced by optimize_tbl function.
- mysql_libs.Analyze_Tbl:  Replaced by analyze_tbl function.
- mysql_libs.Fetch_Logs:  Replaced by fetch_logs function.
- mysql_libs.Start_Slave:  Replaced by mysql_class.slave_start function.
- mysql_libs.Stop_Slave:  Replaced by mysql_class.slave_stop function.
- mysql_libs.Show_Slave_Stat:  Replaced by mysql_class.show_slave_stat function.
- mysql_libs.Show_Slave_Hosts:  Replaced by mysql_class.show_slave_hosts function.
- mysql_libs.Flush_Logs:  Replaced by mysql_class.flush_logs function.
- mysql_libs.Show_Master_Stat:  Replaced by mysql_class.show_master_stat function.
- mysql_libs.Fetch_Global_Var:  Replaced by mysql_class.fetch_global_var function.
- mysql_libs.Fetch_Sys_Var:  Replaced by mysql_class.fetch_sys_var function.
- mysql_libs.Fetch_Db_Dict:  Replaced by fetch_db_dict function.
- mysql_class.Master_Rep:  Replaced by MasterRep class.
- mysql_class.Slave_Rep:  Replaced by SlaveRep class.

### Removed
- mysql_class.py:  Removed mysql_libs library module import.


## [2.3.0] - 2018-03-21
### Added
- Added single-source version control module.


## [2.2.0] - 2017-08-22
### Added
- commands.Is_Cfg_Valid function.

### Changed
- commands.py:  Add classification line for Sunspear use.
- server.py, commands.py:  Change single quotes to double quotes.
- server.py, commands.py:  Convert program to use local libraries from ./lib directory.
- server.GTIDSet.union, server.GTIDSet.\_\_init\_\_:  Replace gen_libs.normalize with gen_libs.Normalize.

### Removed
- commands.Call_Funcs function.
- server.show_bin_logs method.


## [2.1.0] - 2017-01-10
### Added
- commands.Switch_To_Master function.
- commands.Select_Wait_Until function.
- server.Slave_Rep.upd_gtid_pos method.

### Changed
- commands.Fetch_Sys_Var:  Added ability to set level at which the command will run at (e.g. Global | Session).
- server.py:  Deprecate retrieved_gtid and exe_gtid attributes as they are being replaced by retrieved_gtidset and exe_gtidset attributes.
- server.Slave_Rep.upd_slv_status, server.Slave_Rep.\_\_init\_\_:  To call upd_gtid_pos method.

### Deprecated
- server.retrieved_gtid attributes.
- server.exe_gtid attributes.


## [2.0.0] - 2017-01-03
### Added
- server.py:  Added new class to handle GTID sets.  New class will store GTIDs and have a set of rich comparsion operators as part of the class.
- server.GTIDSet class
- server.compare_sets function.  Usable only by GTIDSet class.
- server.py:  copy library.
- server.py:  Cleaned out all pre-V1.12 documentation changes.


## [1.19.0] - 2016-12-28
### Changed
- commands.Start_Slave_Until:  Modified function to handle using GTID and pre-GTID syntax.  The GTID syntax will include the before or after option in the command.  The function now returns an error flag and message to the calling function.
- commands.Is_Rep_Delay, commands.Wait_Until, commands.Sync_Delay, commands.Is_Logs_Synced:  Modified function to handle servers whether they have GTID enabled or use the file and log settings as in pre-MySQL 5.6 servers.
- commands.Is_Logs_Synced, commands.Is_Rep_Delay:  Simplified and streamlined the 'if' statements.
- commands.Wait_Until:  Changed argument list order due to some arguments will not always be used.
- commands.Sync_Delay:  For GTID servers using the "sql_after_gtid" option for the syncing process.
- commands.Fetch_Slv:  Modified function to remove sys.exit() command and also added error flag and message return with Slave instance name.
- commands.Chg_Slv_State:  Added error exception handling if no option passed.
- server.Server.upd_log_stats:  Changed to use Show_Master_Stat function.
- server.Rep.get_serv_id:  Changed to use Fetch_Sys_Var function.
- server.Master_Rep.upd_mst_status, server.Master_Rep.\_\_init\_\_:  Changed to use Show_Master_Stat function.
- server.Master_Rep.show_slv_hosts:  Changed to use Show_Slave_Hosts function.
- server.Slave_Rep.upd_slv_status, server.Slave_Rep.\_\_init\_\_:  Changed to use Show_Slave_Stat function and changed to use Fetch_Global_Var function.
- server.Slave_Rep.stop_slave:  Changed to use Stop_Slave function.
- server.Slave_Rep.start_slave:  Changed to use Start_Slave function.
- server.Slave_Rep.upd_slv_time, server.Slave_Rep.upd_slv_state:  Changed to use Show_Slave_Stat function.

### Deprecated
- commands.Call_Funcs function.
- server.Rep.show_bin_logs:  Should not be part of the class.

### Removed
- commands.get_db_list function.
- commands.chksum_tbl function.
- commands.purge_bin_logs function.
- commands.get_tbl_list function.
- commands.flush_logs function.
- commands.Create_Cfg_Array function.
- commands.Disconnect function.
- commands.show_master function.
- commands.show_slave function.
- commands.stop_slave function.
- commands.start_slave function.
- commands.show_slv_hosts function.
- commands.show_global_var function.
- commands.show_bin_logs function.
- commands.get_serv_id function.


## [1.18.0] - 2016-12-16
### Added
- commands.Reset_Slave function.
- commands.Sync_Rep_Slv function.

### Changed
- server.Server.set_srv_gtid:  Corrected error in setting of gtid_mode attribute.  Changed value of GTID-enable from ON to True and GTID-disable from OFF or None to False.


## [1.17.0] - 2016-11-04
### Added
- commands.py:  MySQL 5.6 (GTID enabled) requires a reset master command the database for a database load which has GTIDs included in the dump.
- commands.Reset_Master function.
- server.py:  MySQL 5.6 - Added GTID set information to the Master Rep class for pre-MySQL 5.6 the attributes will be set to NULL.

### Changed
- commands.py:  MySQL 5.6 (GTID enabled) when using replication, will require the use of the auto position option within the change master command.
- commands.Change_Master_To:  To determine which options to use depending on GTID mode state.
- server.Master_Rep.\_\_init\_\_:  Added attribute for the Executed GTID Set information, also updated the GTID mode attribute from the Super class.
- server.Master_Rep.upd_mst_status:  Update the Executed GTID Set attribute.
- server.Slave_Rep.\_\_init\_\_:  Added attributes for MySQL 5.6.
- server.Slave_Rep.upd_slv_status:  Update the attributes for MySQL 5.6.
- server.Slave_Rep.get_err_stat:  Added IO and SQL error times to output.


## [1.16.0] - 2016-10-20
### Added
- server.py:  Setup and initialize the servers binary log checksum status.
- server.Server.set_srv_binlog_crc method.

### Changed
- server.Server.\_\_init\_\_:  Added attribute for the Servers binary log checksum mode.


## [1.15.0] - 2016-10-19
### Added
- server.py:  Changes to setup and initialize the servers GTID mode status.
- server.Server.set_srv_gtid method.

### Changed
- server.Server.\_\_init\_\_:  Added attribute for the Servers GTID mode.


## [1.14.0] - 2016-10-12
### Changed
- server.py:  Below changes made due to changes made in v1.13.0.
- server.Master_Rep.\_\_init\_\_, server.Slave_Rep.\_\_init\_\_, server.Rep.\_\_init\_\_:  Added \*\*kwargs to argument list.  Added \*\*kwargs to super class call.


## [1.13.0] - 2016-09-27
### Changed
- commands.Crt_Cmd:  Check to see if default-extra-file has been set and modify the command line appropriately.
- commands.Create_Instance:  Added default extra file argument to class instanation call.
- commands.Create_Slv_Array:  Changed port to an integer.  This is to allow the use of different ports to MySQL database other than port 3306.
- commands.py, server.py:  MySQL 5.6 now gives warning if password is passed on the command line.  To suppress this warning, will require the use of the --defaults-extra-file option.
- server.Server.\_\_init\_\_:  Added \*\*kwargs to argument list.  Set extra_def_file for the defaults-extra-file option.

### Deprecated
- commands.Create_Cfg_Array function.
- commands.Disconnect function.


## [1.12.0] - 2016-09-07
### Added
- commands.Crt_Cmd function.

### Changed
- server.py:  Programs cannot connect to a database using a different port other than the default port of 3306.
- server.Server.connect:  Added port to the connection argument list and changed the argument list from positional to named.  NOTE:  When connecting to a database, if 'localhost' is used for the host, this will automatically use port 3306, any other port number is ignored.  Use IP, host name, or '127.0.0.1' to set the port number to something other than 3306.


## [1.11.0] - 2016-05-23
### Added
- server.Server.upd_srv_perf method.

### Changed
- server.Server.\_\_init\_\_:  Added attributes for the Servers performance statistics settings.


## [1.10.0] - 2016-04-15
### Added
- commands.Analyze_Tbl function.
- commands.Optimize_Tbl function.
- commands.Check_Tbl function.
- server.Server.upd_srv_stat method.

### Changed
- server.Server.\_\_init\_\_:  Added attributes for the Servers memory and other status configuration settings.

### Fixed
- commands.Fetch_Global_Var:  Corrected error in order of arguments.
- commands.py:  Corrected an error in Version Information section.


## [1.9.0] - 2016-03-16
### Changed
- server.Server.connect:  Added exception handler to deal with a down or non-reponding server.
- server.Slave_Rep.\_\_init\_\_:  Added 'if' to prevent attributes being updated if there is no connection to the database.


## [1.8.0] - 2015-12-29
### Added
- server.Position class:  This class will contain the binlog position for a specific server.
- server.py:  Added collections library.


## [1.7.0] - 2015-12-21
### Added
- commands.Stop_Slave function.
- commands.Show_Slave_Stat function.
- commands.Show_Master_Stat function.
- commands.Fetch_Global_Var function.
- commands.Show_Slave_Hosts function.
- commands.Start_Slave function.
- server.Server.upd_mst_rep_stat method.
- server.Server.upd_slv_rep_stat method.
- server.Server.fetch_mst_rep_cfg method.
- server.Server.fetch_slv_rep_cfg method.

### Changed
- server.Server.\_\_init\_\_:  Added 10 new attributes.

### Deprecated
- commands.stop_slave function.
- commands.show_slave function.
- commands.show_master function.
- commands.get_tbl_list function.
- commands.get_serv_id function.
- commands.show_global_var function.
- commands.show_slv_hosts function.
- commands.start_slave function.


## [1.6.0] - 2015-12-11
### Added
- commands.Fetch_Tbl_Dict function.
- commands.Create_Instance function.
- commands.Checksum function.
- server.Slave_Rep.fetch_do_tbl method.
- server.Slave_Rep.fetch_ign_tbl method.
- server.Rep.fetch_do_db method.
- server.Rep.fetch_ign_db method.

### Deprecated
- commands.chksum_tbl function.


## [1.5.0] - 2015-12-09
### Added
- commands.Flush_Logs function.
- commands.Fetch_Logs function.
- commands.Purge_Bin_Logs function.
- server.Server.upd_log_stats method.
- server.Server.flush_logs method.
- server.Server.fetch_log method.
- server.py:  Updated documentation on class & library dependencies versions.

### Changed
- commands.py:  Updated documentation on library dependencies versions.
- server.Server.\_\_init\_\_:  Added 4 new attributes.

### Deprecated
- commands.flush_logs function.
- commands.show_bin_logs function.
- commands.purge_bin_logs function.


## [1.4.0] - 2015-12-03
### Added
- commands.Fetch_Db_Dict function.
- commands.Crt_Srv_Inst function.
- commands.py:  Added library gen_libs.
- server.Slave_Rep.is_slv_running method.
- server.Slave_Rep.is_slv_error method.

### Deprecated
- commands.get_db_list function.


## [1.3.0] - 2015-12-01
### Added
- commands.Fetch_Sys_Var function.
- commands.Find_Name function.
- commands.Is_Logs_Synced function.
- commands.Change_Master_To function.
- commands.Start_Slave_Until function.
- commands.Wait_Until function.
- commands.Is_Rep_Delay function.
- commands.Sync_Delay function.
- commands.Chg_Slv_State function.
- commands.Fetch_Slv function.
- commands.Call_Funcs function.
- commands.Create_Cfg_Array function.
- commands.Create_Slv_Array function.
- commands.Disconnect function.
- commands.py:  Added library time.
- server.Master_Rep.upd_mst_status method.

### Changed
- commands.Create_Slv_Array:  Added classes server and machine.
- server.Slave_Rep.\_\_init\_\_:  Added attr:  read_only.
- server.Slave_Rep.upd_slv_status:  Added attr: read_only.

### Fixed
- server.Slave_Rep.upd_slv_state:  Corrected error in command during connection to server.


## [1.2.0] - 2015-11-20
### Added
- server.Master_Rep.get_log_info method.
- server.Master_Rep.get_name method.
- server.Slave_Rep.get_log_info method.
- server.Slave_Rep.get_name method.
- server.Slave_Rep.get_thr_stat method.
- server.Slave_Rep.get_err_stat method.
- server.Slave_Rep.upd_slv_time method.
- server.Slave_Rep.get_time method.
- server.Slave_Rep.get_others method.

### Changed
- server.Slave_Rep.\_\_init\_\_:  Added 3 new attributes.
- server.Slave_Rep.upd_slv_status:  Added 3 new attributes.
- server.py:  Modified documentation as it was missing some class and library dependencies.


## [1.1.0] - 2015-11-13
### Added
- server.Rep class.
- server.Master_Rep class.
- server.Slave_Rep class.
- server.py:  Added additional information to the version setup in library.
- server.py:  Added gen_libs to local libraries.


## [1.0.0] - 2015-11-06
### Added
- commands.py:  Initial program creation.
