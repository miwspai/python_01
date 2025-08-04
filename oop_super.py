# Python Super 函式

class Rectengle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        print("巨型的初始化已執行")


class Square(Rectengle):
    def __init__(self, length, width):
        super().__init__(length, width)
        print("正方形的初始化已執行")

# 長 × 寬 × 高
class Cube(Rectengle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
        print(f"立方體的長寬高{height}, {width}, {height}")

cube = Cube(10, 20, 30)


