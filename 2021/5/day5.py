inputData = []

file = open("input.txt", "r")

lines = []

grid = []

for i in range(1000):
    row = []
    for j in range(1000):
        row.append(0)
    grid.append(row)

for line in file:
    inputData.append(line.rstrip("\n"))

for data in inputData:
    points_raw = data.split(' -> ')

    point_1 = points_raw[0].split(',')
    point_2 = points_raw[1].split(',')

    lines.append([[int(point_1[0]), int(point_1[1])], [int(point_2[0]), int(point_2[1])]])

# [[217, 490], [217, 764]]

for line in lines:
    x1, y1, x2, y2 = line[0][0], line[0][1], line[1][0], line[1][1]

    if x1 == x2:
        if y2 > y1:
            for i in range(y1, y2+1):
                grid[i][x1] += 1
        elif y1 > y2:
            for i in range(y2, y1+1):
                grid[i][x1] += 1
    elif y1 == y2:
        if x2 > x1:
            for i in range(x1, x2+1):
                grid[y1][i] += 1
        elif x1 > x2:
            for i in range(x2, x1+1):
                grid[y1][i] += 1
    else:
        grid[x1][y1] += 1

        while x1 != x2 and y1 != y2:
            if x1 > x2:
                x1 -= 1
            elif x2 > x1:
                x1 += 1
            
            if y1 > y2:
                y1 -= 1
            elif y2 > y1:
                y1 += 1

            grid[x1][y1] += 1            

count = 0

for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] >= 2:
            count += 1

print(count)