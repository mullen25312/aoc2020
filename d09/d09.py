import itertools

class DailyPuzzle09:
    def __init__(self):
        self.data = []

    def read_data(self):
        with open("./d09/input.txt") as f:
            self.data = [int(line) for line in f]

    def solve_part_one(self):
        preamble = 25
        for idx, number in enumerate(self.data):
            if idx <= preamble: 
                continue
            else:
                sums = [pair[0] + pair[1] for pair in itertools.combinations(self.data[idx-preamble:idx], 2)]
                if number not in sums:
                    return number
                
        return 'all are valid'

    def solve_part_two(self):
        sol = 14360655
        for idx in range(len(self.data)):
            sequence = []
            idx2 = 0
            while sum(sequence) < sol:
                sequence.append(self.data[idx+idx2])
                idx2 += 1
                if sum(sequence) == sol:
                    return min(sequence) + max(sequence)

        return 'number not found'
