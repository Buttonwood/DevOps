#!/bin/bash
if [ $# != 1 ];then
        echo "sh pid_info.sh program_name"
        exit
fi

CWD=`dirname $0`
#echo $CWD
#PRO="zabbix"
PRO=$1
NT=`date`
NTM=`date +%s -d "$NT"`
#RTVAL=''
#echo "ps aux|grep $PRO"
if [ ! -z $PRO ];then
        `ps aux|grep $PRO|grep -v "grep" |grep -v "pid_info"|awk '{print $2"@"$3"@"$4;}'  2>&1 >${CWD}/pid_info.txt`
        rm -rf ${CWD}/pid_info2.txt

        while read aa;do
                PID=`echo $aa|awk -F "@" '{print $1;}'`
                if [ ! -z $PID ];then
                        ST=`ps -p $PID -o lstart|grep -v STARTED`
                        STM=`date +%s -d "$ST"`
                        G=`expr $NTM - $STM`
                        echo "${aa}@${STM}@${G}" >> ${CWD}/pid_info2.txt
                fi
        done < ${CWD}/pid_info.txt

        if [ -s "${CWD}/pid_info2.txt" ];then
                RTVAL=`cat ${CWD}/pid_info2.txt |sed ':a;N;$!ba;s/\n/|/g'`
                #echo "\"${RTVAL}\""
                echo $RTVAL
        fi
        #rm -rf ${CWD}/pid_info.txt ${CWD}/pid_info2.txt
fi
#echo "\"${RTVAL}\""
