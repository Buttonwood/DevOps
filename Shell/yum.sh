yum repolist all
yum clean all
yum clean metadata
yum clean dbcache

rpm -qa |grep -i repo-name
rpm -e repo-name
