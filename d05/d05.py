class DailyPuzzle05:
    def __init__(self):
        self.data = []

    def read_data(self):
        with open("./d05/input.txt") as f:
            for line in f:
                row = 0
                for idx, letter in enumerate(reversed(line[0:7])):
                    if letter == "B":
                        row += 2 ** idx

                col = 0
                for idx, letter in enumerate(reversed(line[7:-1])):
                    if letter == "R":
                        col += 2 ** idx

                self.data.append({"row": row, "col": col})

    def solve_part_one(self):
        seat_ids = list(map(lambda seat: seat["row"] * 8 + seat["col"], self.data))
        return max(seat_ids)

    def solve_part_two(self):
        seat_ids = list(map(lambda seat: seat["row"] * 8 + seat["col"], self.data))
        seat_ids.sort()

        for idx in range(1, len(seat_ids)):
            if seat_ids[idx] - seat_ids[idx - 1] == 2:
                my_seat = seat_ids[idx] - 1

        return my_seat
