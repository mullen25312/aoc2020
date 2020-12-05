class DailyPuzzle01:
    def __init__(self):
        self.data = []

    def read_data(self):
        with open("./d01/input.txt") as f:
            self.data = [int(line) for line in f]

    def solve_part_one(self):
        for idx1, num1 in enumerate(self.data):
            for idx2, num2 in enumerate(self.data):
                if idx1 == idx2:
                    break
                if num1 + num2 == 2020:
                    return num1 * num2
        return "No two numbers that add up to 2020 have been found"

    def solve_part_two(self):
        for idx1, num1 in enumerate(self.data):
            for idx2, num2 in enumerate(self.data):
                for idx3, num3 in enumerate(self.data):
                    if idx1 == idx2 or idx1 == idx2 or idx1 == idx3:
                        break
                    if num1 + num2 + num3 == 2020:
                        return num1 * num2 * num3
        return "No three numbers that add up to 2020 have been found"
