# Python Zip 函式 # 迭代時候記得加 .items

username = ["Bob", "Steven", "Sam"]
passwords = ("123", "321", '555')
dates = ['1998-02-05', '1998-03-05', '1998-05-05']

users = zip(username, passwords, dates)
print(users)
for i in users:
    print(i)

# print( list(users))
# user_dict = dict(users)
# print(user_dict) # key → username
# 
# for key, value in user_dict.items():
#     print(key + ":" + value)