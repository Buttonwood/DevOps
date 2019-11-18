```
// login shell
/etc/profile --> /etc/profile.d/*.sh --> ~/.bash_profile --> ~/.bashrc  --> /etc/bash 
```

```
// non-login shell
~/.bashrc --> /etc/bashrc --> /etc/profile.d/*.sh
```

```
ps -ejH
ps -exjf
ps -ef --forest
pstree
pstree -n
pstree -a
pstree -g

tree /proc
tree -d /proc
tree -f /proc
```

### References
*	Bash Guide for Beginners
