# OOP - Python 中的繼承

# 父類別 <-> 子類別

# 動物
class Animal:
    aLive = True

    def eat(self):
        print("這個動物在吃東西")
    def sleep(self):
        print("這個動物正在睡覺")
# 兔子
class Rabbit(Animal):
    def jump(self):
        print("這個兔子正在調")
# animal = Animal()
# animal.eat()
# animal.sleep()
# rabbit = Rabbit()
# rabbit.jump()
# rabbit.eat()

# 魚
class Fish(Animal):
    def swim(self):
        print("魚在游泳")

# fish = Fish()
# fish.swim()
# fish.eat()
# fish.sleep()

# 老鷹
class Hawk(Animal):
    def fly(self):
        print("老鷹正在飛")

hawk = Hawk()
hawk.fly()
hawk.eat()
