with open('Prob02.in.txt') as f:
    file_contents = f.read()

lines = file_contents.split('\n')
lines = lines[1:]  # remove the first line because we don't care about the number of tests

while '' in lines:
    # make sure we don't have any blank lines; that will cause our program to crash in the next step.
    lines.remove('')

# processing input
pairs = []
for l in lines:
    word, ind = l.split(' ')
    ind = int(ind)
    pairs.append((word, ind))

# actually solving the problem
for word, ind in pairs:
    out = word[:ind] + word[ind + 1:]  # out of range slice indices do not throw errors
    print(out)
