# Python 中的函數 / 函式 (function)

# 又稱為方法(method)

def say_hello():
    print("嗨!世界你好!")


# say_hello()
# say_hello()
# say_hello()

# 傳遞參數

def greeting(name):
    print(f"你好, {name}!")
# greeting("阿哥")


def add(x, y):
    return x + y

# result = add(3,5)
# print(result)


def sub(x, y):
    return x - y

# result2 = sub(5, 2)
# print(result2)

def mul(x, y):
    return x * y

# result3 = mul(2, 7)
# print(result3)

def devide(x,y):
    return x / y

# result4 = devide(15, 3)
# print(result4)

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

print( create_name('john', 'wick') )
