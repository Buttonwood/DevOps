### RAID0
![](https://img-blog.csdn.net/20160616205153489)

*   以条带的形式将数据均匀分布在阵列的各个盘上
*   磁盘数目： >= 2 
*   特点: 读、写性能提升，不存在校验，不会占太多cpu资源，设计、使用和配置比较简单； 
*   缺点: 无冗错能力，不能用于对数据安全性要求高的环境；
*   可用空间： N * min(s1, s2 ... 取决于最小的硬盘的空间)
*   适用领域：视频生成和编辑、图形编辑，其它需要大的传输带宽的操作；


### RAID1(Mirror, 镜像卷)
![](https://img-blog.csdn.net/20160616205236475)

*   以镜像为冗余方式，对虚拟磁盘上的数据做多份拷贝，放在成员磁盘上
*   磁盘数：最低2个，2n(n >= 1)个
*   优点：读性能提升、写性能略有下降，具有100%数据冗余，提供最高的数据安全保障理论上可实现2倍的读取效率设计和使用较简单； 
*   缺点：开销大，空间利用率只有50%，在写性能方面提示不大； 有冗余能力 
*   可用空间：1*min（S1，S2…由最小硬盘的空间决定） 
*   适用领域：财务、金融等高可用、高安全的数据存储环境；

### RAID4
![](https://img-blog.csdn.net/20160616205319714)

*   数据都是依次存储在多个硬盘之上，独立的一个硬盘做冗余备份上，容错能力得到了得升。但是独立的硬盘盘访问压力较大，存在性能瓶颈。第3个磁盘存储检验码。
*   优点：有着性能和冗余的均衡考虑。 
*   缺点：固定的冗余盘成为磁盘阵列I/O瓶颈。 
*   最少需要3块硬盘； 数据交叉存储在2块硬盘中，再由第3块硬盘存储数据的校验码； 校验码是由2块硬盘中的chunk块按位进行异或运算后的值而得； 其中1块硬盘坏了不影响文件数据读写操作，数据还可以恢复，但就是有些慢；即使坏了1块硬盘仍然继续在线工作时，称为降级模式，此时数据没有保障，风险较大；所以要马上用新硬盘替换坏硬盘，暂定业务，用2块可用盘进行计算，按位校验恢复数据到新硬盘即可，当所有数据都恢复到新硬盘后，就能继续正常工作了；但是万一在恢复过程中也是有风险的； 
*   RAID4还有一个固有缺点：用单块盘作为存放校验码，无论前面哪块盘访问数据，校验盘都得被访问；即集中存放校验码的校验盘访问压力过大，很容易造成性能瓶颈；所以，尽早发现坏盘损坏，就能尽早更换；可以在接1块新硬盘当做空闲备用盘。

### RAID5
![](https://img-blog.csdn.net/20160616205353227)

*   采用独立存取的阵列方式，校验信息被均匀的分散到阵列的各个磁盘上； 相对于RAID-4把校验码存放在一块硬盘上，而RAID-5是将3块盘循环轮流作存放校验码。左对称即校验码存放各盘的顺序是先在前2块盘存数据，第3块盘存校验码，依次类推，右对称相反
*   磁盘数：最低3个 
*   优点：读性能较高，中等的写性能，校验信息的分布方式存取，避免出现写操作的瓶颈； 
*   缺点：控制器设计复杂，磁盘重建的过程比较复杂； 
*   可用空间：（N-1）*min（S1，S2，…其中的最小空间） 
*   有容错能力：1块磁盘 
*   适用领域：文件服务器、email服务器、web服务器等环境，数据库应用；

### RAID6
![](https://img-blog.csdn.net/20160616205428324)

*   在RAID-5的基础上增加了一个校验码，大大提高了冗余性能。/两块盘做校验盘，校验码存2次，很少用/ 

### RAID10
![](https://img-blog.csdn.net/20160616205511807)

*   RAID10结合RAID1和RAID0，先镜像，再条带化 
*   磁盘数：最低4个，2n个，n大于等于2； 
*   优点：读性能很高，写性能比较好，数据安全性好，允许同时有N个磁盘失效； 
*   缺点：利用率只有50%，开销大； 
*   可用空间：N*min（S1，S2，…其中最小空间）/2； 
*   有容错能力：每组镜像最多只能坏一块； 
*   适用领域：多用于要求高可用性和高安全性的数据库应用；

### RAID01
*   先分成两组做成RAID-0，再把组成的RAID-0做成RAID-1；不符合常用方法，每一组有一块坏的硬盘可能性大；

### RAID50
![](https://img-blog.csdn.net/20160616205535120)

*   是RAID5和RAID0的结合，先实现RAID5，再条带化；（先做RAID-5在做RAID-0，最少6块盘，每组允许坏1块盘，空间利用率灵活）、RAID7（某家公司的私有技术，实际是文件服务器） 
*   磁盘数：最低6个； 
*   优点：比RAID5有更好的读性能，比相同容量的RAID5重建时间更短，可以容许N个磁盘同时失效； 
*   缺点：设计复杂，比较难实现；同一个RAID5组内的两个磁盘失效会导致整个阵列失效； 
*   适用领域：大型数据库服务器、应用服务器、文件服务器等应用；

### JBOD(Just a Bunch ofDisks)
*   将多块磁盘空间合并成一个大的连续空间使用；可用空间：sum（S1+S2+，…磁盘空间之和）


### Summary
RAID|访问速度|数据可靠性|磁盘利用率|最低磁盘数目|原理|使用场景
---|---|---|---|---|---|---
RAID0|很快|很低|100%|2|将数据分成N份，这些数据同时并发写入N块磁盘|HDFS，视频生成和编辑、图形编辑，其它需要大的传输带宽的操作
RAID1|很慢|极高|50%|2n(n >= 1)|以镜像为冗余方式，对虚拟磁盘上的数据做多份拷贝，放在成员磁盘上|财务、金融等高可用、高安全的数据存储环境
RAID10|中等|很高|50%|2n(n>=2)|先镜像(RAID1)，再条带化(RADI0),每组镜像最多只能坏一块|多用于要求高可用性和高安全性的数据库应用
RAID01|---|---|50%|2n(n>=2)|先分成两组做成RAID-0，再把组成的RAID-0做成RAID-1|不符合常用方法
RAID4|较慢|较高|(N-1)/N|3|RAID-4把校验码存放在一块硬盘上|校验盘总是被读写，成为性能瓶颈
RAID5|较快|较高|(N-1)/N|3|RAID-5是将3块盘循环轮流作存放校验码。左对称即校验码存放各盘的顺序是先在前2块盘存数据，第3块盘存校验码，依次类推，右对称相反|文件服务器、email服务器、web服务器等环境，数据库应用
RAID6|较快|较(RAID5)高|(N-2/N)|3|在RAID-5的基础上增加了一个校验码，大大提高了冗余性能|
RAID50|很快|很低|(N-1)/N|2*3n(n>=1)|先做RAID-5再做RAID-0，最少6块盘，每组允许坏1块盘，空间利用率灵活|大型数据库服务器、应用服务器、文件服务器等应用；



### References
*   https://blog.csdn.net/song0156/article/details/51694613
