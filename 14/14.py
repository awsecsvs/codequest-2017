class File:
    def __init__(self, name):
        self.name = name
        self.kids = []

    def __repr__(self):
        return self.name


with open('Prob14.in.txt') as f:
    f.readline()  # I don't care how many files there are
    items = []
    while True:
        l = f.readline()
        if not l:
            break
        n, parnt = l.strip().split(',')
        items.append((n, parnt))

known_files = {'None': File('None')}


def handle(item):
    name, parent_name = item
    file = File(name)
    known_files[name] = file
    parent = known_files[parent_name]
    parent.kids.append(file)


for i in items:
    handle(i)


def print_tree(file, start=''):
    print(start + str(file))
    if file.kids:
        for k in sorted(file.kids, key=lambda x: x.name):
            print_tree(k, start + '-')


for kid in sorted(known_files['None'].kids, key=lambda x: x.name):
    print_tree(kid)
