# 用 Python 實作骰子遊戲

# 骰出骰子之後，顯示總和圖案
# 使用 Unicode 字元來製作骰子的圖案

import random


dice_art ={
    1: (
        "┌───┐",
        "│   │",
        "│ ● │",
        "│   │",
        "└───┘",
    ),
    2:(
       "┌───┐",
       "│●  │",
       "│   │",
       "│  ●│",
       "└───┘",
    ),
    3:(
       "┌───┐",
       "│●  │",
       "│ ● │",
       "│  ●│",
       "└───┘",
    ),
    4:(
       "┌───┐",
       "│● ●│",
       "│   │",
       "│● ●│",
       "└───┘",
    ),
    5:(
       "┌───┐",
       "│● ●│",
       "│ ● │",
       "│● ●│",
       "└───┘",
    ),
    6:(
       "┌───┐", # 0
       "│● ●│", # 1
       "│● ●│", # 2
       "│● ●│", # 3
       "└───┘", # 4
    ),
}
# print(dice_art.get(6))
num_dice = int(input("請輸入要擲幾個骰子: "))
dice = []
for i in range(num_dice):
    dice_number = random.randint(1,6)
    dice.append(dice_number)
# print(dice)

def get_dice_number(number):
    # noinspection PyShadowingNames
    for i in range(5):
        print(dice_art.get(number)[i])

for i in dice:
    get_dice_number(i)
print("總和: ", sum(dice))
# get_dice_number(3)
