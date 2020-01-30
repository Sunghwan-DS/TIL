def move(direction, distance, y, x):
    if direction == 1:
        return [y, x+distance]
    elif direction == 2:
        return [y, x-distance]
    elif direction == 3:
        return [y+distance, x]
    elif direction == 4:
        return [y-distance, x]

K = int(input())
history = []
coordinates = [[1000, 1000]]
for _ in range(6):
    history.append(list(map(int,input().split())))
    coordinates.append(move(history[_][0], history[_][1], coordinates[-1][0], coordinates[-1][1]))

max_y = max(coordinates[_][0] for _ in range(6))
max_x = max(coordinates[_][1] for _ in range(6))
min_y = min(coordinates[_][0] for _ in range(6))
min_x = min(coordinates[_][1] for _ in range(6))

for index, middle in enumerate(coordinates):
    if min_y < middle[0] < max_y and min_x < middle[1] < max_x:
        idx = index
        break

out = history[idx-1][1] * history[idx][1]

print(((max_y-min_y)*(max_x-min_x) - out)*K)