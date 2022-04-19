from typing import Literal


def setDirection(direction) -> int:
    if direction == "EAST":
        return 0
    elif direction == "NORTU":
        return 90
    elif direction == "WEST":
        return 180
    elif direction == "SOUTH":
        return 270


print("input EAST will return :%d" % setDirection("EAST"))
print("input WEST will return :%d" % setDirection("WEST"))
print("input WEST will return :%d" % setDirection("EWST"))