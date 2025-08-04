# 型別轉換 type casting

name = "John"
age = 21
gpa = 1.9
student = True

student =str(student)
print(student)
print(type(student))

gpa = int(gpa)
print(gpa)
print(type(gpa))

age = float(age)
print(age)
print(type(age))


# 隱式型別轉換

x = 10
y = 2.0
x = x/y
print(x)
print(type(x))