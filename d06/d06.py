class DailyPuzzle06:
    def __init__(self):
        self.data = []

    def read_data(self):
        with open("./d06/input.txt") as f:
            self.data = f.readlines()

    def solve_part_one(self):
        groups = []
        group = set()
        for line in self.data:
            if line == "\n":
                groups.append(group)
                group = set()
            else:
                passenger = set(list(line[:-1]))
                group = group.union(passenger)

        groups.append(group)

        number_of_answers = map(len, groups)
        return sum(number_of_answers)

    def solve_part_two(self):
        groups = []
        group = set(list(self.data[0][:-1]))
        for idx, line in enumerate(self.data):
            if line == "\n":
                groups.append(group)
                group = set(list(self.data[idx + 1][:-1]))
            else:
                passenger = set(list(line[:-1]))
                group = group.intersection(passenger)

        groups.append(group)

        number_of_answers = map(len, groups)
        return sum(number_of_answers)
