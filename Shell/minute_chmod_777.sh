#!/bin/bash
function jod(){
    if [ ! -d $1 ];then
        echo "mkdir -p $1 && chmod 777 $1"
        mkdir -p $1 && chmod 777 $1
    fi
    RT=`ls -ld $(dirname $1)|awk '{print $1}'`
    if [ $RT != 'drwxrwxrwx' ];then
        echo  "chmod 777 $(dirname $1)"
        chmod 777 $(dirname $1)
    fi
}
 
PREFIX='/home/tanhao/devops/tmp'
T=`date -d "1 minute" +"%Y/%m/%d/%H/%M" |sed 's#/0#/#g'|awk 'BEGIN{FS="/";OFS=" "}{print $1,$2,$3,$4,$5;}'`
for i in $T ;do
    PREFIX=${PREFIX}/${i}
    jod $PREFIX
done
 
