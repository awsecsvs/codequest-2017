with open('Prob06.in.txt') as f:
    file_contents = f.read()

lines = file_contents.split('\n')[1:]  # ignore the first line. I don't care how many test cases there are.

# process input
# we don't care how long each test is; we'll print our output just the same
tests = []
for l in lines:
    if not l.isnumeric():
        tests.append(l.lower())  # lower all input and ignore case

while '' in tests:
    tests.remove('')  # don't want blank lines in there

d = {'a': 'Alpha', 'b': 'Bravo', 'c': 'Charlie', 'd': 'Delta', 'e': 'Echo', 'f': 'Foxtrot', 'g': 'Golf', 'h': 'Hotel',
     'i': 'India', 'j': 'Juliet', 'k': 'Kilo', 'l': 'Lima', 'm': 'Mike', 'n': 'November', 'o': 'Oscar', 'p': 'Papa',
     'q': 'Quebec', 'r': 'Romeo', 's': 'Sierra', 't': 'Tango', 'u': 'Uniform', 'v': 'Victor', 'w': 'Whiskey',
     'x': 'Xray', 'y': 'Yankee', 'z': 'Zulu', }

# known to not preserve more than one space
for case in tests:
    words_in = case.split()
    words_out = []
    for word in words_in:
        out = '-'.join(d[l] for l in word)
        words_out.append(out)
    print(' '.join(words_out))
