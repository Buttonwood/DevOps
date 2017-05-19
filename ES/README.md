##### 1.    免密码登录
```
#@jp01
ssh-keygen -t rsa
cd ~/.ssh
cat id_rsa.pub >>authorized_keys &&  chmod 600 authorized_keys
```

##### 2.    基础依赖

```
#@jp01-05
yum -y install wget git vim zsh && \
chsh -s /bin/zsh && \
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
scp -r jp01:~/.ssh ~
```

#### 3.    hostname 
```
#@jp01-05
cat << EOF
172.16.18.161 jp01 jp01.test.com
172.16.18.162 jp02 jp02.test.com
172.16.18.163 jp03 jp03.test.com 
172.16.18.164 jp04 jp04.test.com
172.16.18.165 jp05 jp05.test.com 
EOF >> /etc/hosts
```


##### 5. es

*    新增es用户
   
```
groupadd es && useradd es -g es -p es
chown -R es:es /usr/share/elasticsearch-5.4.0/
mkdir -p /data/es
chown -R es:es /data/es
```

*    系统优化

```
cat << EOF
* soft nofile 65555
* hard nofile 65555
EOF >> /etc/security/limits.conf


vim /etc/security/limits.d/90-nproc.conf
*          soft    nproc     unlimited
root       soft    nproc     unlimited

sysctl -w vm.max_map_count=262144 && sysctl -p /etc/sysctl.conf
```

*    启动

```
$ grep -v "#" /usr/share/elasticsearch-5.4.0/config/elasticsearch.yml|sed '/^$/d'
cluster.name: ES_app
node.name: jp05
path.data: /data/es/data
path.logs: /data/es/logs
bootstrap.memory_lock: false
bootstrap.system_call_filter: false
http.cors.enabled: true
http.cors.allow-origin: "*"
network.host: "0.0.0.0"
discovery.zen.minimum_master_nodes: 3
discovery.zen.ping.unicast.hosts: ["jp01","jp02","jp03","jp04","jp05"]

$ su es
/usr/share/elasticsearch-5.4.0/bin/elasticsearch -d
tail /data/es/logs/ES_app.log
```

##### References
http://www.cnblogs.com/jstarseven/p/6803054.html
