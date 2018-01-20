def slg(singles, doubles, triples, hrs, atbats):
    if atbats == 0:
        return 0
    return (singles + 2 * doubles + 3 * triples + 4 * hrs) / atbats


def parse_and_calc(line):
    line = line.strip()  # remove extra whitespace
    name, atbats = line.split(':')
    atbats = atbats.split(',')

    singles = doubles = triples = hrs = ab_count = 0  # trick only works with immutable types

    for bat in atbats:
        if bat == 'BB':
            continue
        elif bat == 'K':
            pass
        elif bat == '1B':
            singles += 1
        elif bat == '2B':
            doubles += 1
        elif bat == '3B':
            triples += 1
        elif bat == 'HR':
            hrs += 1
        else:
            # safeguard against unknown events
            raise ValueError('Unknown at-bat type {!r}'.format(bat))
        ab_count += 1

    score = slg(singles, doubles, triples, hrs, ab_count)
    return name, score


with open('Prob07.in.txt') as f:
    lines = f.readlines()

for l in lines:
    if ':' not in l:
        continue
    name, perc = parse_and_calc(l)
    print('{}={:.3f}'.format(name, perc))
