with open('Prob05.in.txt') as f:
    file_contents = f.read()

lines = file_contents.split('\n')[1:]  # ignore first line (number of test cases)
while '' in lines:
    # no blank lines in input
    lines.remove('')

# build a representation of test cases with nested lists
test_cases = []
first_line = True  # token to tell whether we are on the first line or the second of each case
for line in lines:
    names = line.split(',')  # assumes no space on either side of comma
    if first_line:
        test_cases.append([names])
    else:
        test_cases[-1].append(names)
    first_line = not first_line  # flip the token


def output(people):
    """Accepts people as a list of strings."""
    print(','.join(sorted(people)))


for case in test_cases:
    last_year, this_year = case
    last_only = []
    this_only = []
    both = []
    for person in last_year:
        if person in this_year:
            both.append(person)
        else:
            last_only.append(person)

    for person in this_year:
        if person not in last_year:
            this_only.append(person)

    output(last_only)
    output(both)
    output(this_only)
