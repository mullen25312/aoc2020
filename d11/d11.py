import copy

class DailyPuzzle11:
    def __init__(self):
        self.data = []

    def read_data(self):
        with open("./d11/input.txt") as f:
            for idx, line in enumerate(f):
                tmp = []
                for pos in line[:-1]:
                    if pos == '.':
                        tmp.append(-1)
                    elif pos == 'L':
                        tmp.append(0) 
                    else:
                        tmp.append(1)
                    
                self.data.append(tmp)

    def solve_part_one(self):
        adjacent = [[1,0], [1,1], [0, 1], [0,-1], [-1,0], [1,-1], [-1,1], [-1,-1]]

        tmp_old = copy.deepcopy(self.data) 
        tmp_new = copy.deepcopy(self.data) 

        for round in range(0,120):

            for i, row in enumerate(tmp_old):
                for j, col in enumerate(row):

                    # count occupied neighbors
                    occupied = 0
                    for adj in adjacent:
                        if i+adj[0] < 0 or i+adj[0]>=len(tmp_old) or j+adj[1] < 0 or j+adj[1] >= len(row):
                            continue
                        if tmp_old[i+adj[0]][j+adj[1]] == 1:
                            occupied += 1

                    if tmp_old[i][j] == 0:
                        if occupied == 0:
                            tmp_new[i][j] = 1

                    elif tmp_old[i][j] == 1:
                        if occupied >= 4:
                            tmp_new[i][j] = 0

            tmp_old = copy.deepcopy(tmp_new)
            
            # for row in tmp_new:
            #     output = ''
            #     for pos in row:
            #         if pos == -1:
            #             output += '.'
            #         elif pos == 0:
            #             output += 'L'
            #         else:
            #             output += '#'
            #     print(output)
            # print('\n')

        return sum(row.count(1) for row in tmp_new)

    def solve_part_two(self):
        return ''
