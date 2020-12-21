class DailyPuzzle10:
    def __init__(self):
        self.data = []

    def read_data(self):
        with open("./d10/input.txt") as f:
            self.data = [int(line) for line in f]
            self.data.sort()
            self.data.insert(0, 0)
            self.data.append(self.data[-1]+3)

    def solve_part_one(self): 
        diffs = [0 for n in range(len(self.data)-1)]
        for idx in range(len(self.data)-1):
            diffs[idx] = self.data[idx+1]-self.data[idx] 

        one_jolt_diffs = sum(diff==1 for diff in diffs)
        three_jolt_diffs = sum(diff==3 for diff in diffs)
        return one_jolt_diffs*three_jolt_diffs

    def solve_part_two(self):
        diffs = [0 for n in range(len(self.data)-1)]
        for idx in range(len(self.data)-1):
            diffs[idx] = self.data[idx+1]-self.data[idx] 

        last = -1
        combinations = 1
        for idx, diff in enumerate(diffs):
            if diff == 3:
                if idx != last+1:
                    num_of_ones = idx-last-1
                    if num_of_ones <= 3:
                        combinations *= 2**(num_of_ones-1)
                    elif num_of_ones == 4:
                        combinations = combinations*7
                    else:
                        return 'we got a problem'
                last = idx
        return combinations
