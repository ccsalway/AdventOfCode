with open('input.txt') as f:
    input = f.read()

for i in range(len(input)):
    if len(set(input[i:i + 14])) == 14:
        break

result = i + 14
print(result)

assert result == 2250
