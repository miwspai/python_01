# if else elif控制流程

# Boolean 布林值
for_sale = False # 假
if for_sale:
    print('此項目正在出售')
# else:
    # print('此項目未出售')
# if else
age = int(input("請輸入年齡 : "))
if age >= 18:
    print("你可以註冊")
else:
    print("你必須年滿 18 歲才可以註冊")

# elif => else if 的縮寫
age = int(input("請輸入年齡 : "))
if age >= 100:
    print("您年齡太大，無法註冊")
elif age >= 18:
    print('你可以註冊')
elif age < 0:
    print('你還沒出生')
else:
    print("你必須年滿 18 歲才可以註冊")

# 練習