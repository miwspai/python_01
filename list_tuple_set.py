# Python 中的合集 list, set 與 tuple

# list 列表

# fruits = ["蘋果", "柳橙", "香蕉", "椰子"]

# print(fruits[1])

# for f in fruits:
    # print(f)

# fruits.append("芭樂")
# print(fruits)

# fruits.remove("椰子")
# print(fruits)

# print(fruits.index("香蕉"))
# fruits.append("蘋果")
# fruits.append("蘋果")
# print(fruits)
# print(fruits.count("蘋果"))

# print(fruits)
# fruits.reverse()
# print(fruits)

# set

fruits_set ={"🍎", "🍊", "🍌", "🥥"}
fruits_set.add("🍎")
fruits_set.add("🍉")
for fruit in fruits_set:
    print(fruit, end=" ")
if "🍎" in fruits_set:
    print("有一顆蘋果")

if "🍉" in fruits_set:
    print("有一顆西瓜")
else:
    print("沒有西瓜")

# tuple 元組

# fruits_tuple = ("🍎", "🍊", "🍌","🍎")
# result = fruits_tuple.count("🍎")
# print(result)
# result = fruits_tuple.index("🍊")
# print(result)
# fruits_tuple.add("🍎")