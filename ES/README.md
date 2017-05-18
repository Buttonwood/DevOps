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

```
groupadd es && useradd es -g es -p es
chown -R es:es /usr/share/elasticsearch-5.4.0/
mkdir -p /data/es
chown -R es:es /data/es
su es

```

vi /etc/security/limits.conf
