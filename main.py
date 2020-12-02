# my solutions to the Advent of Code 2020
# https://adventofcode.com/2020
# https://github.com/mullen25312/aoc2020


from d01.d01 import DailyPuzzle01
from d02.d02 import DailyPuzzle02

# from d03.d03 import DailyPuzzle03


def main():

    # day1
    d01 = DailyPuzzle01()
    d01.read_data()
    print("Solutions of daily puzzle 01:")
    print(d01.solve_part_one())
    print(d01.solve_part_two())
    print()

    # day2
    d02 = DailyPuzzle02()
    d02.read_data()
    print("Solutions of daily puzzle 02:")
    print(d02.solve_part_one())
    print(d02.solve_part_two())
    print()


if __name__ == "__main__":
    main()
