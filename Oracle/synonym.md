```
-- 授权(ulimprd to ulimapp)
grant select,insert,update on t_ulim_access_exception_log to ulimapp;
grant select,insert,update on t_ulim_access_log to ulimapp;
grant select,insert,update on t_ulim_access_ing_log to ulimapp;
grant select,insert,update on t_ulim_flush_log to ulimapp;

grant select on s_ulim_access_exception_id  to ulimapp;
grant select on s_ulim_access_log_id  to ulimapp;
grant select on s_ulic_access_ing_id  to ulimapp;
grant select on s_ulim_flush_log_id  to ulimapp;

-- 授权确认(ulimapp)
select * from  ulimprd.t_ulim_access_exception_log;
select * from ulimprd.t_ulim_access_log;
select * from ulimprd.t_ulim_access_ing_log;
select * from ulimprd.t_ulim_flush_log ;

select ulimprd.s_ulim_access_exception_id.nextval  from dual;
select ulimprd.s_ulim_access_log_id.nextval  from dual;
select ulimprd.s_ulic_access_ing_id.nextval  from dual;
select ulimprd.s_ulim_flush_log_id.nextval  from dual;

-- 同义词创建(ulimprd to ulimapp)
create public synonym ulimapp.t_ulim_access_exception_log for ulimprd.t_ulim_access_exception_log
create public synonym ulimapp.t_ulim_access_log for ulimprd.t_ulim_access_log
create public synonym ulimapp.t_ulim_access_ing_log for ulimprd.t_ulim_access_ing_log
create public synonym ulimapp.t_ulim_flush_log for ulimprd.t_ulim_flush_log


create public synonym ulimapp.s_ulim_access_exception_id for ulimprd.s_ulim_access_exception_id
create public synonym ulimapp.s_ulim_access_log_id for ulimprd.s_ulim_access_log_id
create public synonym ulimapp.s_ulic_access_ing_id for ulimprd.s_ulic_access_ing_id
create public synonym ulimapp.s_ulim_flush_log_id for ulimprd.s_ulim_flush_log_id

-- 同义词确认(ulimapp) 
select * from t_ulim_access_exception_log;
select * from t_ulim_access_log;
select * from t_ulim_access_ing_log;
select * from t_ulim_flush_log ;

select s_ulim_access_exception_id.nextval  from dual;
select s_ulim_access_log_id.nextval  from dual;
select s_ulic_access_ing_id.nextval  from dual;
select s_ulim_flush_log_id.nextval  from dual;
```
