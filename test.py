def plus(a, b):
    return a+b

def minus(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    try:
        res = a/b
    except ZeroDivisionError:
        return '0으로는 나눌 수 없습니다.'
    else:
        return res

print(plus(3, 5))
print(minus(10, 7))
print(mul(5, 5))
print(div(10, 2))
print(div(10, 0))