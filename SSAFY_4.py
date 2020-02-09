import random

command = input("명령어를 입력하세요.(자리 / 조 편성)\n")

boys = ['김성민', '김세훈', '김연수', '김원정', '김태형', '남동규', '류승민', '박세진', '박태웅', '서용준',
        '이승헌', '이원준', '이태정', '전성환', '정재철', '조제형', '지건형', '표하민', '황수현']
girls = ['강민정', '김나연', '김민재', '우지윤', ' 이솔 ', '이예은', '조다빈']
total = boys[:] + girls[:]

if command == "자리":
    random.shuffle(total)
    print("""%s %s ㅣ %s %s %s
%s %s ㅣ %s %s %s
%s %s ㅣ %s %s %s
%s %s ㅣ %s %s %s
%s %s ㅣ %s %s
             ㅣ %s %s"""%(total[0], total[1], total[2], total[3], total[4], total[5], total[6], total[7], total[8], total[9], total[10],
                      total[11], total[12], total[13], total[14], total[15], total[16], total[17], total[18], total[19], total[20],
                      total[21], total[22], total[23], total[24], total[25]))


elif command == "조 편성":
    N = int(input("편성하려는 조 개수를 입력하세요.\n"))
    random.shuffle(boys)
    random.shuffle(girls)
    q = boys[:] + girls[:]
    group = [[] for _ in range(N)]
    cnt = 0
    while q:
        group[cnt % N].append(q.pop(0))
        cnt += 1

    for idx, g in enumerate(group):
        print("#%d"%(idx+1),*g)


else:
    print("잘못된 명령어 입니다.")