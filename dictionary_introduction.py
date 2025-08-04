# Python 字典入門 # 鍵 => 值 <=> key => value

capital = {
    "United States": "Washington DC",
    "Japan": "Tokyo",
    "France": "Paris",
    'Russia': 'Moscow'
}

# 1. 
# get() 取得鍵值對
# print(capital.get("Japan"))
# print(capital.get("France"))

# 2.
# update() 更新鍵值對
# capital.update({"Myanmar": "Naypyidaw"})
# print(capital)

# 3.
# pop() 刪除鍵值對
# capital.pop("United States")
# capital.pop("Japan")
# capital.pop("France")
# print(capital)

# 4.
# values() 獲得所有值
print(capital.values())

# 5.
# items() 獲得所有值對
# print(capital.items())
