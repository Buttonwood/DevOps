### User
```
select username,password,default_tablespace,account_status from dba_users;

create user "" identified by 1234
default tablespace Users
temporary tablespace temp
quota 20M On Users
unlimited tablespaces
--Password Expire
account unlock;


drop user '';
drop user scott cascade;


alter user '' identified by ''
default tablespace ''
temporary tablespace ''
quota unlimited on ''
```

### Grant
```
grant session, create table, create view, create trigger, create procedure to 
 '';

-- 	系统权限
create session
create table
create resource
create view
create user
create trigger
create tablespace
create procedure

alter session,database,user 

-- 必须权限
grant create session, create table, unlimited tablespace to '';

revoke create procedure, create view from '';

-- 对象权限
grant , , on , , to , , with grant option;
grant select on dept to scott with grant option;
grant insert(empnpo),update(sal) on emp to u1, u2;
grant execute on functional to u1;

revoke , , on , , from , ,;
revoke update(sal) on emp from u1,u2;
revoke update on emp from u2;

--数据库中所有的系统权限--
select name from system_privilege_map;

--sys从数据字典视图dba_sys_privs中查询任何用户所具有的系统权限--
select grantee, privilege, admin_option from dba_sys_privs;

--普通用户通过user_sys_privs查询用户直接获得的系统权限，即通过grant命令授予当前用户的系统权限--
select * from user_sys_privs;

--从数据字典视图session_privs中可以查询一个用户在当前会话中所具有的系统权限--
--session_privs权限==直接获得的权限 + 該用户从角色中间接获得的系统权限--
select * from session_privs;

-- dba_tab_privs;
-- dba_col_privs;
-- user_tab_privs;
-- user_col_privs;

select grantee,privilege,grantor,table_name,grantable from dba_tab_privs;

select grantee,table_name,column_name,privilege,grantor,grantable from 
dba_col_privs;

select grantee,table_name,column_name,privilege,grantor,grantable from 
user_tab_privs;
```

### Role
```
-- connect
-- create session

-- resource
-- create sequence
-- create triger
-- create cluster
-- create procedure
-- create type
-- create operator
-- create table
-- create indextype

create role '';
drop role '';
grant select on emp to '';
revoke select on emp from '';

--	dba_roles				    记录数据库中所有角色
--	dba_role_privs          记录所有被授予用户或另一角色的角色
--	user_role_privs         记录所有被授予当前用户的角色
--	role_role_privs         记录一个角色中包含的其他角色
--	role_sys_privs          记录一个角色中包含的系统权限
--	role_tab_privs          记录一个角色中包含的对象权限
--	session_roles           记录当前会话中所使用的角色

select role from dba_roles;
select * from dba_role_privs;
select * from role_sys_privs where role = 'CONNECT';
```

### Profile
```
select from v$session where username='';

alter system kill session '144,7';
alter user '' account lock;

create profile '' limit;
create user identified by '' profile '';
alter user '' profile '';

-- Failed_Login_Attempts        允许的失败登录次数，默认值为10次
-- Password_Lock_Time	 账号锁定时间，默认值为1天
-- Password_Life_Time	 口令的有效期，默认值为180天
-- Password_Grace_Time  口令有效期的延长期，默认值为-周、7天
-- Password_Reuse_Time	 为了再次使用过去用过的口令，必须经过的天数
-- Password_Reuse_Max   为了再次使用过去用过的口令，必须使用不同口令的次数
-- Password_Reuse_Time  和 Password_Reuse_Max 必须一起使用

create profile '' limit failed_login_attempts 3 password_lock_time 5;
create profile '' limit password_reuse_time 30 password_reuse_max 5;

alter system set resource_limit=true;

-- Sessions_Per_User    	  一个用户所允许的并发会话数目
-- Cpu_Per_Session	  用户在一个会话内所使用的Cpu时间的总和，时间单位为0.01秒
-- Logical_Reads_Per_Session	用户在一个会话内所能访问的数据块的数量(包括物理读和逻辑读的数量)
-- Connect_Time	一个用户会话所能持续的时间，以分钟为单位；超过这个时间，会话将自动断开
-- Idle_Time	一个用户会话所允许的连续的空闲时间，以分钟为单位，超过这个时间，会话将自动断开
-- Private_Sga	如果数据库服务器的连接模式为共享模式，这个参数用来限制为一个用户会话所分配的Sga空间
-- Cpu_Per_Call	用户执行的每条命令所使用的Cpu时间，时间单位为0.01秒
-- Logical_Reads_Per_Call	用户执行的每条命令所能访问的数据块的数量

create profile '' limit sessions_per_user 100 connect_time 5;
select * from dba_profiles where profile='default';
```
