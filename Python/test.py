def fill_BST(N, idx):
    global cnt
    if idx*2 <= N:
        fill_BST(N, idx*2)
    tree[idx] = cnt
    cnt += 1
    if idx*2+1 <= N:
        fill_BST(N, idx*2+1)

for tc in range(1, int(input()) + 1):
    N = int(input())
    tree = [0] * (N+1)
    cnt = 1
    fill_BST(N, 1)
    print("#%d"%(tc), tree[1], tree[N//2])