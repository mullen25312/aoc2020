import math


class DailyPuzzle03:
    def __init__(self):
        self.data = []

    def read_data(self):
        with open("./d03/input.txt") as f:
            lines = f.readlines()

            tmp = [[""] * (len(lines[0]) - 1) for i in range(len(lines))]
            for idx1, line in enumerate(lines):
                for idx2, letter in enumerate(line[0:-1]):
                    tmp[idx1][idx2] = letter

        self.data = tmp

    def solve_part_one(self):
        N = len(self.data)
        M = len(self.data[0])
        x, y, cnt = 0, 0, 0
        while y < N:
            if self.data[y][x % M] == "#":
                cnt = cnt + 1
            x = x + 3
            y = y + 1

        return cnt

    def solve_part_two(self):
        N = len(self.data)
        M = len(self.data[0])
        slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
        prod = 1

        for slope in slopes:
            x, y, cnt = 0, 0, 0
            while y < N:
                if self.data[y][x % M] == "#":
                    cnt = cnt + 1
                x = x + slope[0]
                y = y + slope[1]
            prod = prod * cnt

        return prod
