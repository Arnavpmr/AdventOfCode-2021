file = open("input.txt", "r")

fishData = []

for line in file:
    fishData += map(int, line.rstrip("\n").split(","))

days = 256

for j in range(days):
    newFish = []
    for i, num in enumerate(fishData):
        if num == 0:
            fishData[i] = 6
            newFish.append(8)
        else:
            fishData[i] -= 1

    fishData += newFish

print(len(fishData))