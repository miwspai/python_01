# 猜拳遊戲

# 猜拳遊戲是一種流行的遊戲，通常有兩個人玩，但也可以由一個人和電腦玩。
# 遊戲目的是在手中手勢中選擇一個，並以某種規則來決定勝負。一下是猜拳遊戲規則：
#
#   石頭 (Rock) 贏剪刀 (Scissors)
#   剪刀 (Scissors) 贏布 (Paper)
#   布 (Paper) 贏石頭 (Rock)
#
# 在遊戲開始之前，每個玩家都必須選擇石頭 、剪刀或布之一，而在決定勝負時，則根據上述規則進行比較。
# 如果兩個人玩家選擇相同的手勢，則比賽以平局結束。

import random
player = None
computer = None
running = True
options = ("剪刀", "石頭", "布")

while running:
    player = input("請輸入剪刀、石頭、布:")
    while player not in options:
        input("輸入錯誤，請輸入剪刀、石頭、布:")
    computer = random.choice(options)
    print(f"玩家: {player}，電腦: {computer}")
    if player == computer:
        print("平手")
    elif player == "剪刀" and computer == "布":
        print("玩家勝利")
    elif player == "石頭" and computer == "剪刀":
        print("玩家勝利")
    elif player == "布" and computer == "石頭":
        print("玩家勝利")
    else:
        print("電腦勝利")
    play_again = input("在玩一局?(y/n)").lower()
    if not play_again == "y":
        running = False

print("謝謝來玩這個遊戲")
