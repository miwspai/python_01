# Python 中的 time

# 系統的初始時間 epoch
import time
# print(time.ctime(0))
# print(time.time())
# local_time = time.localtime()
# print(local_time)
# print("時間格式化:", time.strftime("%Y-%m=%d %H:%M:%S", local_time))

time_string = "2021-01-01 12:12:12"
time_object = time.strptime(time_string,"Literal")
print(time_object)
# print("時間格式化:", time.strftime("%Y-%m=%d %H:%M:%S"))