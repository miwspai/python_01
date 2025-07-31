# Python 購物車程式
# from builtins import float
# from fileinput import input

# list, set, tuple

# goods = [] # 列表 List
# prices = []
# 無窮回圈
while True:
    good = input("請輸入想購買的物品: ")
    if good.lower() == "q":
        break

    # price = float(input(f"請輸入 {good} 的價格: "))
    # goods.append(good)
    # prices.append(price)

# print("商品列表:", goods)
# print("價格列表:", prices)
# for index, good in enumerate(goods):
#     print(f"第 { index + 1 } 商品是 {good},價格: {prices[index]:.2f} ")

total = sum(prices)
print(f"總價格: ${total}")