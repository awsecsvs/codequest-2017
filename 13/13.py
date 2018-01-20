TARGET = 1000 / 90  # ms/frame
LOW_THRESH = .7 * TARGET
EXTR_THRESH = TARGET * .85
HIGH_THRESH = .9 * TARGET

with open('Prob13.in.txt') as f:
    f.readline()
    tests = []
    while True:
        l = f.readline()
        if not l:
            break
        oh, one, two, qual = (float(t) for t in l.split())
        qual = int(qual)
        tests.append((oh, one, two, qual))


def run(test):
    *times, q = test
    if times[-1] > HIGH_THRESH:
        return max(q - 2, 1)
    elif times[-1] > EXTR_THRESH:
        if fails_extr(times):
            return max(q - 2, 1)
        return q
    elif max(times) < LOW_THRESH:
        return min(q + 1, 10)
    return q


def fails_extr(times):
    def calc(x1, y1, x2, y2):
        frac = (3 - x1) / (x2 - x1)
        return y1 + frac * (y2 - y1)

    # both go through point two
    zero = calc(0, times[0], 2, times[2])
    one_ = calc(1, times[1], 2, times[2])

    return max(zero, one_) > HIGH_THRESH


for t in tests:
    print(run(t))
