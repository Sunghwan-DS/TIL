# def my_math():
# #     pi = 3.14
# #
# #     def circum(r):
# #         return 2*pi*r
# #
# #     return circum
# #
# # a = my_math()
# #
# # print(a(1))
# # print(a(3))

def count():
    cnt = 0

    def plus():
        nonlocal cnt
        cnt += 1
        return cnt

    return plus

a = count()
print(a())
print(a())
b = count()
print(a())
print(b())
print(a())