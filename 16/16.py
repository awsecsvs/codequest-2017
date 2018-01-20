M, D, A, S = '*/+-'


def solve(nums, ops, goal):
    true_nums = [float(x) for x in nums.split(',')]
    true_ops = list(ops)
    if len(true_nums) - 1 != len(ops):
        return False
    if len(ops) == 0:
        if true_nums[0] == goal:
            return True
    if M in ops:
        for i, a in enumerate(true_nums):
            for b in true_nums[i + 1:]:
                if handoff(true_nums, true_ops, goal, a, b, M, a * b):
                    return True
    if D in ops:
        for ia, a in enumerate(true_nums):
            for ib, b in enumerate(true_nums):
                if ia == ib:
                    continue
                if b == 0:
                    continue
                if handoff(true_nums, true_ops, goal, a, b, D, a / b):
                    return True

    # If we've tried every use of mult and div and still haven't found a solution, we have failed. In other words,
    # we may only progress on to using addition and subtraction once we have done all multiplication and division,
    # because we are not allowed parentheses. If we still have some * or / operators left, and we enter the + and -
    # sections, we will be performing those operations, then doing * or / in our recursion. Not allowed.
    if M in ops or D in ops:
        return False

    if A in ops:
        for i, a in enumerate(true_nums):
            for b in true_nums[i + 1:]:
                if handoff(true_nums, true_ops, goal, a, b, A, a + b):
                    return True
    if S in ops:
        for ia, a in enumerate(true_nums):
            for ib, b in enumerate(true_nums):
                if ia == ib:
                    continue
                if handoff(true_nums, true_ops, goal, a, b, S, a - b):
                    return True

    return False


def handoff(true_nums, true_ops, goal, a, b, op, reduction):
    n = true_nums.copy()
    o = true_ops.copy()
    n.remove(a)
    n.remove(b)
    n.append(reduction)
    o.remove(op)
    return solve(','.join(str(x) for x in n), ''.join(o), goal)


with open('Prob16.in.txt') as f:
    f.readline()  # idc how many tests there are
    tests = []
    while True:
        l = f.readline()
        if not l:
            break
        goal_, tools = l.split(':')
        goal_ = int(goal_)
        tools = tools.split()
        nums_ = []
        ops_ = []
        for tool in tools:
            if tool.isnumeric():
                nums_.append(tool)
            else:
                ops_.append(tool)
        tests.append((','.join(nums_), ''.join(ops_), goal_))

for t in tests:
    print('TRUE' if solve(*t)else 'FALSE')
