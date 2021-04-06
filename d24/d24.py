import re
import copy
reg_expr = r"(e|se|sw|w|nw|ne)"

trans_odd  = {'e': (1, 0), 'se': (1, -1), 'sw':( 0,-1), 'w': (-1, 0), 'nw': ( 0, 1), 'ne': (1, 1)}
trans_even = {'e': (1, 0), 'se': (0, -1), 'sw':(-1,-1), 'w': (-1, 0), 'nw': (-1, 1), 'ne': (0, 1)}


class DailyPuzzle24:
    def __init__(self):
        self.data = []

    def read_data(self):
        with open("./d24/input.txt") as f:
            for line in f:
                self.data.append(re.findall(reg_expr, line.strip()))

    def solve_part_one(self):
        tiles = set()
        for tile in self.data:
            pos = [0, 0]
            for trans in tile:
                if pos[1] % 2 == 0:
                    pos[0] += trans_even[trans][0]
                    pos[1] += trans_even[trans][1]
                else:
                    pos[0] += trans_odd[trans][0]
                    pos[1] += trans_odd[trans][1]
                
            if tuple(pos) not in tiles:
                tiles.add(tuple(pos))
            else:
                tiles.remove(tuple(pos))

        return len(tiles)

    def solve_part_two(self):
        tiles = set()
        for tile in self.data:
            pos = [0, 0]
            for trans in tile:
                if pos[1] % 2 == 0:
                    pos[0] += trans_even[trans][0]
                    pos[1] += trans_even[trans][1]
                else:
                    pos[0] += trans_odd[trans][0]
                    pos[1] += trans_odd[trans][1]
                
            if tuple(pos) not in tiles:
                tiles.add(tuple(pos))
            else:
                tiles.remove(tuple(pos))

        N = 100
        tiles_old = copy.deepcopy(tiles)
        tiles_new = copy.deepcopy(tiles)
        for idx in range(N):
            tiles_new.clear()
            for tile in tiles_old:
                ## check for rule 1
                tmp = 0
                trans = trans_even if tile[1] % 2 == 0 else trans_odd
                for adj in trans.values():
                    x = tile[0]+adj[0]
                    y = tile[1]+adj[1]
                    if (x,y) in tiles_old:
                        tmp += 1
                if tmp == 0 or tmp > 2:
                    pass
                else:
                    tiles_new.add(tile)

                ## check for rule 2
                trans = trans_even if tile[1] % 2 == 0 else trans_odd
                for adj in trans.values():
                    if (tile[0]+adj[0], tile[1]+adj[1]) in tiles_old:
                        continue
                    y = tile[1]+adj[1]
                    transtrans = trans_even if y % 2 == 0 else trans_odd
                    tmp = 0
                    for adjadj in transtrans.values():
                        xx = tile[0] + adj[0] + adjadj[0]
                        yy = tile[1] + adj[1] + adjadj[1]
                        if (xx,yy) in tiles_old:
                            tmp += 1
                    if tmp == 2:
                        tiles_new.add((tile[0]+adj[0], tile[1]+adj[1]))

            tiles_old = copy.deepcopy(tiles_new)
            # print(len(tiles_new))

        return len(tiles_new)

