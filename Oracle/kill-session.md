### step 1
```
// pid
top 
```

### step 2
```
--select * from gv$process;
--select * from gv$session;
--select * from gv$sql;

select * from gv$process p, gv$session s
where p.ADDR = s.PADDR
and p.SPID = '51990';

select * from gv$sql s where s.ADDRESS='00000077C2F4AFD0';
```

```
select s.username, s.osuser, s.sid, s.serial#, p.spid
  from v$session s, v$process p
 where s.paddr = p.addr
   and s.username is not null;

select 'alter system kill session ',
       '''' || trim(t2.sid) || ',' || trim(t2.serial#) || ''';'
  from v$locked_object t1, v$session t2
 where t1.session_id = t2.sid
 order by t2.logon_time;
```

### References
* https://www.cnblogs.com/kerrycode/p/4034231.html
