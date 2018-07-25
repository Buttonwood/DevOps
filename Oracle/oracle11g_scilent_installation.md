title: oracle 11g installation
tags: [DB]
categories: [DB]
date: 2018-06-01 21:51
mathjax: false

---


### 1.	安装依赖包
```
rpm -qa | grep  pdksh-5.2.14-36.el5

rpm -ivh /int/rpm-ol6.6/libaio-devel-0.3.107-10.el6.x86_64.rpm
rpm -ivh /int/rpm-ol6.6/unixODBC-2.2.14-14.el6.x86_64.rpm
rpm -ivh /int/rpm-ol6.6/unixODBC-devel-2.2.14-14.el6.x86_64.rpm

rpm -ivh /int/rpm-ol6.6/telnet-0.17-48.el6.x86_64.rpm
rpm -ivh /int/rpm-ol6.6/telnet-server-0.17-48.el6.x86_64.rpm
```

### 2. 更改系统配置
#### 2.1 
```
vim /etc/sysconfig/selinux
SELINUX=disabled 
```
#### 2.2
```
vim /etc/sysctl.conf
kernel.sem = 250 32000 100 128
net.ipv4.ip_local_port_range = 9000 65500
net.core.rmem_default = 262144
net.core.rmem_max = 4194304
net.core.wmem_default = 262144
net.core.wmem_max = 1048576
fs.aio-max-nr = 1048576
fs.file-max = 6815744
# 生效
sysctl -p
```
#### 2.3
```
vim /etc/pam.d/login
session     required    pam_limits.so 
```
#### 2.4
```
vim /etc/security/limits.conf
oracle         soft    nproc    10000
oracle         hard    nproc    16384
oracle         soft    nofile   52768
oracle         hard    nofile   6553
root soft nproc 2047
root hard nproc 16384
root soft nofile 1024
root hard nofile 65536
```
#### 2.5 创建相关用户组
```
groupadd oinstall 
groupadd dba 
useradd -g oinstall -G dba oracle 
passwd oracle // oracle

id oracle
mkdir -p /data/app/oracle
mkdir -p /data/app/oraInventory
chown -R oracle:oinstall /data/app/
chmod -R 755 /data
```
#### 2.6 oracle用户生效
```
vim /home/oracle/.bash_profile
umask 022  
export ORACLE_BASE=/data/app  
export ORACLE_HOME=/data/app/oracle/product/11.2.0/db_1
export ORACLE_SID=orcl  
export LANG=en_US.UTF-8
#export NLS_LANG="SIMPLIFIED CHINESE_CHINA.ZHS16GBK"
export NLS_LANG="american_america.zhs16gbk"
```
#### 2.7 全局生效
```
vi /etc/profile
export PATH=$PATH:/data/app/oracle/product/11.2.0/db_1/bin
export ORACLE_BASE=/data/app  
export ORACLE_HOME=/data/app/oracle/product/11.2.0/db_1
export ORACLE_SID=orcl  
export LANG=en_US.UTF-8
#export NLS_LANG="SIMPLIFIED CHINESE_CHINA.ZHS16GBK" 
export NLS_LANG="american_america.zhs16gbk" 
```

