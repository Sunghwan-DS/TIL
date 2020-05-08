import socket
import time
from math import sin, cos, atan, pi, tan

# User and Game Server Information
NICKNAME = 'Python Player'
HOST = '127.0.0.1'
PORT = 1447 # Do not modify

# predefined variables(Do not modify these values)
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 5
HOLES = [ [0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127] ]

class Conn:
    def __init__(self):
        self.sock = socket.socket()
        print('Trying to Connect: ' + HOST + ':' + str(PORT))
        self.sock.connect((HOST, PORT))
        print('Connected: ' + HOST + ':' + str(PORT))
        send_data = '9901/' + NICKNAME
        self.sock.send(send_data.encode('utf-8'))
        print('Ready to play.\n--------------------')
    def request(self):
        self.sock.send('9902/9902'.encode())
        print('Received Data has been currupted, Resend Requested.')
    def receive(self):
        recv_data = (self.sock.recv(1024)).decode()
        print('Data Received: ' + recv_data)
        return recv_data
    def send(self, angle, power):
        merged_data = '%d/%d' % (angle, power)
        self.sock.send(merged_data.encode('utf-8'))
        print('Data Sent: ' + merged_data)
    def close(self):
        self.sock.close()

class GameData:
    def __init__(self):
        self.reset()
    def reset(self):
        self.balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]
    def read(self, conn):
        recv_data = conn.receive()
        split_data = recv_data.split('/')
        idx = 0
        try:
            for i in range(NUMBER_OF_BALLS):
                for j in range(2):
                    self.balls[i][j] = int(split_data[idx])
                    idx += 1
        except:
            self.reset()
            conn.request()
            self.read(conn)
    def show(self):
        print('=== Arrays ===')
        for i in range(NUMBER_OF_BALLS):
            print('Ball%d: %d, %d' % (i, self.balls[i][0], self.balls[i][1]))
        print()



