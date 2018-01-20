with open('Prob08.in.txt') as f:
    file_contents = f.read()

lines = file_contents.split('\n')[1:]  # ignore first line
while '' in lines:
    # don't want them
    lines.remove('')


def time_formatter(seconds):
    s = int(round(seconds, 0))  # follows CQ rounding rules above 0
    m = s // 60
    s = s % 60
    h = m // 60
    m = m % 60
    d = h // 24
    h = h % 24
    return 'Time to Mars: {} days, {} hours, {} minutes, {} seconds'.format(d, h, m, s)


for l in lines:
    d, r = l.split()
    d = float(d) * 1000000  # to miles (from millions of miles)
    r = float(r)
    t = d / r  # in hours
    t *= 3600  # to seconds

    print(time_formatter(t))
