import math
import re

# regular expression for parsing input
reg_expr1 = r"(\d+)"
reg_expr2 = r"([a-z]:)"
reg_expr3 = r"([a-z][a-z]+)"


class DailyPuzzle02:
    def __init__(self):
        self.data = []

    def read_data(self):
        with open("./d02/input.txt") as f:
            lines = f.readlines()
            for line in lines:
                tmp = re.findall(reg_expr1, line)
                letter = re.findall(reg_expr2, line)[0][0]
                password = re.findall(reg_expr3, line)[0]
                line_dict = {"min": int(tmp[0]), "max": int(tmp[1]), "letter": letter, "password": password}
                self.data.append(line_dict)

    def solve_part_one(self):
        cnt = 0
        for line in self.data:
            if line["min"] <= line["password"].count(line["letter"]) <= line["max"]:
                cnt = cnt + 1
        return cnt

    def solve_part_two(self):
        cnt = 0
        for line in self.data:
            if (line["password"][line["min"] - 1] == line["letter"]) ^ (line["password"][line["max"] - 1] == line["letter"]):
                cnt = cnt + 1
        return cnt
