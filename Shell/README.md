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

```
file_a=$1
file_b=$2
s1=`stat -t $file_a |awk '{print $2;}'`
s2=`stat -t $file_b |awk '{print $2;}'`
t1=`stat -t $file_a |awk '{print $(NF-2);}'`
t2=`stat -t $file_b |awk '{print $(NF-2);}'`

if [ $t1 -eq $t2 ] & [ $s1 -eq $s2 ];then 
	echo "the same"
else
	echo "$t1 $t2"
	echo "$s1 $s2"
fi

find /home/weblogic/update/ -type f |while read aa;do echo "stat -t $aa|awk '{print \$(NF-2)\"@\"\$2\"@\"\$1;}'";done |sh
```

#### 2.3 获取挂载盘
```
OUT=`df -hP|sed '/^Filesystem/d'|awk '{print $(NF-1)"@"$NF"@"$1;}'|sed ':a;N;$!ba;s/\n/|/g'`
OUT=`df -hP|sed '/^Filesystem/d'|grep "$1$"|awk '{print $(NF-1)"@"$NF"@"$1;}'|sed ':a;N;$!ba;s/\n/|/g'`
```

##### 2.3.1 生成挂载文件表格
```
df -PTh | column -t| sort -n -k6n|awk 'BEGIN{print "<html><body><table border=1>"} {print "<tr>";for(i=1;i<=NF;i++)print "<td><font color='#00000'>" $i"</td></font>";print "</tr>"} END{print "</table></body></html>"}' |sed -e '10d' >disks.html
```


#### 2.4  windows生成批量重命名脚本
```
@echo off
set INDIR=E:\tanhao\test
set TODIR=E:\tanhao\test
dir /b/s/a:-D %INDIR% |find "\_" > %TODIR%\list.txt
setlocal enabledelayedexpansion
for /f "tokens=1,2* delims=" %%i in (%TODIR%\list.txt) do (
	set name=%%~ni
	echo !name!
	echo !name:~1!
	echo ren %%~fi !name:~1!%%~xi >> %TODIR%\rname.bat
)
pause
```

```
@echo off
set INDIR=E:\tanhao\test
set TODIR=E:\tanhao\test
dir /b/s/a:-D %INDIR% |find "\_" > %TODIR%\list.txt
if exist %TODIR%\file2.txt del %TODIR%\file2.txt
for /f "tokens=1,2* delims=" %%i in (%TODIR%\list.txt) do (
	(@echo %%i) > %TODIR%\file1.txt
	for /f "tokens=3,4* delims=\" %%a in (%TODIR%\file1.txt) do (
		echo %%~fi
		set "NAME=%%~ni"
		echo %NAME%
		echo !NAME!
		echo %NAME:~1%
		echo %%~xi
		(@echo ren %%i %var%) >> %TODIR%\file2.txt
		(@echo ren %%i %%b) >> %TODIR%\file2.txt
    )
)
pause
```

windows 截取字符串
```
@echo off
set str=_123456789
echo %str%
set str=%str:~1%
echo %str%
set str=%str:~1,4%
echo %str%
pause
```

文件查找
```
@echo off
dir /b/s/a:-D E:\tanhao\test |find "_" > E:\tanhao\test\file1.txt
findstr "\_" E:\tanhao\test\file1.txt > E:\tanhao\test\file2.txt
for /f "delims='\' tokens=2,3*" %%a in (E:\tanhao\test\file1.txt) do (
        (@echo %%a) >> E:\tanhao\test\output.txt
        (@echo %%b) >> E:\tanhao\test\output.txt
        (@echo %%c) >> E:\tanhao\test\output.txt
        (@echo %%d) >> E:\tanhao\test\output.txt
)
```

进程检查
```
@echo off
tasklist /nh|find /i "chrome.exe" /c
exit
```
