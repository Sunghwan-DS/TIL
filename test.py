# class Calculator:
#     count = 0
#
#     def info(self):
#         print('나는 계산기 입니다.')
#
#     @staticmethod
#     def add(a, b):
#         Calculator.count += 1
#         print('{0} + {1}는 {2} 입니다.'.format(a, b, a+b))
#
#     @classmethod
#     def history(cls):
#         print('총 {}번 계산 했습니다.'.format(cls.count))
#
# a = Calculator()
# a.info()
# a.add(1, 2)
# a.history()

class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print('{}! 걷는다!'.format(self.name))

    def eat(self):
        print('{}! 먹는다!'.format(self.name))


class Dog(Animal):
    def walk(self):
        print('{}! 달린다!'.format(self.name))

    def run(self):
        print('{}! 달린다!'.format(self.name))


class Bird(Animal):
    def fly(self):
        print('{}! 푸드덕!'.format(self.name))

dog = Dog('멍멍이')
dog.walk()
dog.run()

bird = Bird('구구')
bird.walk()
bird.eat()
bird.fly()