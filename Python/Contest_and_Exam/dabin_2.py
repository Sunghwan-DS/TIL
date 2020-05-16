import sys
import codecs
import random
# sys.stdin = codecs.getreader("utf-8")(sys.stdin.detach())
# sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

N = int(sys.stdin.readline())

for tc in range(N):
    song = list(sys.stdin.readline().rstrip('\n').split('\t'))
    singer = list(sys.stdin.readline().rstrip('\n').split('\t'))
    lst = [i for i in range(len(song))]
    sequence = []
    idx = random.choice([i for i in range(len(song))])
    while lst:
        if not sequence:
            sequence.append(lst.pop(idx))
            if len(lst) > 0:
                idx %= len(lst)
        else:
            for insert_idx in range(len(sequence) + 1):
                if 0 <= insert_idx - 1:
                    TF1 = singer[sequence[insert_idx - 1]] != singer[lst[idx]]
                else:
                    TF1 = True

                if insert_idx < len(sequence):
                    TF2 = singer[sequence[insert_idx]] != singer[lst[idx]]
                else:
                    TF2 = True

                if TF1 and TF2:
                    sequence.insert(insert_idx, lst.pop(idx))
                    if len(lst) > 0:
                        idx %= len(lst)
                    break
            else:
                idx = (idx + 1) % len(lst)
    answer_lst = []
    singer_lst = []
    for idx in sequence:
        answer_lst.append(song[idx])
        singer_lst.append(singer[idx])
    answer = '\t'.join(answer_lst)
    print(singer_lst)
    print(len(song), len(answer_lst))



    #sys.stdout.
