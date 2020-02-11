N, K = map(int,input().split())
colar = [list(map(int,input().split())) for _ in range(N)]

unit = [list(map(int,input().split())) for _ in range(K)]

dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]
