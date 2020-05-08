from math import sin, cos, atan, pi

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

print(round(1.0000049, 5))
