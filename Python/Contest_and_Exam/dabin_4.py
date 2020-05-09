n = int(input())
a = int(input())
formation = input()
formation = formation[:a] + 'A' + formation[a:]

val = 'A'
ans = -1
while len(formation) != 1:
    next_formation = ''
    for idx in range(0, len(formation), 2):
        if idx != len(formation) - 1:
            result = set([formation[idx], formation[idx+1]])
        else:
            result = set([formation[idx]])

        if result == set(['R', 'P']):
            next_formation += 'P'
        elif result == set(['R', 'S']):
            next_formation += 'R'
        elif result == set(['P', 'S']):
            next_formation += 'S'
        elif len(result) == 1:
            next_formation += list(result)[0]

        elif result == set(['P', 'A']):
            if val != 'S':
                val = 'S'
                ans += 1
                next_formation += 'A'
            else:
                next_formation += 'A'
        elif result == set(['S', 'A']):
            if val != 'R':
                val = 'R'
                ans += 1
                next_formation += 'A'
            else:
                next_formation += 'A'
        elif result == set(['R', 'A']):
            if val != 'P':
                val = 'P'
                ans += 1
                next_formation += 'A'
            else:
                next_formation += 'A'
    formation = next_formation
print(ans)