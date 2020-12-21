sin_table = {0: 0, 1: 1, 2: 0, 3: -1}
cos_table = {0: 1, 1: 0, 2: -1, 3: 0}


class DailyPuzzle12:
    def __init__(self):
        self.data = []

    def read_data(self):
        with open("./d12/input.txt") as f:
            for line in f:
                self.data.append([line[0], int(line[1:-1])])

    def solve_part_one(self):
        x, y, face = 0, 0, 0

        for instruction in self.data:
            com = instruction[0]
            arg = instruction[1]
            if com == "N":
                y += arg
            elif com == "S":
                y -= arg
            elif com == "E":
                x += arg
            elif com == "W":
                x -= arg
            elif com == "L":
                face = (face - int(arg / 90)) % 4
            elif com == "R":
                face = (face + int(arg / 90)) % 4
            elif com == "F":
                x += ((face + 1) % 2) * arg * (1 - face)
                y += (face % 2) * arg * (face - 2)

        return abs(x) + abs(y)

    def solve_part_two(self):
        dx, dy = 10, 1
        xs, ys = 0, 0

        for instruction in self.data:
            com = instruction[0]
            arg = instruction[1]
            if com == "N":
                dy += arg
            elif com == "S":
                dy -= arg
            elif com == "E":
                dx += arg
            elif com == "W":
                dx -= arg
            elif com == "L":
                angle = -int(arg / 90) % 4
                tmp = cos_table[angle] * dx + sin_table[angle] * dy
                dy = -sin_table[angle] * dx + cos_table[angle] * dy
                dx = tmp

            elif com == "R":
                angle = int(arg / 90) % 4
                tmp = cos_table[angle] * dx + sin_table[angle] * dy
                dy = -sin_table[angle] * dx + cos_table[angle] * dy
                dx = tmp

            elif com == "F":
                xs += arg * dx
                ys += arg * dy

        return abs(xs) + abs(ys)
