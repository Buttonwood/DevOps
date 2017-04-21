

```
//	逻辑结构 
Database	--> Tablespace --> Segment --> Extent --> Oracle Block 
//	物理结构		|						|				|
				Datafiles					--->		OS Block
```

逻辑结构从左到右是包含关系，也是一对多的关系。

1.	一个数据库有一个或多个表空间。
2.	一个表空间有一个或多个段
3.	一个段有一个或多个区段
4.	一个区段有多个数据库块组成
5.	一个数据库块有多个操作系统数据库块组成

表空间T(Tablespace):上一个数据库由表空间组成，一个表空间只能属于一个数据库，反之不成立。一个表空间包含一个或多个操作系统文件（数据文件）。表空间包含一个或多个段。

段(Segment):段是表空间内的一个逻辑存储空间，一个表空间包含一个或多个段，一个段不能跨表空间，即一个段只能在一个表空间中，但段可以跨越数据文件，即一个段可以分布在同一个表空间的几个数据文件上。一个段由一个或多个区段组成，如表段、索引段都是段对象，当创建一个表时就创建一个表段。

区段(Extent):区段时段中分配的逻辑存储空间，一个区段由连续的Oracle数据库块组成，一个区段只能存在于一个数据文件中。当创建一个段时，该段至少包含一个区段，当段增长时，将分配更多的区段给该段，同时DBA可以手动地向该段中添加区段，如创建一个表时，就自动分配一定数量的区段。

数据库块(Oracle block):Oracle数据库管理存储空间中的数据文件的最小单位。一个数据库块由一个或多个操作系统块组成，且应当是操作系统数据块的整数倍，以避免IO。DB_BLOCK_SIZE一般为4K或8K，数据库一旦建立，该参数将无法修改。


```
show parameter db_block_size;

create table lgctest(
	id number, 
	name varchar2(20), 
	salary number
) tablespace users;

select * from user_segments where segment_name='lgctest';
```


####  segment 管理方式
1.	手动管理
```
pctfeee:表示数据块里剩余的可用空间占数据块总空间的百分比(default:10),用于insert/update
pctused:表示已经使用的空间占数据块总空间的百分比(default:40),用于delete
```

2.	自动管理
BMB(bitmap Block)
```
1.	多个BMB来管理，而不是一个链表，避免了单链表管理的争用问题；
2.	多个进程可以同时使用多个BMB进行并行的插入，避免了对seg header的争用；
```

```
create smallfile tablespace satbs
	datafile '/u01/app/Oracle/oradata/PROD/satbs.dbf' size 100m
	autoextend on next 1m maxsize unlimited logging
	segment space management auto
	extent management local uniform size 1m;

select * from dba_tablespaces;
```

#### 表空间磁盘管理
1.	数据字典管理
```
desc fet$;
desc uet$;
```

2.	本地管理

#### 表空间分类
1.	永久表空间
2.	临时表空间
3.	还原表空间


#### 创建表空间
1.	创建数据字典管理的表空间，放在不同的磁盘以及目录下，有利于平衡IO.
```
creare tablespace tj_data
	datafile 'd:\userdata\tj_data01.dbf' size 100M,
		'e:\userdata\tj_data02.dbf' size 100M,
		'f:\userdata\tj_data03.dbf' size 100M
	mininum extent 20k
	extent management dictionary
	default storage(initial 20k next 20k maxextent 500 pctincrease 0);
```

2.	创建本地管理的表空间
不能随意更改存储参数。
```
creare tablespace bj_data
	datafile 'd:\userdata\bj_data01.dbf' size 100M
	extent management local
	uniform size 1M;
```

3.	创建还原表空间
还原段中存放更改前的数据，保证读一致性。还原表空间中只能放还原段，不能存放其他任何对象。
创建还原表空间时，只能使用DATAFILE子句和EXTENT MANAGEMENT子句。
```
create undo tablespace user_undo
	datafile 'd:\userundo\unser_undo.dbf' size 30M;
```

4.	创建大文件表空间管理
只需要创建一个数据文件，大大减少了数据文件的数量，简化了数据文件的管理。
大文件表空间的容量比普通表空间要大得多，索引其存储能力显著提高。

创建数据库时设置大文件表空间且把它作为默认表空间
```
create database 
	set default bigfile tablespace tbs_name
		datafile 'd:\bigfile_tabs\tbs01.dbf' size 2G;
```

创建大文件表空间bigfiletbs
```
create bigfile tablespace bigfiletbs
	datafile 'd:\bigfile_tabs\tbs01.dbf' size 2G;
```

把数据库的默认表空间类型改为大文件表空间类型
```
alter tablespace set default bigfile tablespace
```

更改大文件表空间的大小
```
// 手动更改
alter tablespace bigfiletbs resize 4G;
// 自动扩展
alter tablespace bigfiletbs autoextend on next 1G;
```

创建非标准块表空间
```
1.	OLTP应用中，短小、小数据量的事务较多，建议使用较小的数据块(<8K)
2.	DSS或者数据仓库中，事务比较大，涉及的数据量也大，建议使用较大的数据块(16K/32K)
3.	其他混合型
```

```
show parameter db_block_size;

alter system set db_2k_cache_size=3m;
create tablespace test2k 
	datafile '/u01/app/Oracle/oradata/test2k.dbf' size 10m blocksize 2k;
```

### 表空间管理
读写(READ WRITE)
只读(READ ONLY)
离线(OFFLINE)

```
alter tablespace ex_tbs offline;

alter tablespace users read only;
select tablespace_name, status from dba_tablespaces;
select owner, tablespace_name, table_name from dba_tables where owner='SCOTT';

alter tablespace users read write;
```

### 表空间和数据文件管理
1.	表空间管理：修改表空间的大小，删除表空间以及修改表空间的存储参数等
2.	数据文件管理：修改数据文件的大小，删除表空间中的数据文件，迁移数据文件以及修改表空间的存储路径

#### 表空间管理
##### 表空间大小修改
1.	创建表空间时，使用AUTOEXTENT ON子句使其自动扩展
```
create tablespace ex1_tbs
	datafile 'd:\ex_tbs\ex1_tbs1.dbf' size 100M
	autoextend on;
```

2.	创建表空间后，使用ALTER DATABASE DATAFILE file_name AUTOEXTENT ON修改不能自动扩展的表空间的数据文件。
```
create tablespace ex2_tbs
	datafile 'd:\ex_tbs\ex2_tbs1.dbf' size 100M
	uniform size 1M;

select * from dba_files;

alter database datafile 'd:\ex_tbs\ex2_tbs1.dbf' autoextend on next 1M;
```

3.	在表空间中增加数据文件
```
create tablespace ex3_tbs
	datafile 'd:\ex_tbs\ex3_tbs1.dbf' size 100M
	uniform size 1M;

select * from dba_files;

alter tablespace ex2_tbs add datafile 'd:\ex_tbs\ex3_tbs2.dbf' size 50M;

select * from dba_data_files where tablespace_name='ex3_tbs';
```

4.	修改数据文件的大小，即重新设置表空间中耨个数据文件的大小
```
create tablespace ex4_tbs
	datafile 'd:\ex_tbs\ex4_tbs1.dbf' size 100M
	uniform size 1M;

alter database datafile 'd:\ex_tbs\ex4_tbs1.dbf' resize 500M;

select * from dba_data_files where tablespace_name='ex4_tbs';
```
