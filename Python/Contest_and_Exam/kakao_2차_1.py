# Enter your code here. Read input from STDIN. Print output to STDOUT

import math


def tf(unique_word, target_content, target_max_ftd):
    if unique_word in target_content:
        ftd = target_content[unique_word]
    else:
        ftd = 0
    return 0.5 + 0.5 * (ftd / target_max_ftd)


def idf(unique_word):
    global N

    return math.log(N / cnt_unique_words[unique_word])


def tfidf(unique_word, target_content, target_max_ftd):
    return tf(unique_word, target_content, target_max_ftd) * idf(unique_word)


def cal_cosine_similarity(vector1, vector2):
    ttt = len(vector1)
    sum_val = 0
    A_val = 0
    B_val = 0
    for idx in range(ttt):
        sum_val += vector1[idx] * vector2[idx]
        A_val += vector1[idx] ** 2
        B_val += vector2[idx] ** 2

    return sum_val / (A_val ** 0.5 * B_val ** 0.5)


N = 10
Data_list = []

clusters = []
ID_Data = {}
Unique_words = set()
# max_unique_words = {}
cnt_unique_words = {}

input_data = [('20200806194156728 13', '처음 엠카 전소미 에이티즈 강 다니엘 여자 아이 산들 로켓 펀치 컴백 종합'),
              ('20200806190006889 9', '이강인 메인 모델 발렌시아 시즌 목표 계약 유니폼 공개'),
              ('20200806060107549 5', '우리 사랑 손호준 송지효 기회'),
              ('20200806205532059 8', '발렌시아 유니폼 공개 메인 모델 이강인 계약 목표'),
              ('20200805223802735 7', '우리 사랑 송지효 손호준 김다솜 종합 기회'),
              ('20200806154955512 8', '중국 반도체 자립 속도 법인세 면제 파격 혜택'),
              ('20200805222700617 9', '종합 퀴즈 블럭 김창한 대표 배틀 그라운드 수익 개발비'),
              ('20200806170331696 11', '할리스 방문 홍천 캠핑 확진자 집단 감염 역삼동 빌딩 근무 처음'),
              ('20200806194247742 11', '엠카 강 다니엘 에이티즈 여자 아이 산들 로켓 펀치 컴백 전소미'),
              ('20200806184750590 7', '반도체 속도 법인세 면제 파격 중국 자립')]

tot_cnt = 0
for _ in range(N):
    DOC_ID, cnt_word = input_data[_][0].split()
    words = input_data[_][1].split()
    # print(DOC_ID, cnt_word, words)
    tot_cnt += int(cnt_word)

    content = {}
    kind_of_content = set()
    for word in words:
        kind_of_content.add(word)
        if word in content:
            content[word] += 1
        else:
            content[word] = 1
    kind_of_content = list(kind_of_content)
    for kind in kind_of_content:
        if kind in cnt_unique_words:
            cnt_unique_words[kind] += 1
        else:
            cnt_unique_words[kind] = 1

    max_ftd = 0
    for key in content:
        max_ftd = max(max_ftd, content[key])

    # for word in content:
    #     if word in max_unique_words:
    #         max_unique_words[word] = max(content[word], max_unique_words[word])
    #     else:
    #         max_unique_words[word] = content[word]

    Data_list.append([DOC_ID, content, max_ftd])
    ID_Data[DOC_ID] = content
    for word in content:
        Unique_words.add(word)

Unique_words = list(Unique_words)
Unique_words.sort()
# print(cnt_unique_words)
# print(len(Unique_words))

for data in Data_list:
    target_DOC_ID, target_content, target_max_ftd = data
    target_vector = []

    for unique_word in Unique_words:
        target_vector.append(tfidf(unique_word, target_content, target_max_ftd))
    print(target_vector)
    select_cluster = 0
    max_val = 0

    for cluster_idx, cluster in enumerate(clusters):
        DOC_ID, cnt, vector = cluster

        new_val = cal_cosine_similarity(vector, target_vector)
        if new_val > max_val:
            select_cluster = cluster_idx
            max_val = new_val

    # print(max_val, select_cluster)
    if max_val >= 0.98:
        clusters[select_cluster][1] += 1
    else:
        clusters.append([target_DOC_ID, 1, target_vector])

print(len(clusters))
for cluster in clusters:
    DOC_ID, cnt, vector = cluster
    print(DOC_ID, cnt)

# 7
# 20200806203611754 8
# 올림픽대로 강변북로 통제 서울 출근 지각 퇴근길 대란
# 20200806003111043 6
# 백종원 골목 식당 창동 강정 예고
# 20200806155137596 6
# 아파트 전월세 월세 전세 보증금 급등
# 20200805215334147 7
# 올림픽대로 통제 강변북로 서울 퇴근길 대란 지각
# 20200806093242998 6
# 서울 올림픽대로 강변북로 지각 출근 대란
# 20200805230051988 8
# 갤럭시 버즈 라이브 공개 노이즈 캔슬링 품질 개선
# 20200806140159987 5
# 아파트 전월세 전세 월세 급등

# print(tot_cnt, cnt_unique_words)
# ccc = 0
# for key in cnt_unique_words:
#     ccc += cnt_unique_words[key]
# print(ccc)