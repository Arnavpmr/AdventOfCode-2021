import sys

sys.setrecursionlimit(int(1e6))

file = open("input.txt", "r")

ans = 0
count = 0

for DX in range(1000):
    for DY in range(-1000, 1000):

        dx = DX
        dy = DY

        ok = False

        x = 0
        y = 0

        max_y = 0

        for t in range(1000):
            x += dx
            y += dy

            max_y = max(max_y, y)
            
            if dx > 0:
                dx -= 1
            elif dx < 0:
                dx += 1
            
            dy -= 1

            if 117 <= x <= 164 and -140 <= y <= -89:
                ok = True
                count += 1
        
        if ok:
            print(dx, dy, count)
            ans = max(max_y, ans)

print(count)    