with open('Prob03.in.txt') as f:
    file_contents = f.read()

lines = file_contents.split('\n')[1:]  # ignore first line of input
while '' in lines:
    # ensure no blank lines
    lines.remove('')

for l in lines:
    a, b = l.split(' ')
    a, b = int(a), int(b)
    print(a + b, a * b)
