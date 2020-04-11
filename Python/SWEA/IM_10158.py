w, H = map(int, input().split())
p, q = map(int,input().split())
t = int(input())
move_x = t % (2*w)
move_y = t % (2 * H)
if move_x > w:
    result_x = abs(w-abs(p+move_x-w))
else:
    result_x = w-abs(p+move_x-w)

if move_y > H:
    result_y = abs(H - abs(q + move_y - H))
else:
    result_y = H - abs(q + move_y - H)
print(result_x, result_y)