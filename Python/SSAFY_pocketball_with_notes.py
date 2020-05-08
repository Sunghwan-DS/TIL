from math import sin, cos, atan, pi

def ball_in_path(start_y, start_x, end_y, end_x, radius):
    a = end_y - start_y
    b = start_x - end_x
    c = (-start_x) * end_y + end_x * start_y
    for ball_y, ball_x in balls:
        if (round(ball_y, 4) == round(start_y, 4) and round(ball_x, 4) == round(start_x, 4)) or (round(ball_y, 4) == round(end_y, 4) and round(ball_x, 4) == round(end_x, 4)):
            continue

        if abs(a*ball_x + b*ball_y + c) / (a**2 + b**2) ** 0.5 < 2*radius and min(start_y, end_y) < ball_y < max(start_y, end_y) and min(start_x, end_x) < ball_x < max(start_x, end_x):
            return True
    return False


def cal_actan(dy, dx):
    if dx > 0:
        if dy > 0:
            return atan(dy/dx) * 180 / pi
        elif dy < 0:
            return atan(dy / dx) * 180 / pi + 360
        else:
            return 0

    elif dx < 0:
        if dy > 0:
            return atan(dy/dx) * 180 / pi + 180
        elif dy < 0:
            return atan(dy/dx) * 180 / pi + 180
        else:
            return 180

    elif dx == 0:
        if dy > 0:
            return 90
        elif dy < 0:
            return 270


w = 127     # 당구대 가로 절반
h = 127     # 당구대 세로
holes = ((0, 0, 225), (0, w, 270), (0, 2*w, 315), (h, 0, 135), (h, w, 90), (h, 2*w, 45))    # 6개의 구멍 좌표와 진입각

radius = 2.86      # 당구공 반지름
white_y = 64   # 흰공 y좌표
white_x = 64   # 흰공 x좌표

balls = [(250, 5)]     # 목표 공들의 좌표 (x, y)

angles_white_to_ball = []   # 흰공에서 각 목표 공에 대한 각도(radian)
for ball_x, ball_y in balls:
    angles_white_to_ball.append(cal_actan(ball_y - white_y, ball_x - white_x))
print("흰공에서 각 목표 공의 각도:", angles_white_to_ball)
print()

angles_balls_to_holes = []
sequence = []
for ball_num, ball_data in enumerate(balls):
    ball_x = ball_data[0]
    ball_y = ball_data[1]
    ball_to_holes = []
    for hole_num, hole_data in enumerate(holes):
        hole_y = hole_data[0]
        hole_x = hole_data[1]
        ball_to_hole = cal_actan(hole_y - ball_y, hole_x - ball_x)
        ball_to_holes.append(ball_to_hole)
        abs_angle = abs(angles_white_to_ball[ball_num] - ball_to_hole)
        sequence.append((min(abs_angle, 360 - abs_angle), ball_num, hole_num))
    angles_balls_to_holes.append(ball_to_holes)

print(angles_balls_to_holes)
print(sequence)
sequence.sort()     # 각도, 공 번호, 구멍 번호
print("우선순위:", sequence)

for dummy, ball_num, hole_num in sequence:
    print("선택된 목표 공 번호:", ball_num)
    print("선택된 구멍 번호:", hole_num)
    ball_to_hole = angles_balls_to_holes[ball_num][hole_num]
    print("선택된 구멍까지의 각도:", ball_to_hole)
    print("보정값:", ball_to_hole - holes[hole_num][2])
    cal_angle = (ball_to_hole - holes[hole_num][2]) * 0.00 + ball_to_hole  # 목표 공이 진행하게 될 각도, 임의로 정한 0.1 @@@@@@@@@@@@
    print("벽을 감안한 목표 공의 진행각:", cal_angle)
    print()

    ball_x, ball_y = balls[ball_num]
    hole_y, hole_x, dummy = holes[hole_num]
    # 목표 공 진행 경로에 공이 있는지 검토
    if ball_in_path(ball_y, ball_x, hole_y, hole_x, radius):
        continue

    move_white_y = ball_y - 2 * radius * sin(cal_angle * pi / 180)  # 흰공이 도착해야할 y좌표
    move_white_x = ball_x - 2 * radius * cos(cal_angle * pi / 180)  # 흰공이 도착해야할 x좌표
    print("흰공이 도착해야할 좌표:", move_white_y, ",", move_white_x)

    shoot_angle = cal_actan(move_white_y - white_y, move_white_x - white_x) % (360)  # 흰공 쏠 각도
    print("흰공 쏠 각도:", shoot_angle)
    print()

    # 흰공 진행 경로에 공이 있는지 검토
    if ball_in_path(white_y, white_x, move_white_y, move_white_x, radius):
        continue

    distance_ball = ((hole_y - ball_y) ** 2 + (hole_x - ball_x) ** 2) ** 0.5
    print("목표 공이 가야할 거리:", distance_ball)
    k = 9   # 상수 k = 2 * f / m, 임의로 1 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    need_target_v = k * distance_ball ** 0.5
    print("목표 공이 필요한 속도:", need_target_v)
    abs_delta = abs(shoot_angle - cal_angle)
    print("흰공 진행방향과 목표 공이 진행할 방향의 각도:", abs_delta)
    need_white_v = need_target_v / cos(abs_delta * pi / 180)
    print("목표 공이 필요한 충돌 직전 속도:", need_white_v)
    distance_white = ((white_y - move_white_y) ** 2 + (white_x - move_white_x) ** 2) ** 0.5
    print("흰공이 이동하는 거리", distance_white)
    need_white_v0 = (need_white_v ** 2 + k * distance_white) ** 0.5
    print("흰공의 초기 속도:", need_white_v0)
    print()

    print("결정된 흰 공의 각도: %f, 파워: %f"%(shoot_angle, need_white_v0))
    shoot_angle = ((360 - shoot_angle) + 90) % 360 # 최종 각도
    print("출력할 각도: %f, 힘: %f"%(shoot_angle, need_white_v0))
    break


# 아무런 방법도 없을 경우
else:
    print("최후의 보루")