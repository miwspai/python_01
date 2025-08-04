# Python 的字串方法

# 'len()'、'find()'、'capitalize()'、
# 'upper()'、'lower()'、'count()'、和 'replace()'
# help(str)

# 使用者的全名
name = "code shiba administrator"
#
# 幾個字元
length = len(name)
print("您的全名共有", length, "個字元。")

# 找到第一個空格
space_pos = name.find(" ")
print("第一個空格出現在第", space_pos, "個字元。")

name_capitalized = name.lower()
print("您的全名（第一個字母大寫）:", name_capitalized)
