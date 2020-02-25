N = int(input())
match = [list(map(int, input().split())) for _ in range(N)]
team_set = {i for i in range(N)}
answer = 1000


def score(team):
    result = 0
    result2 = 0
    for i in team:
        for j in team:
            result += match[i][j]
    team2 = list(team_set - set(team))
    for i in team2:
        for j in team2:
            result2 += match[i][j]
    return abs(result - result2)


def make_teams(num, team):
    global answer
    if num == N // 2:
        if answer > score(team):
            answer = score(team)
        return

    for i in range(max(team) + 1, N):
        team.append(i)
        make_teams(num + 1, team)
        team.pop(-1)


make_teams(1, [0])
print(answer)