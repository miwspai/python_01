# Python 中的方法重寫(Method Overriding)

class Animal:
    def eat(self):
        print("動物正在吃東西")

# 哺乳類 Mammal
class Mammal(Animal):
    def hi(self):
        print("我是哺乳類")
    pass
# 貓 Cat
class Cat(Mammal):
    def eat(self):
        print("小貓正在吃魚")

# 夠 Dog
class Dog(Mammal):
    def eat(self):
        print("小狗正在坑骨頭")

# cat = Cat()
# cat.eat()
# dog = Dog()
# dog.eat()
m = Mammal()
m.eat()

# class Rebbit(Animal):
#     pass
#     # def eat(self):
#     #     print("兔子再吃紅蘿蔔")

# animal = Animal()
# animal.eat()
# rebbit = Rebbit()
# rebbit.eat()