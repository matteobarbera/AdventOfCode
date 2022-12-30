import numpy as np
from math import sin, cos, radians


class Ship:

    def __init__(self):
        self.b_dir = {0: "N", 90: "E", 180: "S", 270: "W"}
        self.bearing = 90
        self.position = {"N": 0, "E": 0, "S": 0, "W": 0}

    def manhattan_distance(self):
        return abs(self.position["N"] - self.position["S"]) + abs(self.position["E"] - self.position["W"])

    def rotate(self, direction: str, val: int):
        sign = {"R": 1, "L": -1}
        self.bearing += sign[direction] * val
        self.bearing = self.bearing % 360

    def advance(self, val):
        self.position[self.b_dir[self.bearing]] += val

    def move(self, instr: str, val: int):
        try:
            self.position[instr] += val
        except KeyError:
            if instr in {"R", "L"}:
                self.rotate(instr, val)
            else:
                self.advance(val)


class Ship2:

    def __init__(self):
        self.current_position = np.zeros(2, dtype=int)
        self.ship_waypoint = np.array([10, 1], dtype=int)

        self.instr_sign = {"N": 1, "E": 1, "S": -1, "W": -1, "L": 1, "R": -1}

    def manhattan_distance(self):
        return abs(self.current_position[0]) + abs(self.current_position[1])
    
    def rotate_waypoint(self, angle):
        angle = radians(angle)
        rot_mat = np.array([[cos(angle), -sin(angle)],
                            [sin(angle), cos(angle)]], dtype=int)
        self.ship_waypoint = rot_mat @ self.ship_waypoint

    def process_instr(self, instr: str, val: int):
        if instr in ["N", "S"]:
            self.ship_waypoint[1] += self.instr_sign[instr] * val
        elif instr in ["E", "W"]:
            self.ship_waypoint[0] += self.instr_sign[instr] * val
        elif instr in ["L", "R"]:
            self.rotate_waypoint(self.instr_sign[instr] * val)
        elif instr == "F":
            self.current_position += val * self.ship_waypoint
        else:
            raise ValueError("Unexpected instruction")


def day12_part1():
    with open("day12_input.txt") as f:
        ship = Ship()
        for instruction in f:
            instr = instruction[0]
            val = int((instruction.rstrip())[1:])
            ship.move(instr, val)
        return ship.manhattan_distance()


def day12_part2():
    with open("day12_input.txt") as f:
        ship = Ship2()
        for instruction in f:
            instr = instruction[0]
            val = int((instruction.rstrip())[1:])
            ship.process_instr(instr, val)
        return ship.manhattan_distance()


if __name__ == "__main__":
    print("=" * 10 + " Part 1 " + "=" * 10)
    print(f"Manhattan distance: {day12_part1()}")
    print("=" * 10 + " Part 2 " + "=" * 10)
    print(f"Manhattan distance: {day12_part2()}")
