def reslice(l, i):
    """Slice the list l at i and loop back around to i-1"""
    return l[i:] + l[:i + 1]


def solve(tanks):
    target = sum(tanks) / len(tanks)

    best = 1e999  # large number

    for i in range(len(tanks)):
        sl = reslice(tanks, i)

        spouts = 0

        total = 0
        count = 0

        for tank in sl:
            total += tank
            count += 1
            if total / count == target:
                spouts += count - 1
                total = count = 0

        best = min(spouts, best)
    return best


class Site:
    def __init__(self, name, tanks):
        self.name = name
        self.tanks = tanks

    def __repr__(self):
        return '{}: {}'.format(self._abbrev(), solve(self.tanks))

    def _abbrev(self):
        return ''.join(w[0] for w in self.name.split())


with open('Prob18.in.txt') as f:
    len_tests = int(f.readline())
    tests = []
    for _ in range(len_tests):
        name = f.readline().strip()
        tanks_ = [int(x) for x in f.readline().split()][1:]  # lop off the tank count — we don't care.
        tests.append(Site(name, tanks_))

for t in tests:
    print(t)
