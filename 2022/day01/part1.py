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

result = max(totals)
print(result)

assert result == 71300
