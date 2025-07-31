# 複利計算機
# 總金額 = 本金 * (1 + (利率 / 100)) ** 時間
amount = 0
rate = 0
time = 0

while amount <= 0:
    if amount <= 0:
        print("本金金額不能小於或是等於零")
    amount = float(input("請輸入本金金額: "))

while rate <= 0:
    rate =float(input("請輸入利率: "))
    if rate <= 0:
        print("利率不能小於或等於0")

while time <= 0:
    time = int(input("請輸入年限: "))
    if time <= 0:
        print("年齡不能小於等於 0")

print("金額: ",amount)
print("利率: ", rate)
print("年限", time)


# 總金額 = 本金 * (1 + (利率 / 100)) ** 時間
total = amount * (1+ (rate / 100)) ** time
print("總金額: ", total)