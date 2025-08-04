# Python 中 Lambda λ

# Lambda 有函式的功能 一行就可以寫完

# example 1 - double
# def double(x):
#     return x * 2

# print(double(10))

# double2 = lambda x: x*2
# print(double2(50))

# e×2

# multiply = lambda x, y: x * y
# print(multiply(5, 10))

# e×3 if else 條件語句

# result = lambda x: f"{x} 是偶數" if x % 2 == 0 else f"{x} 是奇數"
# 
# print(result(50.2))

# e×4 處理字串

full_name = lambda first_name, last_name: f"{first_name} {last_name}"
print(full_name("Administrator", "Local"))
