X = 'X'
O = 'O'


# I am always X

class State:
    @classmethod
    def parse_from_text(cls, text):
        cleaned = text.replace('\n', '')
        return cls(list(cleaned))

    def __init__(self, spaces, my_turn=True):
        self.spaces = spaces
        assert len(self.spaces) == 9
        self.my_turn = my_turn  # aka X's turn
        self.children = []
        if self.winner() is None:
            self.make_children()

    def __repr__(self):
        return ''.join(self.spaces)

    def __str__(self):
        return '{}{}{}\n{}{}{}\n{}{}{}'.format(*self.spaces)

    def winner(self):
        s = self.spaces  # alias for easier typing
        if s[0] == s[1] == s[2] != '*':
            return s[0]
        if s[3] == s[4] == s[5] != '*':
            return s[3]
        if s[6] == s[7] == s[8] != '*':
            return s[6]

        if s[0] == s[3] == s[6] != '*':
            return s[0]
        if s[1] == s[4] == s[7] != '*':
            return s[1]
        if s[2] == s[5] == s[8] != '*':
            return s[2]

        if s[0] == s[4] == s[8] != '*':
            return s[0]
        if s[2] == s[4] == s[6] != '*':
            return s[2]

        return None

    def get_score(self):
        w = self.winner()
        if w == X:
            return 1
        elif w == O:
            return -1
        elif '*' not in self.spaces:
            # draw
            return 0
        else:
            children_scores = [s.get_score() for s in self.children]
            if self.my_turn:
                return max(children_scores)
            else:
                return min(children_scores)

    def make_children(self):
        for i, s in enumerate(self.spaces):
            if s == '*':
                spaces_copy = self.spaces.copy()
                spaces_copy[i] = X if self.my_turn else O
                self.children.append(State(spaces_copy, not self.my_turn))

    def pick_move(self):
        for s in self.children:
            if s.winner() == X:
                return s
        child_scores = [s.get_score() for s in self.children]
        for desired in range(1, -2, -1):
            for b, s in zip(self.children, child_scores):
                if s == desired:
                    return b


with open('Prob17.in.txt') as f:
    f.readline()  # don't care about the first line
    tests = []
    while True:
        l = f.readline()
        if not l:
            break
        tests.append(l + f.readline() + f.readline())  # three lines at once, contatenated

for t in tests:
    print(State.parse_from_text(t).pick_move())
