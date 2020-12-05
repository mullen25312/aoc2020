import re

reg_yr = r"([0-9]{4})"
reg_hgt = r"([0-9]{2,3}(in|cm))"
reg_hcl = r"(#[0-9a-z]{6})"
reg_ecl = r"(amb|blu|brn|gry|grn|hzl|oth)"
reg_pid = r"([0-9]{9})"


def check_byr(value):
    if re.fullmatch(reg_yr, value):
        if 1920 <= int(value) <= 2002:
            return True
    return False


def check_iyr(value):
    if re.fullmatch(reg_yr, value):
        if 2010 <= int(value) <= 2020:
            return True
    return False


def check_eyr(value):
    if re.fullmatch(reg_yr, value):
        if 2020 <= int(value) <= 2030:
            return True
    return False


def check_hgt(value):
    if re.fullmatch(reg_hgt, value):
        num = int(value[0:-2])
        unit = value[-2:]
        if (unit == "cm" and (150 <= num <= 193)) or (unit == "in" and (59 <= num <= 76)):
            return True
    return False


def check_hcl(value):
    return bool(re.fullmatch(reg_hcl, value))


def check_ecl(value):
    return bool(re.fullmatch(reg_ecl, value))


def check_pid(value):
    return bool(re.fullmatch(reg_pid, value))


class DailyPuzzle04:
    def __init__(self):
        self.data = []

    def read_data(self):
        with open("./d04/input.txt") as f:

            tmp = {}
            for line in f:
                if line == "\n":
                    self.data.append(tmp)
                    tmp = {}
                else:
                    entries = line[0:-1].split(" ")
                    for entry in entries:
                        key, value = entry.split(":")
                        tmp[key] = value

            self.data.append(tmp)

    def solve_part_one(self):
        required_field = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
        cnt = 0
        for passport in self.data:
            if required_field.issubset(passport):
                cnt += 1
        return cnt

    def solve_part_two(self):
        required_field = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
        cnt = 0
        for passport in self.data:
            if required_field.issubset(passport):
                if check_byr(passport["byr"]) and check_iyr(passport["iyr"]) and check_eyr(passport["eyr"]) and check_hgt(passport["hgt"]) and check_hcl(passport["hcl"]) and check_ecl(passport["ecl"]) and check_pid(passport["pid"]):
                    cnt += 1
        return cnt
