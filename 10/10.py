row_1_norm = 'wertyuiop'
row_1_shift = 'qwertyuio'
row_2_norm = 'sdfghjkl'
row_2_shift = 'asdfghjk'
row_3_norm = 'xcvbnm,.'
row_3_shift = 'zxcvbnm,'

NONSPECIAL_LETTERS = row_1_norm + row_2_norm + row_3_norm
NONSPECIAL_SHIFTS = row_1_shift + row_2_shift + row_3_shift


class Keyboard:
    def __init__(self):
        self.capslock = False
        self.out = ''
        self.new = True

    def use(self, s):
        self.new = False
        for l in s:
            self._type(l)

    def _type(self, l):
        if l == ' ':
            self.out += ' '
            return
        if l.lower() in NONSPECIAL_LETTERS:
            i = NONSPECIAL_LETTERS.index(l.lower())
            o = NONSPECIAL_SHIFTS[i]
            if l.isupper():
                self._add_letter(o.upper())
            else:
                self._add_letter(o)
        else:
            if l.lower() == 'q':
                self.out += '    '
            if l.lower() == 'a':
                self.capslock = not self.capslock
            if l.lower() == 'z':
                pass  # nothing happens; equivalent to pressing shift

    def _add_letter(self, letter):
        if not self.capslock:
            self.out += letter
        else:
            if letter.isupper():
                self.out += letter.lower()
            else:
                self.out += letter.upper()


with open('Prob10.in.txt') as f:
    contents = f.read()

lines = contents.split('\n')[2:]  # we ignore the first two lines for proper output formatting
while '' in lines:
    lines.remove('')

k = Keyboard()
for l in lines:
    if l.isnumeric():
        print(k.out)
        # new block, new keyboard
        k = Keyboard()
    else:
        if not k.new:
            k.out += '\n'
        k.use(l)
print(k.out)  # last block doesn't end in a number
