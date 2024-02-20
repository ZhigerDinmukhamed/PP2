from datetime import *
x = datetime.now()
without_micro = x.replace(microsecond = 0)
print(without_micro.strftime("%Y - %m - %d, %H:%M:%S.%f"))