```
set arraysize 5000;  --此参数可提高SPOOL卸载的速度，最大可以设置为5000--

set autotrace on;    --设置允许对执行的sql进行分析--

set colsep ',';　　　--域输出分隔符--

set echo off;　　　　--显示start启动的脚本中的每个sql命令，缺省为on--

set feedback off;　　--回显本次sql命令处理的记录条数，缺省为on，设置显示“已选择XX行”--

set heading off;　　 --输出域标题，字段的名称，缺省为on--

SET LINESIZE 2500;   
--每行允许的最大字符数，设置大些，免得数据被截断，但不宜过大，太大会大大降低导出的速度(注意必须与trimspool结合使用防止导出的文本有太多的尾部空格)--

set newpage 1;       
--设置页与页之间的分隔{1|n|NONE};当值为0时在每页开头有一个小的黑方框;当值为n时在页和页之间隔着n个空行;当为none时，会在页和页之间没有任何间隔；--

set newp none;       --设置查询出来的数据分多少页显示，如果需要连续的数据，中间不要出现空行就把newp设置为none，这样输出的数据行都是连续的，中间没有空行之类的--

set num 18;          --设置数字的长度，如果不够大，则用科学记数法显示--

set numwidth 12;　   --输出number类型域长度，缺省为10--

SET NULL text;       --显示时,用text值代替NULL值--

set pagesize 2000;　 --输出每页行数，页面大小，缺省为24,为了避免分页，可设定为0--

set serveroutput on; --设置允许显示输出类似dbms_output;--编写存储过程时,大多会将必要的信息输出；--

SET SPACE 0;

set term off;        --不在屏幕上输出执行结果--

set termout off;　　 --显示脚本中的命令的执行结果，缺省为on--

set timing on;       --显示每个sql语句花费的执行时间，设置显示“已用时间：XXXX”--

set trimout on;　　　--去除标准输出每行的拖尾空格，缺省为off--

set trimspool on;　　--去除重定向（spool）输出每行的拖尾空格，缺省为off--

set verify off       --是否显示替代变量被替代前后的语句--

SET wrap on;         --输出行长度大于设置行长度时(用set linesize n命令设置);值为on时,多余的字符另起一行显示,否则多余的字符将被切除，不予显示；--

--set markup html on;--
spool格式
spool d:/tables.csv    --指定输出文件--

--也可以是 tables.html  或者 tables.xls ，但如果是html格式，要设置set markup html on  --

--  @d:/get_tables.sql      执行get_tables.sql文件,sql后缀默认可以不要--

select '"' || empno || '" ,"' || ename || '" ,"' || job || '","' || mgr || '","' || hiredate || '","' || sal || '","' || comm || '","' || deptno || '""'         
--指定SQL语句，如果是多个SQL语句的话，则要把语句写入一个sql文件，用@(绝对路径)sql文件名去执行，否则执行spool导出命令的话，sql语句也会写到输出文件去--

from scott.emp;   ---分隔为 ，用||连接字符和， ,--

spool off

exit

```

### References
* http://blog.itpub.net/29874114/viewspace-1679895/
