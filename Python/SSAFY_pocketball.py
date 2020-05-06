from math import sin, cos, atan, pi

def ball_in_path(start_y, start_x, end_y, end_x):
    global radius
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
            return atan(dy/dx)
        elif dy < 0:
            return atan(dy / dx) + 2 * pi
        else:
            return 0

    elif dx < 0:
        if dy > 0:
            return atan(dy/dx) + pi
        elif dy < 0:
            return atan(dy/dx) + pi
        else:
            return pi

    elif dx == 0:
        if dy > 0:
            return pi / 2
        elif dy < 0:
            return 3 / 2 * pi


w = 100     # 당구대 가로 절반
h = 100     # 당구대 세로
holes = ((0, 0, 5/4*pi), (0, w, 3/2*pi), (0, 2*w, 7/4*pi), (h, 0, 3/4*pi), (h, w, 1/2*pi), (h, 2*w, 1/4*pi))    # 6개의 구멍 좌표와 진입각 angle of entry

radius = 5      # 당구공 반지름
white_y = 50    # 흰공 y좌표
white_x = 100   # 흰공 x좌표

balls = [(75, 150)]     # 목표 공들의 좌표 (y, x)

angles_white_to_ball = []   # 흰공에서 각 목표 공에 대한 각도(radian)
for ball_y, ball_x in balls:
    angles_white_to_ball.append(cal_actan(ball_y - white_y, ball_x - white_x))

angles_balls_to_holes = []
sequence = []
for ball_num, ball_data in enumerate(balls):
    ball_y = ball_data[0]
    ball_x = ball_data[1]
    ball_to_holes = []
    for hole_num, hole_data in enumerate(holes):
        hole_y = hole_data[0]
        hole_x = hole_data[1]
        ball_to_hole = cal_actan(hole_y - ball_y, hole_x - ball_x)
        ball_to_holes.append(ball_to_hole)
        abs_angle = abs(angles_white_to_ball[ball_num] - ball_to_hole)
        sequence.append((min(abs_angle, 2*pi - abs_angle), ball_num, hole_num))
    angles_balls_to_holes.append(ball_to_holes)

sequence.sort()     # 각도, 공 번호, 구멍 번호

for dummy, ball_num, hole_num in sequence:
    ball_to_hole = angles_balls_to_holes[ball_num][hole_num]
    cal_angle = (ball_to_hole - holes[hole_num][2]) * 0.1 + ball_to_hole  # 목표 공이 진행하게 될 각도, 임의로 정한 0.1 @@@@@@@@@@@@

    ball_y, ball_x = balls[ball_num]
    hole_y, hole_x, dummy = holes[hole_num]
    # 목표 공 진행 경로에 공이 있는지 검토
    if ball_in_path(ball_y, ball_x, hole_y, hole_x):
        continue

    move_white_y = ball_y - 2 * radius * sin(cal_angle)  # 흰공이 도착해야할 y좌표
    move_white_x = ball_x - 2 * radius * cos(cal_angle)  # 흰공이 도착해야할 x좌표

    shoot_angle = cal_actan(move_white_y - white_y, move_white_x - white_x) % (2*pi)  # 흰공 쏠 각도
    # 흰공 진행 경로에 공이 있는지 검토
    if ball_in_path(white_y, white_x, move_white_y, move_white_x):
        continue

    distance_ball = ((hole_y - ball_y) ** 2 + (hole_x - ball_x) ** 2) ** 0.5
    k = 1   # 상수 k = 2 * f / m, 임의로 1 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    need_target_v = k * distance_ball ** 0.5
    abs_delta = abs(shoot_angle - cal_angle)
    need_white_v = need_target_v / cos(abs_delta)
    distance_white = ((white_y - move_white_y) ** 2 + (white_x - move_white_x) ** 2) ** 0.5
    need_white_v0 = (need_white_v ** 2 + k * distance_white) ** 0.5

    print("결정된 흰 공의 각도: %f, 파워: %f"%(shoot_angle, need_white_v0))
    break


# 아무런 방법도 없을 경우
else:
    print("최후의 보루")