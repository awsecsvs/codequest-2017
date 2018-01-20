class Char:
    def __init__(self, letter):
        val = ord(letter.upper())
        self.val = val - 65

    def __repr__(self):
        return chr(self.val + 65)

    def shift(self, n):
        if isinstance(n, Char):
            n = n.val
        self.val = (self.val + n) % 26


with open('Prob09.in.txt') as f:
    file_contents = f.read()

lines = file_contents.split('\n')[1:]  # don't care about the number of tests
while '' in lines:
    lines.remove('')

# process input
tests = []
is_message = True  # flag to determine if this line is a message or a code
for l in lines:
    if is_message:
        tests.append([l])
    else:
        tests[-1].append(l)
    is_message = not is_message

for t in tests:
    msg, key = t
    key = [Char(l) for l in key]

    i = 0
    msg_l = []
    for l in msg:
        if l == ' ':
            c = ' '
        else:
            c = Char(l)
            c.shift(key[i])
            i += 1
            if i == len(key):
                i = 0
        msg_l.append(c)

    print(''.join(str(m) for m in msg_l))
