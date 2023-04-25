from collections import deque

file = open("input.txt")

def is_min(posy, posx, height_map):

    level = height_map[posy][posx]

    minx, maxx = 0, len(height_map[posy]) - 1
    miny, maxy = 0, len(height_map) - 1

    if miny < posy and height_map[posy - 1][posx] <= level:
        return False

    if posy < maxy and height_map[posy + 1][posx] <= level:
        return False

    if minx < posx and height_map[posy][posx - 1] <= level:
        return False
    
    if posx < maxx and height_map[posy][posx + 1] <= level:
        return False

    return True
        

height_map = []

basin_sizes = []

total = 0

for line in file:
    height_map.append([int(i) for i in line.rstrip("\n")])

for i in range(len(height_map)):
    for j in range(len(height_map[i])):
        if is_min(i, j, height_map):
            minx, maxx = 0, len(height_map[i]) - 1
            miny, maxy = 0, len(height_map) - 1

            total = 1
            
            q = deque()
            q.append((i, j))

            while len(q) > 0:
                y, x = q.pop()

                for yn, xn in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

                    newx = x + xn
                    newy = y + yn

                    if miny <= newy <= maxy and minx <= newx <= maxx:
                        if height_map[newy][newx] != 9 and height_map[newy][newx] != -1 and height_map[newy][newx] > height_map[i][j] and (newy, newx) not in q:
                            height_map[newy][newx] = -1
                            q.append((newy, newx))
                            
                            total += 1
            
            basin_sizes.append(total)

basin_sizes.sort()

print(basin_sizes[-3] * basin_sizes[-2] * basin_sizes[-1])