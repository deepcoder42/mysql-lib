# Python project that contains common libraries and classes for MySQL database.
# Classification (U)

# Description:
  This project consists of a number of Python files that contain common function libraries and classes for connecting to and operating in a MySQL database and Mysql replication set.


###  This README file is broken down into the following sections:
  * Prerequisites
  * Installation
    - Pip Installation
  * Testing
    - Unit
    - Integration


# Prerequisites:

  * List of Linux packages that need to be installed on the server via git.
    - git
    - python-pip

  * Local class/library dependencies within the program structure.
    - lib/machine
    - lib/gen_libs


# Installation:

### Pip Installation:
  * From here on out, any reference to **{Python_Project}** or **PYTHON_PROJECT** replace with the baseline path of the python program.
  * Replace **{Other_Python_Project}** with the baseline path of another python program.

###### Create requirements file in another program's project to install mysql-lib as a library module.

Create requirements-mysql-lib.txt file and requirements-python-lib.txt files:

```
cd {Python_Project}
cp requirements-mysql-lib.txt > {Other_Python_Project}/requirements-mysql-lib.txt
cp requirements-python-lib.txt > {Other_Python_Project}/requirements-python-lib.txt
```

##### Modify the other program's README.md file to add the pip commands under the "Install supporting classes and libraries" section.

Modify the {Other_Python_Project}/README.md file:

```
   pip install -r requirements-mysql-lib.txt --target mysql_lib --system
   pip install -r requirements-python-lib.txt --target mysql_lib/lib --system
```

##### Add the general Mysql-Lib requirements to the other program's requirements.txt file.  Remove any duplicates.

Add/modify the following lines to the {Other_Python_Project}/requirements.txt file:

```
mysql-connector-python==8.0.16
simplejson==2.0.9
```


# Testing

# Unit Testing:

### Installation:

Install the project using git.

```
umask 022
cd {Python_Project}
git clone git@github.com:deepcoder42/mysql-lib.git
```

Install/upgrade system modules.

```
cd mysql-lib
sudo bash
umask 022
pip install -r requirements.txt --upgrade --system
exit
```

### Testing:

```
cd {Python_Project}/mysql-lib
test/unit/mysql_libs/unit_test_run.sh
test/unit/mysql_class/unit_test_run.sh
```

### Code Coverage:
```
cd {Python_Project}/mysql-lib
test/unit/mysql_libs/code_coverage.sh
test/unit/mysql_class/code_coverage.sh
```

# Integration Testing:

NOTE:  Integration testing will require access to a MySQL database server.

### Installation:

Install the project using the procedures in the Unit Testing - Installation section.

### Configuration:

Create MySQL configuration file.

Make the appropriate change to the environment.
  * Change these entries in the MySQL setup:
    - user = "USER"
    - japd = "PSWORD"
    - host = "HOST_IP"
    - name = "HOST_NAME"
    - sid = SERVER_ID
    - extra_def_file = "PYTHON_PROJECT/config/mysql.cfg"
    - cfg_file = "DIRECTORY_PATH/my.cnf"

  * Change these entries only if required:
    - serv_os = "Linux"
    - port = 3306

```
cd test/integration/config
cp mysql_cfg.py.TEMPLATE mysql_cfg.py
vim mysql_cfg.py
chmod 600 mysql_cfg.py
```

Create MySQL definition file.

Make the appropriate change to the environment.
  * Change these entries in the MySQL definition file:
    - password="PASSWORD"
    - socket=DIRECTORY_PATH/mysql.sock

```
cp mysql.cfg.TEMPLATE mysql.cfg
vim mysql.cfg
chmod 600 mysql.cfg
```

### Testing:

```
cd {Python_Project}/mysql-lib
test/integration/mysql_libs/integration_test_run.sh
test/integration/mysql_class/integration_test_run.sh
```

