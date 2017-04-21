#### 好处
1.	分区级(partition level)进行数据加载、索引创建及重建、或备份恢复等数据管理操作，而非整个表上。
2.	提高查询性能
3.	缩短维护时间
4.	分区独立操作
5.	提高可用性
6.	代码逻辑并不改变


#### 分类
根据分区键自动选择分区，支持插入、更新及删除等操作。
分区键：
1.	1-16个数据列顺序构成
2.	不能包含LEVEL、ROWID或MLSLABEL虚列(pseudocolumn)，也不能包含类型为ROWID的列
3.	不能包含可为空(NULL)的列

一个表最多由1024K-1个分区构成。任何表都能够被分区。可采用压缩形式存储表及分区表。


##### 1.	范围分区
```
CREATE TABLE ex1(
	range_key_column date,
	data varchar2(20)
)	PARTITION BY RANGE (range_key_column) //指定分区键
(
	PARTITION p1 VALUES LESS THEN (to_date('01/01/2015','dd/mm/yyyy')),
 	PARTITION p2 VALUES LESS THEN (to_date('01/01/2016','dd/mm/yyyy')),
 	PARTITION p1 VALUES LESS THEN (MAXVALUE)
);

select table_name,partitioning_type,partition_count,status from user_part_tables where table_name='ex1'

select table_name,partition_name,tablespace_name from user_tab_partitions where table_name='ex1'
```

也可以将子分区放在不同的表空间下，对于减少IO争用有好处。


2.	列表分区
根据离散的值列表来指定一行位于哪个分区。

```
CREATE TABLE ex2(
	state_name varchar2(20),
	data varchar2(20)
) PARTITION BY LIST(state_name)(
	PARTITION p1 values ('New York','Virginia'),
	PARTITION p2 values ('California','Oregon'),
	PARTITION p3 values ('Illionis','Texas')
);

select * from ex2 partition(p1);

alter table ex2 add partition p4 values(default);
// 一旦列表分区中有一个default分区，就不能再向这个表中增加更多的分区了。此时必须先删除default分区，添加新分区后再加回default分区。
```

3.	哈希分区
散列分区是为了能使数据更好地分布在多个不同设备或磁盘上，为表选择的散列键应当是唯一的一个列或一组列，或者至少有足够多的相异值。

```
CREATE TABLE ex3(
	hash_key date,
	data varchar2(20)
) PARTITION BY HASH(hash_key)(
	PARTITION p1 tablespace tbs1,
	PARTITION p2 tablespace tbs2,
	PARTITION p3 tablespace tbs3,
	PARTITION p4 tablespace tbs4
);

// 散列分区，无法控制数据行最终放在哪个分区中
// 改变分区个数，数据会在所有分区中重新分布，向一个散列中增加或删除一个分区时，将导致所有数据都重写 
// 分区数应该是2的幂数，尽量保证数据均匀分布
/
```

4.	组合分区
上层是区间分区，下层可能是散列或列表分区。

```
CREATE TABLE ex4(
	range_key date,
	hash_key int,
	data varchar2(20)
)
	PARTITION BY RANGE(hash_key)
	SUBPARTITION BY HASH(hash_key) subpartitions 2
(
	PARTITION p1 VALUES LESS THEN (to_date('01/01/2015','dd/mm/yyyy'))(
		SUBPARTITION p1s1,
		SUBPARTITION p1s2
	)
 	PARTITION p2 VALUES LESS THEN (to_date('01/01/2016','dd/mm/yyyy'))(
 		SUBPARTITION p2s1,
		SUBPARTITION p2s2
 	)
);
```


分区键修改导致行跨分区移动(启用行移动，不要太频繁)
```
select rowid from ex1 where range_key = to_date('31-Dec-2014','dd-mon-yyyy');
alter table ex1 enable row movement;
update ex1 sed range_key=to_date('31-Dec-2016','dd-mon-yyyy') where range_key= to_date('31-Dec-2014','dd-mon-yyyy');
```

### 
Learn Oracle from  Oracle Certified Master



pctfree
pctused

manageability
availability
