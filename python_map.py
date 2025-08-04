# Python 中的 map

# map(可迭代的[列表], 函式) - 宣告

store = [
    ('襯衫', 300), # 新台幣
    ('褲子', 600),
    ('夾克', 1600),
    ('襪子', 200)
]

# to_ntd = lambda data: (data[0], data[1] * 30)

# store_euros = list(map(to_ntd, store))
# print(store_euros)

# 將台幣轉換成美金
to_usd = lambda data: (data[0], round(data[1] / 30))
store_usd = list(map(to_usd, store))

for item in store_usd:
    print(item)