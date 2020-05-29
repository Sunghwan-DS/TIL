import sys
sys.setrecursionlimit(100000)

def count_node(num):
    cnt = 1
    if tree[num][1]:
        cnt += count_node(tree[num][1])
        if tree[num][2]:
            cnt += count_node(tree[num][2])
    return cnt

def find_LCA(root, p, q):
    if root in (p, q, None):
        return root
    left = find_LCA(tree[root][1], p, q)
    right = find_LCA(tree[root][2], p, q)
    return root if (left and right) else (left or right)

for tc in range(1, int(input()) + 1):
    V, E, A, B = map(int, input().split())
    tree = [[0, 0, 0] for _ in range(V + 1)]
    data = list(map(int, input().split()))
    for idx in range(V-1):
        tree[data[idx * 2 + 1]][0] = data[idx * 2]
        if not tree[data[idx * 2]][0]:
            tree[data[idx * 2]][1] = data[idx * 2 + 1]
        else:
            tree[data[idx * 2]][2] = data[idx * 2 + 1]

    LCA = find_LCA(1, A, B)
    print("#%d"%(tc), LCA, count_node(LCA))
