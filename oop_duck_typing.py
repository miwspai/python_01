# Duck Typing

class Duck:
    def walk(self):
        print("鴨子在走路")
    def talk(self):
        print("鴨子在呱呱呱")

class Chilken:
    def walk(self):
        print("雞在走路")
    def talk(self):
        print("雞在咕咕的叫")

# 即使沒有繼承的關係,也可以當作同一類型的類別使用

class Person():
    def catch(self, duck):
        duck.walk()
        duck.talk()
# duck = Duck()
chilken = Chilken()
person = Person()
# person.catch(duck)
person.catch(chilken)

