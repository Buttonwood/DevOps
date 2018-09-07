#! /usr/bin/python # coding=utf-8

from datetime import datetime
from datetime import timedelta
from random import randint,random

fxsj = open("fxsj.sql", "w")


def temperature():
    mi = randint(400,430)
    mx = randint(650,750)
    st = mi + randint((mx-mi),(mx-mi)*2)*1.00/4
    rd = mi + randint((mx-mi)*2,(mx-mi)*3)*1.00/4
    ten = randint(460,600)
    mean = randint(int(st),int(rd)) + random()
    median = randint(int(st),int(rd)) + random()
    ss = '\'%d\', \'%d\', \'%d\', \'%.2f\', \'%.2f\', \'%.2f\', \'%.2f\'' % (mi, mx, ten, st, rd, mean, median)
    return ss

def swing():
    mi = randint(10,15)
    mx = randint(20,25)
    st = mi + randint((mx-mi),(mx-mi)*2)*1.00/4
    rd = mi + randint((mx-mi)*2,(mx-mi)*3)*1.00/4
    ten = randint(15,20)
    mean = randint(int(st),int(rd)) + random()
    median = randint(int(st),int(rd)) + random()
    ss = '\'%d\', \'%d\', \'%d\', \'%.2f\', \'%.2f\', \'%.2f\', \'%.2f\'' % (mi, mx, ten, st, rd, mean, median)
    return ss

def data(i=randint(1,20)):
    jh = str(i).zfill(5)
    st = datetime(2014,1,1,0,0,0)
    d = 0
    for xq in xrange(1,randint(150,250)):
        # a week
        st += timedelta(days=7)
        # a week < 3
        dt = datetime(st.year, st.month, st.day)
        for x in xrange(1,randint(2,4)):
            # a day < 3
            dt += timedelta(days=x)
            ad = datetime(dt.year, dt.month, dt.day, randint(9,17))
            for y in xrange(1,randint(2,3)):
                d += 1
                hd = str(d).zfill(5)
                # fly time
                ed = 1800 + randint(0,12) * 600
                ad += timedelta(hours=y, seconds=ed) 
                ast = datetime(ad.year, ad.month, ad.day, ad.hour, randint(0,3) * 15, 0)
                ss = '\'%s\',\'%s\', \'%s\', \'%s\', \'%d\'' % (datetime(ad.year, ad.month, ad.day).strftime("%Y-%m-%d"),str(ast),jh,hd,ed)
                ss += ',' + temperature() + ',' + swing()
                fxsj.write("INSERT INTO flight_data (flight_date, flight_segment, flight_id, segment_id, flight_time, temperature_min, temperature_max, temperature_ten, temperature_first, temperature_third, temperature_mean, temperature_medain, swing_min, swing_max, swing_ten, swing_first, swing_third, swing_mean, swing_medain) VALUES (" + ss + ");\n")
                print(ss)

def test():
    #print(temperature(),swing())
    data()

def main():
    test()
    fxsj.close()
    
if __name__ == '__main__':
    main()
