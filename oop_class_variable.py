# Python 中的類別變數

class Car:
	wheels = 4
	
	# 事件變數
	def __init__(self, make, model, year, color):
		# 初始化
		self.make = make
		self.model = model
		self.year = year
		self.color = color

# car1 = Car("福特", "Focus", 2023, "白色")
# print(car1.wheels)
# 機車
car2 = Car("三陽", "勁戰", 2020, "黑色")
print (car2.wheels)