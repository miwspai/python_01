# Python 中的 if __name__ = 'main'
import module1
# 模組 2
print("模組2 __name__: " + __name__)
if __name__ == '__main__':
    print('模組 2 __name__ = __main__')

def hello():
    print("hello")
