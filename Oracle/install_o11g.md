### 1.安装桌面
```
yum groupinstall "Desktop"
yum groupinstall "X Window System"
yum install gvim
```

### 2.修改系统参数
```
// 修改hostname
vim /etc/sysconfig/network
hostname database
vim /etc/hosts

// 修改文件句柄数
vim /etc/security/limits.conf
oracle soft nproc 2047
oracle hard nproc 16384
oracle soft nofile 1024 
oracle hard nofile 65536

// 安全参数
vi /etc/pam.d/login
session required /lib/security/pam_limits.so
session required pam_limits.so

// 系统参数
vi /etc/sysctl.conf
fs.file-max = 6815744
fs.aio-max-nr = 1048576
kernel.shmall = 2097152
kernel.shmmax = 2147483648
kernel.shmmni = 4096
kernel.sem = 250 32000 100 128
net.ipv4.ip_local_port_range = 9000 65500
net.core.rmem_default = 4194304
net.core.rmem_max = 4194304
net.core.wmem_default = 262144
net.core.wmem_max = 1048576

sysctl -p
```

### 3. 安装依赖包
由于服务器版本6.5，依赖包安装冲突，下载镜像挂载为本地yum源。

```
// 自建yum源
wget -c -t 0 -T 90 http://archive.kernel.org/centos-vault/6.5/isos/x86_64/CentOS-6.5-x86_64-bin-DVD1.iso

mount -o loop /media/iso/CentOS-6.5-x86_64-bin-DVD1.iso /media/rhel/

cd  /etc/yum.repos.d/ 
mv CentOS-Base.repo CentOS-Base.repose_bak
mv CentOS-Debuginfo.repo CentOS-Debuginfo.repo_bak

vi /etc/yum.repos.d/CentOS-Media.repo
[HZ-media]                     
name=CentOS 6.5               
baseurl=file:///media/rhel/     
gpgcheck=1                     
enabled=1                      
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6

yum install binutils compat-libstdc++ elfutils-libelf elfutils-libelf-devel elfutils-libelf-devel* gcc gcc-c++ glibc glibc-common glibc-devel glibc-headers kernel-headersksh libaio libgcc libgomp libstdc++ libstdc++-devel make numactl-develsysstat unixODBC unixODBC-devel
```

### 4. 创建用户组
```
groupadd oinstall 
groupadd dba
useradd -g oinstall -g dba -m oracle
passwd oracle

// 安装目录
mkdir -p /home/oracle/app/{oracle,oradata}
mkdir /home/oracle/app/oracle/product
chown -R oracle:oinstall /home/oracle/app
yum install tree
tree /home/oracle

cd /opt/linux.x64_11gR2/database/install
chmod 777 .oui
chmod 777 unzip

vi /etc/profile
if [ $USER = "oracle" ]; then
	if [ $SHELL = "/bin/ksh" ]; then
		ulimit -p 16384
		ulimit -n 65536
	else
		ulimit -u 16384 -n 65536
	fi
fi

su oracle

// oracle用户环境变量
vim ~/.bash_profile
export ORACLE_BASE=/home/oracle/app 
export ORACLE_HOME=$ORACLE_BASE/oracle/product/11.2.0/dbhome_1
export ORACLE_SID=orcl
export PATH=$PATH:$HOME/bin:$ORACLE_HOME/bin
export LD_LIBRARY_PATH=$ORACLE_HOME/lib:/usr/lib

[oracle@database database]$  ./runInstaller -ignoreSysPrereqs -ignorePrereq -silent -responseFile ./response/db_install.rsp
```


### 5. 测试链接
```
~/app/oracle/product/11.2.0/dbhome_1/bin/sqlplus / as sysdba
show v$version
```

### 6. docker 镜像
```
docker run -d -p 8080:8080 -p 1521:1521 --name oracle-db satg89/oracle-12c
docker logs -f oracle-db
docker exec -it  oracle-db /bin/bash
```


### Reference
https://www.cnblogs.com/zzuyczhang/p/5681299.html

https://www.linuxidc.com/Linux/2017-05/143918.htm

http://www.oracle.com/technetwork/database/enterprise-edition/downloads/oracle12c-linux-12201-3608234.html

https://docs.oracle.com/en/database/oracle/oracle-database/12.2/ladbi/preface.html#GUID-3F9284E1-EA40-4745-842A-373DB0B19608

https://docs.oracle.com/cd/E11882_01/install.112/e47689/pre_install.htm#LADBI1110

https://www.cnblogs.com/wq3435/p/6523840.html

http://blog.sina.com.cn/s/blog_d840ff330102v4j0.html



