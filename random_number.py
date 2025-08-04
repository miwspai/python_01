import random
# number = random.randint(low, high)

# randint()
# print( random.randint(1,10))

# random()

# print( random.random() )

# 列表中隨機選擇一個元素
# options = ["剪刀", "石頭", "布"]
# rand_option = random.choice(options)
# print("電腦選擇的是: ", rand_option)

# 將一個列表打亂
# cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# random.shuffle(cards)
# print(cards)

# 猜數字遊戲

low = 1
high = 100
number = 66
guesses = 0

while True:
    # 讓玩家猜數字
    guess = int(input(f"請猜一個介於{low}~{high}之間的數字:"))
    guesses += 1
    if guess < number:
        print("猜的數字太小了")

    elif guess > number:
        print("猜的數字太大了")
    else:
        print(f"恭喜你猜對了!這個數字就是{number}")
        print(f"你總共猜了{guesses}次。")
        break
