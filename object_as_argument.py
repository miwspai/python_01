# Python 物件當成引數

class Car:
    color = None

def change_color(car, color):
    car.color = color

car1 = Car()
car2 = Car()
car3 = Car()

print(car1.color)
print(car2.color)
print(car3.color)

change_color(car1, "紅色")
change_color(car2, "藍色")
change_color(car3, "綠色")

print(car1.color)
print(car2.color)
print(car3.color)
