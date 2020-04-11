for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    cx1 = (p1+x1)
    cy1 = (q1+y1)
    cx2 = (p2+x2)
    cy2 = (q2+y2)

    hx1 = (p1-x1)
    hy1 = (q1-y1)
    hx2 = (p2-x2)
    hy2 = (q2-y2)

    if abs(cx1-cx2) > (hx1+hx2) or abs(cy1-cy2) > (hy1+hy2):
        print("d")

    elif abs(cx1-cx2) < (hx1+hx2) and abs(cy1-cy2) < (hy1+hy2):
        print("a")
       
    elif abs(cx1-cx2) == (hx1+hx2) and abs(cy1-cy2) == (hy1+hy2):
        print("c")
    
    else:
        print("b")