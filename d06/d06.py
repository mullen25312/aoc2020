class DailyPuzzle06:
    def __init__(self):
        self.data = []

    def read_data(self):
        with open("./d06/input.txt") as f:

            groups = []
            group = []
            for line in f:
                if line == "\n":
                    groups.append(group)
                    group = []
                else:
                    passenger = set(list(line[:-1]))
                    group.append(passenger)

            groups.append(group)
        self.data = groups

    def solve_part_one(self):
        return sum(map(len, map(lambda group: set.union(*group), self.data)))

    def solve_part_two(self):
        return sum(map(len, map(lambda group: set.intersection(*group), self.data)))
