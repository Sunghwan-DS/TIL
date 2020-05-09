N, K = map(int,input().split())
sequence = list(map(int,input().split()))
history = [[] for _ in range(101)]

for idx, num in enumerate(sequence):
    history[num].append(idx)

socket = {}

ans = 0
for idx, num in enumerate(sequence):
    if len(socket) < N:
        socket[num] = 1

    elif num in socket:
        pass

    else:
        del_idx = idx
        del_num = 101
        for check in socket:
            for check_idx in history[check]:
                if check_idx > idx:
                    if del_idx < check_idx:
                        del_idx = check_idx
                        del_num = check
                    break
            else:
                del_num = check
                break

        del socket[del_num]
        socket[num] = 1
        ans += 1

print(ans)