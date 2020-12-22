import math


## extended euclidean algorithm (https://brilliant.org/wiki/extended-euclidean-algorithm/)
def egcd(a, b):
    tmp = abs(a * b)
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    lcm = tmp // gcd
    return gcd, lcm, x, y


class DailyPuzzle13:
    def __init__(self):
        self.timestamp = 0
        self.bids = []

    def read_data(self):
        with open("./d13/input.txt") as f:
            self.timestamp = int(f.readline())
            self.bids = [int(bid) if bid != "x" else 0 for bid in f.readline()[:-1].split(",")]

    def solve_part_one(self):
        wait_times = [bid - (self.timestamp) % bid for bid in filter(lambda x: x > 0, self.bids)]
        val, idx = min((val, idx) for (idx, val) in enumerate(wait_times))
        return val * self.bids[idx]

    def solve_part_two(self):
        offset = 0
        period = self.bids[0]
        for idx, bid in enumerate(self.bids[1:]):
            if bid == 0:
                continue
            else:
                # threat bus schedules as two period systems with individual offsets
                #  find intersection by extended euclidean algorithm to
                # first offset: intersection of considered buses so far
                # second offset: subsequent ticks later, detmined by index
                g, lcm, s, t = egcd(period, bid)
                z = (-offset - (idx + 1)) // g
                multiplier = z * s

                offset = (multiplier * period + offset) % lcm
                period = lcm

        return offset
