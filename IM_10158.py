w, h = map(int, input().split())
p, q = map(int,input().split())
t = int(input())
move_x = t % (2*w)
move_y = t % (2*h)
if move_x > w:
    result_x = abs(w-abs(p+move_x-w))
else:
    result_x = w-abs(p+move_x-w)

if move_y > h:
    result_y = abs(h-abs(q+move_y-h))
else:
    result_y = h-abs(q+move_y-h)
print(result_x, result_y)