### Code Coverage:
```
cd {Python_Project}/mysql-lib
test/integration/mysql_libs/code_coverage.sh
test/integration/mysql_class/code_coverage.sh
```

### Master Replication Testing Section

This section requires the database being tested to be a master database in a MySQL replica set.  Will include all previous testing units.

### Configuration:

Create MySQL configuration file.

Make the appropriate change to the environment.
  * Change these entries in the MySQL setup:
    - user = "USER"
    - japd = "PSWORD"
    - rep_user = "REP_USER"
    - rep_japd = "REP_PSWORD"
    - host = "HOST_IP"
    - name = "HOST_NAME"
    - sid = SERVER_ID
    - extra_def_file = "PYTHON_PROJECT/config/mysql.cfg"
    - cfg_file = "DIRECTORY_PATH/my.cnf"

  * Change these entries only if required:
    - serv_os = "Linux"
    - port = 3306

```
cd test/integration/config
cp mysql_cfg.py.TEMPLATE master_mysql_cfg.py
vim master_mysql_cfg.py
chmod 600 master_mysql_cfg.py
```

Create MySQL definition file.

Make the appropriate change to the environment.
  * Change these entries in the MySQL definition file:
    - password="PASSWORD"
    - socket=DIRECTORY_PATH/mysql.sock

```
cp mysql.cfg.TEMPLATE mysql.cfg
vim mysql.cfg
chmod 600 mysql.cfg
```

### Testing:

```
cd {Python_Project}/mysql-lib
test/integration/mysql_class/rep_integration_test_run.sh
```

### Code Coverage:
```
cd {Python_Project}/mysql-lib
test/integration/mysql_class/rep_code_coverage.sh
```

### Slave Replication Testing Section

This section requires the database being tested to be a slave database in a MySQL replica set.

Testing will also require a master_mysql_cfg.py file to be present in the config directory.  See above for details on creating one.

### Configuration:

Create MySQL configuration file.

Make the appropriate change to the environment.
  * Change these entries in the MySQL setup:
    - user = "USER"
    - japd = "PSWORD"
    - rep_user = "REP_USER"
    - rep_japd = "REP_PSWORD"
    - host = "HOST_IP"
    - name = "HOST_NAME"
    - sid = SERVER_ID
    - extra_def_file = "PYTHON_PROJECT/config/mysql.cfg"
    - cfg_file = "DIRECTORY_PATH/my.cnf"

  * Change these entries only if required:
    - serv_os = "Linux"
    - port = 3306

```
cd test/integration/config
cp mysql_cfg.py.TEMPLATE slave_mysql_cfg.py
vim slave_mysql_cfg.py
chmod 600 slave_mysql_cfg.py
```

Create MySQL definition file.

Make the appropriate change to the environment.
  * Change these entries in the MySQL definition file:
    - password="PASSWORD"
    - socket=DIRECTORY_PATH/mysql.sock

```
cp mysql.cfg.TEMPLATE mysql.cfg
vim mysql.cfg
chmod 600 mysql.cfg
```

Create a MySQL slave configuration file.

Make the appropriate change to the environment.
  * Change these entries in the MySQL slave setup:
    - user = USER
    - japd = PSWORD
    - rep_user = REP_USER
    - rep_japd = REP_PSWORD
    - host = HOST_IP
    - name = HOSTNAME
    - sid = SERVER_ID

  * Change these entries only if required:
    - cfg_file = None
    - serv_os = Linux
    - port = 3306

  * NOTE:  Create a new set of entries for each slave in the MySQL replica set.

```
cp slave.txt.TEMPLATE slave.txt
vim slave.txt
chmod 600 slave.txt
```

### Testing:

```
cd {Python_Project}/mysql-lib
test/integration/mysql_class/slaverep_integration_test_run.sh
```

### Code Coverage:
```
cd {Python_Project}/mysql-lib
test/integration/mysql_class/slaverep_code_coverage.sh
```

