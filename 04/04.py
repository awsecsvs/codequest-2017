# The number will be less than or equal to 90.

LIMIT = 95  # just in case :)

FIB = [0, 1]
while len(FIB) < LIMIT:
    # solution is impractical for larger limits because of memory use but works fine in this context
    FIB.append(FIB[-2] + FIB[-1])

with open('Prob04.in.txt') as f:
    file_contents = f.read()

lines = file_contents.split('\n')[1:]  # ignore first line

while '' in lines:
    lines.remove('')  # ensure no empty lines

for inp in lines:
    out = '{} = {}'.format(inp, FIB[int(inp) - 1])  # subtract 1 to account for 0-indexing
    print(out)
