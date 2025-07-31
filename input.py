# 變數是一個可以重複使用的容器，用於儲存值。變數的行為就好像它所包含的值一樣。
# 在寫程式中也是類似的。
# 當我們創建一個變數時，我們需要給它一個獨特的名稱，來表示所包含的內容。
# age = 25 # integer
# print("我的年紀是" + str(age) + "歲")
# f string(字串)
# print(f"我的年紀是 {age} 歲(f-string)")
# integer 整數
# age = 30
# float 浮點數
# gpa = 3.3
# print(f"我的 GPA {gpa} 分")
# print(type(gpa))
# string
# name = 'peter'
# print(type(name))
# boolean # true,
# is_online = True
# print(f"在線上嗎?{is_online}")
# print(type(is_online))
##
# 顯式 隱式型別轉換
# print(type(name))
# print(type(age))
# print(type(gpa))
# print(type(student))
# 顯式型別轉換

# name = "John"
# age = 21
# gpa = 1.9
# student = True
#
# student =str(student)
# print(student)
# print(type(student))
#
# gpa = int(gpa)
# print(gpa)
# print(type(gpa))
#
# age = float(age)
# print(age)
# print(type(age))


# 隱式型別轉換

# x = 10
# y = 2.0
# x = x/y
# print(x)
# print(type(x))

# name = input("請輸入名字 : ")
# print(f"你的名字是 {name}")

# 練習一 : 填詞遊戲
adj_1 = input("請輸入第  1 個形容詞 : ")
noun = input("請輸入名詞 : ")
adj_2 = input("請輸入第  2 個形容詞 : ")
verb = input("請輸入動詞 : ")
adj_3 = input("請輸入第  3 個形容詞 : ")

# print(f"今天我去了一個{adj_1}的動物園，在展覽中看到了{noun} 這個 {noun} 很{adj_2}，正在 {verb} 我感到很 {adj_3}")
# 練習二 : 計算矩形面積
# length = float(input("請輸入矩形長度"))
# width = float(input("請輸入矩形寬度"))

# area = length * width
# print(f"面積為{area} 平方公分")
# 練習三 : 購物車程式

# item = input("你想購買什麼物品")
# price = float(input("價格多少?"))
# quantity = int(input("你需要多少件?"))
#
# total = price * quantity
#
# print(f"你購買了 {quantity} {item}，總價為 ${total}")
