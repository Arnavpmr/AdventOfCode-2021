from math import inf

file = open("input.txt", "r")

G = []

for line in file:
    G.append([int(x) for x in line.strip()])

DP = {}

# def solve(r, c):
#     if (r, c) in DP:
#         return DP[(r, c)]
#     if r < 0 or r >= len(G) or c < 0 or c >= len(G[r]):
#         return 1e9
#     if r == len(G) - 1 and c == len(G[r]) - 1:
#         return G[r][c]
    
#     ans = G[r][c] + min(solve(r+1, c), solve(r, c+1))
#     DP[(r, c)] = ans
    
#     return ans

def solve(r, c):
    pass

print(solve(0, 0))