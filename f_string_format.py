# 014. Python f-string 的字串格式化

print_1 = '31bf3856ad364e35'
print_2 = -77
print_3 = 15.11

# 1.
# 小數點的精確度
print(f"價格 1 為 {print_1:.2f}\n"
      f"價格 2 為 {print_2:.2f}\n"
      f"價格 3 為 {print_3:.2f}")

# 2.
# 加上正號或負號
print(f"價格 1 為 {print_1:+.2f}\n"
      f"價格 2 為 {print_2:+.2f}\n"
      f"價格 3 為 {print_3:+.2f}")

# 3.
# 對齊 < > ^子中對齊
print(f"價格 1 為 {print_1:>10.2f}\n"
      f"價格 2 為 {print_2:>10.2f}\n"
      f"價格 3 為 {print_3:>10.2f}")

# 4.
# 混合不同符號
print(f"價格 1 為 {print_1:>+.2f}\n"
      f"價格 2 為 {print_2:>+.2f}\n"
      f"價格 3 為 {print_3:>+.2f}")
