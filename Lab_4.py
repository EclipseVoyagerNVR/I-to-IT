# №1
import math
import datetime


def sqrt(n):
    return math.sqrt(n)
print(sqrt(9))

date_now = datetime.datetime.now()
print(date_now)



# №2
import my_module


num = my_module.add(1, 6)
print(num)



# №3
import my_package.modul_1
import my_package.modul_2


num = my_package.modul_1.mult(2, 14)
st = my_package.modul_2.srtings('apple')
print(num)
print(st)
