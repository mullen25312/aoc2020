class DailyPuzzle23:
    def __init__(self):
        self.data = []

    def read_data(self):
        with open("./d23/input.txt") as f:
            self.data = [int(n) for n in f.readline().strip()]

    def solve_part_one(self):
        # cups = self.data.copy()
        N = len(self.data)

        cups = {}
        for idx, cup in enumerate(self.data):
            cups[cup] = self.data[(idx + 1)  % N]

        current = self.data[0]

        for _ in range(100):
            # remove pick up
            tmp = [cups[current], cups[cups[current]], cups[cups[cups[current]]]]
            cups[current] = cups[cups[cups[cups[current]]]]
            
            # destination
            diff = -1
            while (current+diff) % (N+1) not in cups.keys() or (current+diff) % (N+1) in tmp:
                diff -= 1
            dest = (current+diff) % (N+1)

            # insert pick up
            cups[tmp[2]] = cups[dest]
            cups[dest] = tmp[0]
            
            # prepare next round
            current = cups[current]
            
            # debug print
            # debug = [current]
            # for _ in range(len(cups)-1):
            #     debug.append(cups[debug[-1]])

            # print("{0:s} --> sel: {1:d}, pick up: {2:s}, dest: {3:d}".format(str(debug), current, str(tmp), dest))

        result = [1]
        for _ in range(len(cups)-1):
            result.append(cups[result[-1]])
        return ''.join([str(n) for n in result[1:]])

    def solve_part_two(self):
        cups = {}
        for idx, cup in enumerate(self.data):
            if idx < len(self.data)-1:
                cups[cup] = self.data[(idx + 1)]
            else:
                cups[cup] = idx + 2
        
        M = 1000000
        for idx in range(10, M+1):
            cups[idx] = (idx+1)

        cups[M] = self.data[0]

        N = len(cups)
        current = self.data[0]

        # debug = [[current, cups[current]]]
        # for _ in range(len(cups)-1):
        #     debug.append([cups[debug[-1][0]], cups[cups[debug[-1][0]]]])
        # print(debug)
        
        for _ in range(10000000):
            # remove pick up
            tmp = [cups[current], cups[cups[current]], cups[cups[cups[current]]]]
            cups[current] = cups[cups[cups[cups[current]]]]
            
            # destination
            diff = -1
            while (current+diff) % (N+1) not in cups.keys() or (current+diff) % (N+1) in tmp:
                diff -= 1
            dest = (current+diff) % (N+1)

            # insert pick up
            cups[tmp[2]] = cups[dest]
            cups[dest] = tmp[0]
            
            # prepare next round
            current = cups[current]
            
        return cups[1]*cups[cups[1]]


