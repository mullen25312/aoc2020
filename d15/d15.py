class DailyPuzzle15:
    def __init__(self):
        self.data = {}

    def read_data(self):
        with open("./d15/input.txt") as f:
            # self.data = [line for line in f]
            self.data = [int (n) for n in f.readline()[:-1].split(',')]

    def solve_part_one(self):
        spoken_dict = {}
        last = 0
        for idx, number in enumerate(self.data[:-1]):
            spoken_dict[number] = idx
        last = self.data[-1]

        N = 2020
        spoken = 0
        for idx in range(len(spoken_dict)-1,N-2):
            if last in spoken_dict.keys():
                spoken = idx+1 - spoken_dict[last] 
            else: 
                spoken = 0

            spoken_dict[last] = idx+1 
            last = spoken

        return spoken

    def solve_part_two(self):
        spoken_dict = {}
        last = 0
        for idx, number in enumerate(self.data[:-1]):
            spoken_dict[number] = idx
        last = self.data[-1]

        N = 30000000
        spoken = 0
        for idx in range(len(spoken_dict)-1,N-2):
            if last in spoken_dict.keys():
                spoken = idx+1 - spoken_dict[last] 
            else: 
                spoken = 0

            spoken_dict[last] = idx+1 
            last = spoken

        return spoken
