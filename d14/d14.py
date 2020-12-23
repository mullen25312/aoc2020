import itertools


class DailyPuzzle14:
    def __init__(self):
        self.data = []

    def read_data(self):
        with open("./d14/input.txt") as f:
            self.data = [line for line in f]

    def solve_part_one(self):
        mem = {}
        mask_ones = 2 ** 36
        mask_zeros = 0
        for instruction in self.data:
            com = instruction.split("=")[0].strip()
            arg = instruction.split("=")[1].strip()

            if com == "mask":
                mask_ones = int("".join(["1" if bit == "1" else "0" for bit in arg]), 2)  # for or
                mask_zeros = int("".join(["0" if bit == "0" else "1" for bit in arg]), 2)  # for and

            else:
                mem[int(com[4:-1])] = (int(arg) | mask_ones) & mask_zeros

        return sum(mem.values())

    def solve_part_two(self):
        mem = {}
        for instruction in self.data:
            com = instruction.split("=")[0].strip()
            arg = instruction.split("=")[1].strip()
            if com == "mask":
                tmp = [["0", "1"] if (c == "X") else c for c in arg]
                combs = ["".join(lst) for lst in list(itertools.product(*tmp))]
                mask_ones = "".join(["1" if bit == "1" else "0" for bit in arg])
                mask_xses = "".join(["0" if bit == "X" else "1" for bit in arg])
            else:
                base_address = (int(com[4:-1]) | int(mask_ones, 2)) & int(mask_xses, 2)
                for comb in combs:
                    mem[base_address | int(comb, 2)] = int(arg)
        return sum(mem.values())
