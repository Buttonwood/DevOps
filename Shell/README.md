### 1.基础篇



### 2.使用篇
#### 2.1 统计端口使用量
```
netstat -anop |grep -v 10050 |grep -v 1521 |grep tcp | \
awk '{print $4;}' |awk -F ":" '{print $NF;}' |sort |uniq -c |awk '$1>1'
```

#### 2.2 文件修改时间
```
ls *.sh |xargs stat -c %Y
 #
ls *.sh |xargs stat -c %y
```
