import copy

class Handheld:
    def __init__(self, program):
        self.acc = 0
        self.ip = 0
        self.ips = set()
        self.program = program

    def run(self):
        while self.ip not in self.ips:
            if self.ip == len(self.program):
                return True
            self.ips.add(self.ip)
            instruction = self.program[self.ip][0]
            argument = self.program[self.ip][1]

            if instruction == 'acc':
                self.acc += argument
                self.ip += 1
            elif instruction == 'jmp':
                self.ip += argument
            else:
                self.ip += 1

        return False


    def get_acc(self):
        return self.acc

class DailyPuzzle08:
    def __init__(self):
        self.data = []

    def read_data(self):
        with open("./d08/input.txt") as f:
            for line in f:
                instruction = line.split(' ')[0]
                argument = int(line.split(' ')[1])
                self.data.append([instruction, argument])

    def solve_part_one(self):
        mHandheld = Handheld(self.data)
        mHandheld.run()
        return mHandheld.get_acc()

    def solve_part_two(self):
        for idx in range(len(self.data)):
            instructions = copy.deepcopy(self.data)
            if instructions[idx][0] == 'nop':
                instructions[idx][0] = 'jmp'
            elif instructions[idx][0] == 'jmp':
                instructions[idx][0] = 'nop'
            else:
                continue

            mHandheld = Handheld(instructions)
            if mHandheld.run():
                return mHandheld.get_acc()

        return 'unsuccessful'
