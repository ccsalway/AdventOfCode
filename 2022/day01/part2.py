totals = []

with open('input.txt') as f:
    subtotal = 0
    for line in f.read().splitlines():
        # dont rely on newline being \n
        try:
            subtotal += int(line)
        except ValueError:
            # will cause an exception on each blank line
            totals.append(subtotal)
            subtotal = 0

totals.sort(reverse=True)

result = sum(totals[0:3])
print(result)

assert result == 209691
