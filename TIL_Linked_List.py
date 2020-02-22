# 단순 연결 리스트 (다음 노드의 주소만을 저장, 단일방향으로만 이동 가능)

# 첫 번째 노드로 삽입하는 알고리즘
def addtoFirst(data):  # 첫 노드에 데이터 삽입
    global Head
    Head = Node(data, Head)  # 새로운 노드 생성


# 가운데 노드에 삽입하는 알고리즘
def add(pre, data):  # pre 다음에 데이터 삽입
    if pre == None:
        print('error')
    else:
        pre.link = Node(data, pre.link)


# 마지막 노드로 삽입하는 알고리즘
def addtoLast(data):  # 마지막에 데이터 삽입
    global Head
    if Head == None:  # 빈 리스트이면
        Head = Node(data, None)
    else:
        p = Head
        while p.link != None:  # 마지막 노드를 찾을 때까지
            p = p.link
        p.link = Node(data, None)


# 첫 번째 노드를 삭제하는 알고리즘
def deletetoFirst():  # 처음 노드 삭제
    global Head
    if Head == None:
        print('error')
    else:
        Head = Head.link


# 노드를 삭제하는 알고리즘
def delete(pre):  # pre 다음 노드 삭제
    if pre == None or pre.link == None:
        print('error')
    else:
        pre.link = pre.link.link



# 이중 연결 리스트 (이전 노드의 주소와 다음 노드의 주소를 저장, 양방향 이동 가능)

# prev, data, next (이중 연결 리스트의 기본 노드)
