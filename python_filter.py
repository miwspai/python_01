# Python filter 過濾

# 可以用來過濾可迭代的資料結構 (List, …)

friends = [
    ("Bob", 18),
    ("Steven", 17),
    ("Michael", 19),
    ("Susan", 16)
]

age_filter = lambda data: data[1] >= 18

can_drink_friends = list( filter(age_filter, friends) )
for friend in can_drink_friends:
    print(friend[0])
    print(friend[1])
