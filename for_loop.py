# Python 中的 for 迴圈
# 可迭代的

# for x in range(1, 11):
#     print(x)

# for x in reversed(range(1,11)):
#     print(x)
# print("Happy new year!!")

# credit_card ="1234-5678-9012-3456"
# for x in credit_card:
#     if x == '9':
        # continue
    #     break
    # else:
    #     print(x)

# 字典 dictionary
# 鍵 key: 值 value
my_dict = {"a": 1, "b": 2, "c": 3}
# for x in my_dict:
# #     print(x)
for key, value in my_dict.items():
    print("key:", key)
    print("value:", value)