# 자신의 차례가 되어 게임을 진행해야 할 때 호출되는 Method
def play(conn, gameData):
    global TABLE_WIDTH, TABLE_HEIGHT

    def is_not_hit(white_y, white_x, ball_y, ball_x, angle):
        a = tan(((450 - angle) % 360) * pi / 180)
        b = -1
        c = (-a) * white_x + white_y

        if abs(a * ball_x + b * ball_y + c) / (a ** 2 + b ** 2) ** 0.5 < 2 * radius:
            print(abs(a * ball_x + b * ball_y + c) / (a ** 2 + b ** 2) ** 0.5, '<', 2 * radius)
            return False
        return True


    def ball_in_path(start_y, start_x, end_y, end_x, radius):
        a = end_y - start_y
        b = start_x - end_x
        c = (-start_x) * end_y + end_x * start_y
        for idx in range(1, len(balls)):
            ball_x, ball_y = balls[idx]
            print(idx+1, '번공', abs(a * ball_x + b * ball_y + c) / (a ** 2 + b ** 2) ** 0.5, '<', 2 * radius)
            if abs(a * ball_x + b * ball_y + c) / (a ** 2 + b ** 2) ** 0.5 < 2 * radius:
                white_rode = (start_y - end_y) ** 2 + (start_x - end_x) ** 2
                yellow_1 = (start_y - ball_y) ** 2 + (start_x - ball_x) ** 2
                yellow_2 = (end_y - ball_y) ** 2 + (end_x - ball_x) ** 2
                if max(white_rode, yellow_1, yellow_2) == white_rode:
                    return True
        return False

    def cal_actan(dy, dx):
        if dx > 0:
            if dy > 0:
                return atan(dy / dx) * 180 / pi
            elif dy < 0:
                return atan(dy / dx) * 180 / pi + 360
            else:
                return 0

        elif dx < 0:
            if dy > 0:
                return atan(dy / dx) * 180 / pi + 180
            elif dy < 0:
                return atan(dy / dx) * 180 / pi + 180
            else:
                return 180

        elif dx == 0:
            if dy > 0:
                return 90
            elif dy < 0:
                return 270

    w = TABLE_WIDTH / 2
    h = TABLE_HEIGHT

    holes = ((0, 0, 225), (0, w, 270), (0, 2 * w, 315), (h, 0, 135), (h, w, 90), (h, 2 * w, 45))
    radius = 2.86
    balls = gameData.balls
    white_y = balls[0][1]
    white_x = balls[0][0]

    balls.pop(0)
    for idx in range(len(balls)-1, -1, -1):
        if balls[idx][0] == -1:
            balls.pop(idx)

    ball_x, ball_y = balls[0]
    white_to_ball = cal_actan(ball_y - white_y, ball_x - white_x)
    print("흰공에서 목표공 각도:", white_to_ball)

    distance_white_to_ball = ((ball_y - white_y) ** 2 + (ball_x - white_x) ** 2) ** 0.5

    if distance_white_to_ball <= radius :
        angle = ((360 - white_to_ball) + 90) % 360
        conn.send(round(angle), 1)
        return

    ball_to_holes = []
    sequence = []
    for hole_num, hole_data in enumerate(holes):
        hole_y = hole_data[0]
        hole_x = hole_data[1]
        ball_to_hole = cal_actan(hole_y - ball_y, hole_x - ball_x)
        ball_to_holes.append(ball_to_hole)
        abs_angle = abs(white_to_ball - ball_to_hole)
        sequence.append((min(abs_angle, 360 - abs_angle),  hole_num))

    sequence.sort()

    for criterion,  hole_num in sequence:
        if criterion >= 80:
            continue

        ball_to_hole = ball_to_holes[hole_num]
        print("목표 공에서 구멍까지 각도:", ball_to_hole)
        print("구멍의 입구 각:", holes[hole_num][2])
        correct = ball_to_hole - holes[hole_num][2]
        print("보정값:", correct)
        cal_angle = correct * 0.03 + ball_to_hole  # 목표 공이 진행하게 될 각도
        print("벽을 감안한 목표 공의 진행각:", cal_angle)

        hole_y, hole_x, dummy = holes[hole_num]

        # 목표 공 진행 경로에 공이 있는지 검토
        if ball_in_path(ball_y, ball_x, hole_y, hole_x, radius):
            continue


        move_white_y = ball_y - 2 * radius * sin(cal_angle * pi / 180)
        move_white_x = ball_x - 2 * radius * cos(cal_angle * pi / 180)

        shoot_angle = cal_actan(move_white_y - white_y, move_white_x - white_x) % (360)

        # 흰공 진행 경로에 공이 있는지 검토
        if ball_in_path(white_y, white_x, move_white_y, move_white_x, radius):
            angle = ((360 - white_to_ball) + 90) % 360
            conn.send(angle, 1)
            break

        distance_ball = ((hole_y - ball_y) ** 2 + (hole_x - ball_x) ** 2) ** 0.5
        need_target_v = distance_ball / 3.28 + 4
        abs_delta = abs(shoot_angle - cal_angle)
        print("흰공 진행방향과 목표 공이 진행할 방향의 각도:", abs_delta)
        need_white_v = need_target_v / cos(abs_delta * pi / 180)
        distance_white = ((white_y - move_white_y) ** 2 + (white_x - move_white_x) ** 2) ** 0.5
        power = need_white_v + distance_white / 3.28 + 4

        if power > 110:
            continue

        print("이상적인 흰 공의 각도: %f, 파워: %f" % (shoot_angle, power))
        print("보정값:", correct)
        # if correct < 0:
        #     shoot_angle = int(shoot_angle) + 1
        # elif correct > 0:
        #     shoot_angle = int(shoot_angle)
        # else:
        #     shoot_angle = round(shoot_angle)

        shoot_angle = round(shoot_angle)
        print("벽을 감안한 흰 공의 각도: %d, 파워: %d" % (shoot_angle, power))

        angle = ((360 - shoot_angle) + 90) % 360  # 게산 각도
        print("환산된 각도: %d, 힘: %d" % (angle, power))

        if is_not_hit(white_y, white_x, ball_y, ball_x, angle):
            continue

        print("최종 각도: %d, 힘: %d" % (angle, power))
        conn.send(angle, power)
        break


    # 아무런 방법도 없을 경우
    else:
        # 목표 공에 붙히기만 한다
        print("방법이 없다")
        min_v = round(distance_white_to_ball / 3.28) + 1
        angle = ((360 - white_to_ball) + 90) % 360
        conn.send(round(angle), min_v)


def main():
    conn = Conn()
    gameData = GameData()
    while True:
        gameData.read(conn)
        gameData.show()
        if gameData.balls[0][0] == 9909:
            break
        play(conn, gameData)
    conn.close()
    print('Connection Closed')

if __name__ == '__main__':
    main()
