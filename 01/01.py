with open('Prob01.in.txt') as f:
    f.readline()  # ignore the first line
    while True:
        l = f.readline().strip()
        if not l:
            break
        print(l)
        print(l)
