class DailyPuzzle19:
    def __init__(self):
        self.rules = {}
        self.data = []

    def read_data(self):
        with open("./d19/input.txt") as f:
            rules_finished = False
            for line in f:
                if rules_finished == False:
                    if line == '\n':
                        rules_finished = True
                    else:
                        num = int(line.split(':')[0].strip())
                        rule = line.split(':')[1].strip()
                        self.rules[num] = rule
                else:
                    self.data.append(line.strip())

        # print(self.rules)
        # print(self.data)

    def solve_part_one(self):
        return ''
    def solve_part_two(self):
        return ''
