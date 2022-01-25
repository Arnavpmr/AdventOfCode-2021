file = open("input.txt", "r")

octopuses = []

ans = 0

def flash(y, x):

    global ans
    ans += 1

    maxx, maxy = len(octopuses[y]) - 1, len(octopuses) - 1

    octopuses[y][x] = -1

    for dr in [-1, 0, 1]:
        for dc in[-1, 0, 1]:
            rr = y+dr
            cc = x+dc

            if 0 <= rr <= maxy and 0 <= cc <= maxx and octopuses[rr][cc] != -1:
                octopuses[rr][cc] += 1
                if octopuses[rr][cc] >= 10:
                    flash(rr, cc)


for line in file:
    octopuses.append([int(i) for i in line.rstrip('\n')])

done = True

i = 0

while True:

    i += 1

    for y in range(len(octopuses)):
        for x in range(len(octopuses[y])):
            octopuses[y][x] += 1

    for y in range(len(octopuses)):
        for x in range(len(octopuses[y])):
            if octopuses[y][x] >= 10:
                flash(y, x)

    done = True
    for y in range(len(octopuses)):
        for x in range(len(octopuses[y])):
            if octopuses[y][x] == -1:
                octopuses[y][x] = 0
            else:
                done = False

    if i == 100:
        print(ans)
    if done:
        print(i)
        break