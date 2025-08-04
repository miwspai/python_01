# Python 獠牙運算符 :=

# 獠牙運算符
# 賦值表達式 :=
# 賦值運算子 =

# Python 3.8

# happy =True
# print(happy)

# print(happy := False)

foods = []
while (food := input('你喜歡什麼食物?')) != 'quit':
    # if food == 'quit':
    #     break
    foods.append(food)

print(foods)