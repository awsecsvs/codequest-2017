def process(line):
    in_word = False

    def rev(word):
        r = reversed(word)
        o = []
        for ol, nl in zip(word, r):
            if ol.isupper():
                o.append(nl.upper())
            else:
                o.append(nl.lower())
        return ''.join(o)

    isalpha = [c.isalpha() for c in line]
    out = []
    i = -1
    for a, c in zip(isalpha, line):
        i += 1
        if not a:
            out.append(c)
            in_word = False
        else:
            if in_word:
                continue
            w = c
            i_copy = i + 1
            while i_copy != len(line) and isalpha[i_copy]:
                w += line[i_copy]
                i_copy += 1
            out.append(rev(w))
            in_word = True

    return ''.join(out)


with open('Prob11.in.txt') as f:
    lines = f.read().split('\n')

for l in lines:
    if l and not l.isnumeric():
        print(process(l))
