file = open("input.txt", "r")

points = []
instructions = []

for line in file:
    line = line.rstrip("\n")

    if line.startswith("fold"):
        instructions.append(line)
    else:
        if not line == "":
            x, y = map(int, line.split(","))
            points.append((x, y))

for instruction in instructions:
    p2 = []
    axis, coord = instruction.split()[2].split("=")[0], int(instruction.split()[2].split("=")[1])

    if axis == 'x':
        for point in points:
            if point[0] > coord:
                dist = point[0] - coord

                if (point[0] - (2*dist), point[1]) not in p2:
                    p2.append((point[0] - (2*dist), point[1]))
            else:
                p2.append(point)

    elif axis == 'y':
        for point in points:
            if point[1] > coord:
                dist = point[1] - coord
                if (point[0], point[1] - (2*dist)) not in p2:
                    p2.append((point[0], point[1] - (2*dist)))
            else:
                p2.append(point)

    points = p2

X = max([x for x, y in points])
Y = max([y for x, y in points])

output = ""

for i in range(Y+1):
    for j in range(X+1):
        output += ('x' if (j, i) in points else ' ')
    print(output)
    output = ""