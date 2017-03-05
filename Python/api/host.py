import paramiko
import time

class Host(object):
	"""docstring for Host"""
	def __init__(self, host, user, passwd):
		super(Host, self).__init__()
		self.host = host
		self.user = user
		self.passwd = passwd
		self.ssh = paramiko.SSHClient()
		self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		self.ssh.connect(self.host, 22, self.user, self.passwd)

	def os(self):
		cmd = "if [[ -f /etc/redhat-release ]];then \
OS=$(cat /etc/redhat-release |sed 's/^[ \t]*//g'); \
elif [[ -f /usr/bin/lsb_release ]];then \
OS=$(/usr/bin/lsb_release -a |grep Description |awk -F : '{print $2}' |sed 's/^[ \t]*//g');\
else \
OS=$(cat /etc/issue |sed -n '1p');\
fi;\
echo $OS;uptime|sed 's/\([0-9]\),\([0-9]\)/\\1.\\2/g'"
		return self.cmd(cmd)

	def cpu(self):
		cmd = "grep 'processor' /proc/cpuinfo |sort |uniq |wc -l;grep 'physical id' /proc/cpuinfo |sort |uniq |wc -l;top -b -n 1 |grep Cpu | awk '{print $8}'|sed 's/,/./g'"
		#cmd = "grep 'physical id' /proc/cpuinfo |sort |uniq |wc -l"
		return self.cmd(cmd)

	def processor(self):
		cmd = "grep 'processor' /proc/cpuinfo |sort |uniq |wc -l"
		return self.cmd(cmd)

	def memory(self):
		cmd = "cat /proc/meminfo |grep '^Mem' |awk -F : '{print $2}' |sed 's/^[ \t]*//g'"
		#cmd = "cat /proc/meminfo |grep 'MemTotal' |awk -F : '{print $2}' |sed 's/^[ \t]*//g'"
		return self.cmd(cmd)

	def disks(self):
		cmd = "df -hP|awk 'NR>1 {print $1,$2,$3,$4,$5,$6;}' OFS='|'|sed 's/,/./g'"
		#cmd = "df -hP|awk 'NR>1 {print $1,$2,$3,$4,$5,$6;}' OFS='|' |sed ':a;N;$!ba;s/\n/,/g'"
		return self.cmd(cmd)

	def cmd(self, cmd):
		stdin, stdout, stderr = self.ssh.exec_command(cmd)
		return {dst():[line.strip('\n') for line in stdout.readlines()]}

	def __del__(self):
		self.ssh.close()


def dst():
	return int(time.time())

def main():
	import json
	host = Host("10.0.2.15",'vagrant','vagrant')
	print(json.dumps(host.disks(),indent=4))
	print(json.dumps(host.os(),indent=4))
	print(json.dumps(host.memory(),indent=4))
	#print(host.processor())
	print(json.dumps(host.cpu(),indent=4))

if __name__ == '__main__':
	main()