### 3. 静默安装
#### 3.1 
```
vim response/db_install.rsp
oracle.install.responseFileVersion=/oracle/install/rspfmt_dbinstall_response_schema_v11_2_0
oracle.install.option=INSTALL_DB_SWONLY
ORACLE_HOSTNAME=D65012
INVENTORY_LOCATION=/data/app/oraInventory
SELECTED_LANGUAGES=en,zh_CN,zh_TW
ORACLE_HOME=/data/app/oracle/product/11.2.0/db_1
ORACLE_BASE=/data/app
oracle.install.db.InstallEdition=EE
oracle.install.db.isCustomInstall=false
oracle.install.db.DBA_GROUP=dba
oracle.install.db.OPER_GROUP=oinstall
oracle.install.db.config.starterdb.type=GENERAL_PURPOSE
oracle.install.db.config.starterdb.globalDBName=ocrl
oracle.install.db.config.starterdb.SID=ocrl
oracle.install.db.config.starterdb.characterSet=AL32UTF8
oracle.install.db.config.starterdb.memoryOption=true
oracle.install.db.config.starterdb.memoryLimit=4069
oracle.install.db.config.starterdb.installExampleSchemas=false
oracle.install.db.config.starterdb.enableSecuritySettings=true
oracle.install.db.config.starterdb.password.ALL=oracle
oracle.install.db.config.starterdb.control=DB_CONTROL
oracle.install.db.config.starterdb.dbcontrol.\
enableEmailNotification=false
oracle.install.db.config.starterdb.automatedBackup.enable=false
SECURITY_UPDATES_VIA_MYORACLESUPPORT=false
DECLINE_SECURITY_UPDATES=true
```
#### 3.2 
```
vim /home/oracle/oraInst.loc
inventory_loc=/data/app/oraInventory
inst_group=oinstall

chown oracle:oinstall /home/oracle/oraInst.loc
chmod 664 /home/oracle/oraInst.loc
```
#### 3.3
```
su oracle
[oracle@D65012 database]$  ./runInstaller -silent \
-responseFile /home/oracle/database/response/db_install.rsp \
-invPtrLoc /home/oracle/oraInst.loc \
-ignoreSysPrereqs -ignorePrereq

su root
sh /data/app/oracle/product/11.2.0/db_1/root.sh
```
#### 3.4 创建数据库实例
```
vi response/dbca.rsp
[GENERAL]
RESPONSEFILE_VERSION = "11.2.0"
OPERATION_TYPE = "createDatabase"
[CREATEDATABASE]
GDBNAME = "D65012"
SID = "orcl"
TEMPLATENAME = "General_Purpose.dbc"
SYSPASSWORD = "sys"
SYSTEMPASSWORD = "sys"
DATAFILEDESTINATION = /data/app/oracle/oradata
CHARACTERSET = "ZHS16GBK"
TOTALMEMORY = "4096"

[oracle@D65012 response]$ dbca -silent -responseFile \
/home/oracle/database/response/dbca.rsp
```
#### 3.5 监听
```
netca /silent /responsefile /home/oracle/database/response/netca.rsp
```

##### 3.5.1 listener.ora
```
vim /data/app/oracle/product/11.2.0/db_1/network/admin/listener.ora
LISTENER =
  (DESCRIPTION_LIST =
    (DESCRIPTION =
      (ADDRESS = (PROTOCOL = IPC)(KEY = EXTPROC1521))
      (ADDRESS = (PROTOCOL = TCP)(HOST = D65012)(PORT = 1521))
      (ADDRESS_LIST =
        (ADDRESS = (PROTOCOL = IPC)(KEY = EXTPROC))
      )
    )
  )

ADR_BASE_LISTENER = /data/app
```

##### 3.5.2 tnsnames.ora
```
vim /data/app/oracle/product/11.2.0/db_1/network/admin/tnsnames.ora
LISTENER_D65012 =
  (ADDRESS = (PROTOCOL = TCP)(HOST = 10.119.1.126)(PORT = 1521))

D65012  =
  (DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = 10.119.1.126)(PORT = 1521))
    (CONNECT_DATA =
      (SERVER = DEDICATED)
      (SERVICE_NAME = D65012)
      (UR=A)
    )
  )
```
##### 3.5.3 lsnrctl
```
lsnrctl start 
lsnrctl status
lsnrctl stop
```

##### 3.5.4  mount
```
sqlplus /nolog
SQL> conn / as sysdba;
SQL> alter user system identified by "oracle";
SQL> alter user sys identified by "oracle";

SQL> alter database mount;
SQL> alter database open;
SQL> show parameter service_name;

SQL> shutdown immediate; 
SQL> startup;
```

##### 3.5.5 apps
```
SQL> create user apps identified by "apps";
SQL> grant connect,resource to apps;

sqlplus apps/apps@localhost/helowin
sqlplus sys/oracle@D65012/D65012 as sysdba
```

### References
*	https://blog.csdn.net/jameshadoop/article/details/48223645
*	https://blog.csdn.net/jameshadoop/article/details/48086933
*	http://www.dbaexpert.com/blog/create-oracle-12c-rac-databases-in-silent-mode/
* 	https://docs.oracle.com/cd/E11882_01/em.112/e12255/c_oui_appendix.htm#OUICG379


