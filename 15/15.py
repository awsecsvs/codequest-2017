with open('Prob15.in.txt') as f:
    f.readline()  # I don't care how many tests there are
    items = []
    while True:
        l = f.readline()
        if not l:
            break
        items.append(l)


def handle(test):
    def fmt(result):
        return '{} = {}'.format(test.strip(), result)

    nums = [int(n) for n in test.strip() if n != '0']
    freq = dict()
    for num in nums:
        freq[num] = 1 + freq.get(num, 0)

    # let's see what frequencies we have
    five = four = three = two = extra_two = extra_three = False
    for val in freq.values():
        if val >= 5:  # we can "select down"
            five = True
        if val == 4:
            four = True
        if val == 3:
            if three:
                extra_three = True
            three = True
        if val == 2:
            if two:
                extra_two = True
            two = True

    if five:
        return fmt('FIVE OF A KIND')
    if four:
        return fmt('FOUR OF A KIND')
    if three and (two or extra_three):
        return fmt('FULL HOUSE')
    if check_straight(nums):
        return fmt('STRAIGHT')
    if three:
        return fmt('THREE OF A KIND')
    if two and extra_two:
        return fmt('TWO PAIR')
    if two:
        return fmt('PAIR')
    return fmt(max(nums))


def check_straight(nums):
    for i in range(1, 6):
        success = True
        for j in range(i, i + 5):
            if j not in nums:
                success = False

        if success:
            return True
    return False


for t in items:
    # if t in ('72777727\n', '72881228\n', '29402299\n'):
    #     print()
    print(handle(t))
