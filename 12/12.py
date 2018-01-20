def tryfloat(s):
    if s and not s.isspace():
        return float(s)
    return 0.0


with open('Prob12.in.txt') as f:
    num_tests = int(f.readline())
    tests = []
    for _ in range(num_tests):
        test_len = int(f.readline())
        this_test = []
        for __ in range(test_len):
            daynum, charges, payments = (tryfloat(x) for x in f.readline().split(','))
            daynum = int(daynum)
            this_test.append((daynum, charges, payments))
        tests.append(this_test)


def solve(test):
    ledger = [0]
    for day in test:
        ch, py = day[1:3]
        ledger.append(ledger[-1] + ch - py)
    del ledger[0]  # extra value added in the beginning for continuity :)
    interest = monthly_interest(ledger)
    return '${:.2f}'.format(interest)


def monthly_interest(ledger):
    avg_bal = sum(ledger) / len(ledger)
    i_over_p = .18 / 12
    return avg_bal * i_over_p


for t in tests:
    print(solve(t))
