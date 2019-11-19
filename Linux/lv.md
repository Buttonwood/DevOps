### vCenter
```
ls  /sys/class/scsi_host/ |sort |awk '{print "echo \"- - -\" >/sys/class/scsi_host/"$1"/scan";}' |sh
```

### fdisk
*  VM物理磁盘扩容，先物理盘扩容，再加到lv组
*  挂盘也可以参考。

```
[root@cdh04 ~]# fdisk /dev/sda
Welcome to fdisk (util-linux 2.23.2).

Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.


Command (m for help): m
Command action
   a   toggle a bootable flag
   b   edit bsd disklabel
   c   toggle the dos compatibility flag
   d   delete a partition
   g   create a new empty GPT partition table
   G   create an IRIX (SGI) partition table
   l   list known partition types
   m   print this menu
   n   add a new partition
   o   create a new empty DOS partition table
   p   print the partition table
   q   quit without saving changes
   s   create a new empty Sun disklabel
   t   change a partition's system id
   u   change display/entry units
   v   verify the partition table
   w   write table to disk and exit
   x   extra functionality (experts only)

Command (m for help): n
Partition type:
   p   primary (3 primary, 0 extended, 1 free)
   e   extended
Select (default e): p
Selected partition 4
First sector (125829120-167772159, default 125829120):
Using default value 125829120
Last sector, +sectors or +size{K,M,G} (125829120-167772159, default 167772159):
Using default value 167772159
Partition 4 of type Linux and of size 20 GiB is set

Command (m for help): w
The partition table has been altered!

Calling ioctl() to re-read partition table.

WARNING: Re-reading the partition table failed with error 16: Device or resource busy.
The kernel still uses the old table. The new table will be used at
the next reboot or after you run partprobe(8) or kpartx(8)
Syncing disks.
```

```
reboot
fdisk /dev/sdc1
pvcreate /dev/sda4
vgdisplay
vgextend lv_system /dev/sda4

#lvextend -L +20G /dev/mapper/lv_system-root
lvextend -L +19.99G /dev/mapper/lv_system-root
lvextend -l +25600 /dev/lv_system/root

#resize2fs  /dev/mapper/lv_system-root
xfs_growfs  /dev/mapper/lv_system-root
xfs_growfs /dev/lv_system/root
```

### `noatime`
```
vim  /etc/fstab
/dev/sdc /home/disk0 xfs defaults,noatime 0 0

mount -o remount /home/disk0

// or
mount -o noatime -o nodiratime -o remount /home/disk0
```
