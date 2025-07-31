# import math
# Python 中的數學

# 加減乘除
# apples = 3
# apples = apples + 1
# apples += 1
# print(apples)
# # apples = apples + 1
# apples += 1
# print(apples)
# apples = apples - 1
# print(apples)
# apples -= 1
# print(apples)

# apples =apples * 2
# print(apples)
# apples *= 2
# print(apples)

# apples =apples / 3
# print(apples)
# apples /= 2
# print(apples)

# (平方, 三次方)
# apples = 3
# apples = apples ** 1
# apples **= 2
# print(apples)

# 模數 mod

# 10 mod 3 等於 3 除 1
print(10 % 3)
# 11 mod 3 等於 3 除 2
print(11 % 3)
# 12 mod 3 等於 4 除 0
print(12 % 3)

# 內置函數

# # 次方 pow
print(pow(3,2))

# 最大值 Max 與最小值 Min
# x = 1
# y = 2
# z = 3
# print(max(x,y,z))
# print(min(x,y,z))
#
# # 四捨五入 round
# a = 3.14
# print(round(a))
# b = 3.5
# print(round(b))

### 絕對值
# c = -4
# print("絕對值:", abs(c))

# 四捨五入 ，無條件進位 ，無條件捨去
# x = 9.5
# # print(round(9.5))
# # print(math.ceil(x))
# print(math.floor(x))
# 圓周率

# print(math.pi)

# 計算圓的周長 2πR
# radius = float(input("請輸入圓的半徑"))
# c = 2 * math.pi * radius
# print(f"圓的周長為{round(c,2) }")

# 計算圓的面積 πR²
# radius = float(input("請輸入圓的半徑"))
# area = math.pi * (radius ** 2)
# print(f"圓的面積為{round(area) }")