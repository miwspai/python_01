# Python 中的作用域

# 變數範圍與作用域
# LEGB 作用域順序

# L - local 區域
# E - enclosed
# G - Global 全域
# B - built-in

# 變數範圍

a = 10
b = 31
c = 30
d = 40
f = 3856
e = 35

def function_one():
    a = 1
    print("a:", a)
    def function_two():
        b = 35
        print("b:", e)
    def function_three():
            c = 3
            print("c:", c)
            # def function_four():
            #         d = (101)
            #         print("d:", d)
            # function_four()

            def function_six():
                    f = (3856)
                    print("f:", f)
            function_six()
    function_three()
    function_two()
function_one()

from math import e
print(e)
print(round(e))

# def function_one():
#     print(e)
# function_one()
