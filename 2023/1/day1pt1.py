vals = []

with open('input.txt', 'r') as f:
    for line in f:
        digits = [int(i) for i in line if i.isdigit()]
        vals.append(str(digits[0]) + str(digits[-1]))

vals = list(map(int, vals))
print(sum(vals))
