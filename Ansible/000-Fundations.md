### Ansible
*	ansible
*	core modules(command, shell, scripts, copy, file, ping, setup)
* 	host inventory
*  custom modules
*  playbooks
*  connection plugins

```
yum install ansible
yum remove ansible

/etc/ansible/ansible.cfg
/etc/ansible/hosts
/etc/ansible/roles

ansible
ansible-config
ansible-doc
ansible-galaxy
ansible-inventory
ansible-playbook
ansible-pull
ansible-vault
ansible-console
```

```
// -m command; 不支持管道
ansible -i ./hosts all -a 'pwd'

// -m shell
ansible -i ./hosts all -m shell -a 'pwd | grep a'

// -m scripts
ansible -i ./hosts all -m scripts -a '~/sss.sh'

// -m copy
ansible -i ./hosts all -m copy -a 'src=... dest=... owner=root group=root mode=644"
	
// -m setup 用于查看远程服务器的基本信息。
ansible -i ./hosts all -m setup
	
// -m ping 用于查看远程服务器的运行状态。
ansible -i ./hosts all -m ping
	
// -m file 用于操作远程服务器上的文件。
ansible -i ./hosts all -m file
```

```
vim hosts
192.168.100.100 ansible_ssh_pass=***
192.168.100.101 ansible_ssh_pass=***

[group1]
192.168.0.2
www.example.com
www[01:50].example.com
db-[a:f].example.com

[group2]
10.18.16.20 k1=v1 k2=v2
10.18.16.21 k1=v1 k2=v2

[group3:vars]
ansible_ssh_user=root
k1=v1
k2=v2
```

```
ansible server|group -m copy -a 'content="hello" dest=/tmp/hello.txt'

ansible-doc -l
ansible-doc -s copy
```

### Modules
```
// -m command
ansible servers -a 'date'

// ping
// command
// shell
// scripts
// yum
// service
// pip
// copy
// user
// group
// get_url
// file
// template
// unarchive

ansible servers -m yum -a "name=docker state=latest skip_broken=yes"
ansible servers -m copy -a "src=/etc/docker/daemon.json dest=/etc/docker/daemon.json"
ansible servers -m service -a "name=docker state=started enabled=yes"
```

### playbook
```
vim docker.yml
---
- hosts: servers
  remote_user: root
  tasks:
  	 - name: ensure docker is at the latest version
       yum: name=docker state=latest skip_broken=yes
  	 - name: config docker daemon
  	   copy: src=/etc/docker/daemon.json dest=/etc/docker/daemon.json
  notify:
  	 - retstart docker
  	 - name: ensure docker is running
  	   service: name=docker state=started
  handlers:
  	 - name: restart docker
  	   service: name=httpd state=restarted
  	   
ansible-playbook docker.yml
```

#### playbook Roles
![](https://pic3.zhimg.com/80/v2-e42f7797ff906da041f70d214723397a_hd.jpg)

![](https://pic3.zhimg.com/80/v2-ebc9a33f12ca2f25ed694e3594fa8cce_hd.jpg)

![](https://pic2.zhimg.com/80/v2-5f634600e32a54c36570e426afdf5745_hd.jpg)

![](https://pic1.zhimg.com/80/v2-6bf1cb89ae9959aa4d929563588e7a50_hd.jpg)

![](https://pic1.zhimg.com/80/v2-80450ffee5a76326e36ccbda5f8b9118_hd.jpg)

![](https://pic3.zhimg.com/80/v2-1cf44ee9887fad1bae73b435e076c0a6_hd.jpg)

![](https://pic2.zhimg.com/80/v2-da7a2fd26b946f0d59156ceb8fe91875_hd.jpg)

#### playbook tags
![](https://pic1.zhimg.com/80/v2-5714941b8b4de57ce84e93e07f45a308_hd.jpg)

#### playbook block
![](https://pic2.zhimg.com/80/v2-45ea9ba168cda5c76b14681bc1fe43b1_hd.jpg)
