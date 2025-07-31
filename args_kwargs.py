# kwargs => 關鍵字 + args (keyword args) ** => diction
# args => arguments 任意數量的參數

# args

# def add(a, b):
#     return a + b
# print(add(1,2))

# def add(*args):
#     total = 0
#     for arg in args:
#         print(f"args: {arg}")
#         total += arg
#     return total

# print( add(1,2, 3))



def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"key: {key} value: {value}")

print_info(name="Alice", age="25", occupation="工程師")