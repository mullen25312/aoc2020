from itertools import product
import copy

class DailyPuzzle17:
    def __init__(self):
        self.data = set()

    def read_data(self):
        with open("./d17/input.txt") as f:
            for y, line in enumerate(f):
                for x, pos in enumerate(line.strip()):
                    if pos == '#':
                        self.data.add((x,y,0))
                            
    def solve_part_one(self):
        neighbors = list(product([-1, 0, 1], repeat = 3))
        neighbors.remove((0,0,0))

        N = 6
        cubes_old = self.data.copy()
        cubes_new = set()

        for _ in range(N):

            cubes_new.clear()
            for cube in cubes_old:
                
                # rule 1
                tmp = 0
                for adj in neighbors:
                    x = cube[0]+adj[0]
                    y = cube[1]+adj[1]
                    z = cube[2]+adj[2]
                    if (x,y,z) in cubes_old:
                        tmp += 1 
                if tmp == 2 or tmp == 3:
                    cubes_new.add(cube)

                # rule 2
                for adj in neighbors:
                    x = cube[0]+adj[0]
                    y = cube[1]+adj[1]
                    z = cube[2]+adj[2]
                    if (x,y,z) in cubes_old:
                        continue
                    tmp = 0
                    for adjadj in neighbors:
                        xx = x + adjadj[0]
                        yy = y + adjadj[1]
                        zz = z + adjadj[2]
                        if (xx,yy,zz) in cubes_old:
                            tmp += 1 
                    if tmp == 3:
                        cubes_new.add((x,y,z))

            cubes_old = cubes_new.copy()

        return len(cubes_old)

    def solve_part_two(self):
        neighbors = list(product([-1, 0, 1], repeat = 4))
        neighbors.remove((0,0,0,0))

        N = 6

        cubes_old = set()
        for data in self.data:
            cubes_old.add((data[0], data[1], data[2], 0))

        cubes_new = set()

        for _ in range(N):

            cubes_new.clear()
            for cube in cubes_old:
                
                # rule 1
                tmp = 0
                for adj in neighbors:
                    x = cube[0]+adj[0]
                    y = cube[1]+adj[1]
                    z = cube[2]+adj[2]
                    w = cube[3]+adj[3]
                    if (x,y,z,w) in cubes_old:
                        tmp += 1 
                if tmp == 2 or tmp == 3:
                    cubes_new.add(cube)

                # rule 2
                for adj in neighbors:
                    x = cube[0]+adj[0]
                    y = cube[1]+adj[1]
                    z = cube[2]+adj[2]
                    w = cube[3]+adj[3]
                    if (x,y,z,w) in cubes_old:
                        continue
                    tmp = 0
                    for adjadj in neighbors:
                        xx = x + adjadj[0]
                        yy = y + adjadj[1]
                        zz = z + adjadj[2]
                        ww = w + adjadj[3]
                        if (xx,yy,zz,ww) in cubes_old:
                            tmp += 1 
                    if tmp == 3:
                        cubes_new.add((x,y,z,w))

            cubes_old = cubes_new.copy()

        return len(cubes_old)
