# Python  列表推導式(list comprehension)

# 列表推導式 => 更少的語法創建新列表

# lambda
# 平方
# def square(x):
#     return x * x
# list = []
# for i in range(1, 11):
#     list.append(square(i))
# print(list)

# squares = [i * i for i in range(1, 11)]
# print("列表推導式")
# print(squares)

grades = [100, 90, 66, 80, 46, 29, 88]
passed_grades = [g for g in grades if g >= 60]
print(passed_grades)