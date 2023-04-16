import statistics

file = open("input.txt", "r")

crabPositions = []

for line in file:
    crabPositions += map(int, line.rstrip("\n").split(","))

med = statistics.median(crabPositions)

def BC(n):
    return n*(n+1)/2

q = float("inf")

for i in range(min(crabPositions), max(crabPositions) + 1):
    t = sum(BC(abs(x - i)) for x in crabPositions)
    q = min(q, t)

print(q)