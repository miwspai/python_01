# Python 中的方法鏈接 Method Chainig

# car.turn_on().drive().brake().turn_off()

class Car:
    def turn_on(self):
        print("你啟動了引擎")
        # 回傳物件本身
        return self
    
    def drive(self):
        print("你開車了")
        return self

    def brake(self):
        print("你踩了剎車")
        return self

    def turn_off(self):
        print("你關閉了引擎")
        return self

car = Car()
car.turn_on().drive().brake().turn_off()
