### 1.基础篇



### 2.使用篇
#### 2.1 统计端口使用量
```
$ netstat -anop |grep -v 10050 |grep -v 1521 |grep tcp |awk '{print $4;}' |awk -F ":" '{print $NF;}' |sort |uniq -c |awk '$1>1'
```
