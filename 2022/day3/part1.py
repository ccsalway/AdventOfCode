total = 0

with open('input.txt') as f:
    for line in f.read().splitlines():
        n = len(line)
        h = n // 2  # assuming all lines are perfectly divisible by 2
        f = set(line[0:h])
        s = set(line[h:n])
        i = [ord(x) for x in f & s][0]
        if i >= 97:  # a-z
            total += i - 97 + 1
        elif i >= 65:  # A-Z
            total += i - 65 + 27

print(total)

assert total == 7821
