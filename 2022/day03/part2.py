total = 0

with open('input.txt') as f:
    lines = []
    for index, line in enumerate(f.read().splitlines()):
        lines.append(set(line))
        if (index + 2) % 3 == 1:
            a, b, c = lines
            i = [ord(x) for x in a & b & c][0]
            if i >= 97:  # a-z
                total += i - 97 + 1
            elif i >= 65:  # A-Z
                total += i - 65 + 27
            lines = []

print(total)

assert total == 2752
