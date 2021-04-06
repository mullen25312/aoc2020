class DailyPuzzle25:
    def __init__(self):
        self.data = []

    def read_data(self):
        with open("./d25/input.txt") as f:
            self.data = [int(line) for line in f]

    def solve_part_one(self):
        subject_number = 7
        mod_base = 20201227

        tmp = 1
        idx0 = 0
        while tmp != self.data[0]:
            tmp = (tmp*subject_number) % mod_base
            idx0 += 1

        tmp = 1
        idx1 = 0
        while tmp != self.data[1]:
            tmp = (tmp*subject_number) % mod_base
            idx1 += 1 

        key = 1
        for _ in range(idx0):
            key = (key*self.data[1]) % mod_base

        return idx0, idx1, key

    def solve_part_two(self):
        return ''

