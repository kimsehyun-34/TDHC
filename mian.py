import time
import os
import csv

a = 0

now = time
y = str(now.localtime().tm_year)
m = str(now.localtime().tm_mon)
d = str(now.localtime().tm_mday)
h = str(now.localtime().tm_hour)


f = open('main.csv', "r")
ff = csv.reader(f)
for line in ff:
    print(line[0])
    a = a+1
f.close()

print("특수공휴일:", a)


os.system('pause')
