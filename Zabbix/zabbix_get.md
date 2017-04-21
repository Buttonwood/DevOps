#### ip
```
ifconfig |grep "inet addr" |grep Bcast |awk '{print $2;}'|cut -d ":" -f 2
```

#### grep
```
zgrep -a  -C 1 INCLUDE Python-3.6.0.tgz |less
```

#### Server side
```
/ulic/zabbix/zabbix/bin/zabbix_get -s 192.168.8.143 -k "system.cpu.util[,idle]"
/ulic/zabbix/zabbix/bin/zabbix_get -s 192.168.8.143 -k vfs.fs.discovery|python -m json.tool
/ulic/zabbix/zabbix/bin/zabbix_get  -s 192.168.132.62 -k system.uname
/ulic/zabbix/zabbix/bin/zabbix_get  -s 192.168.132.62 -k "vfs.fs.size[/share]"
/ulic/zabbix/zabbix/bin/zabbix_get  -s 192.168.132.62 -k "vfs.fs.size[/share,pfree]"

zabbix_get -s 127.0.0.1 -k vfs.fs.discovery

zabbix_get -s 192.168.3.5 -k vfs.fs.size[/ulic/newoutentrys/healthlink,pfree]

zabbix_get -s 192.168.3.5 -p 10050 -I 192.168.8.64 -k "proc.mem[,,,com.ulic.life.newbiz.jms.OnlineAnswerReceiveBatch]"

zabbix_get -s 192.168.3.5 -p 10050 -I 192.168.8.64 -k "proc.num[,,,BatchServer]"

zabbix_get -s 192.168.3.5 -p 10050 -I 192.168.8.64 -k "proc.num[,,,com.ulic.life.newbiz.jms.OnlineAnswerReceiveBatch]"
```

#### Agent side
```
./zabbix_agentd -t proc.num[,,,tomcat]

zabbix_agentd -t net.tcp.port[192.168.3.5,10050]

../sbin/zabbix_agentd  -t vfs.fs.discovery
```
