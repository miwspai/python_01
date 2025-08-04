# Python 中的 if __name__ = '__main__'
# 模組 1
import module2
module2.hello()

print("模組1 __name__: " + __name__)
if __name__ == '__main__':
    print('模組 1 __name__ = __main__')