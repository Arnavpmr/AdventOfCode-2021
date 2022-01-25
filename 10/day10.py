from collections import deque

file = open("input.txt", "r")

q = deque()

opening = ['(', '[', '{', '<']
closing = [')', ']', '}', '>']

char_dict = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

completion_dict = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

scores = []

lines = []

total = 0


for line in file:
    lines.append(line.rstrip('\n'))

for line in lines:
    is_incomplete = True

    q.clear()
    
    for char in line:
        if char in opening:
            q.append(char)
        elif char in closing:
            recent_char = q.pop()

            if closing.index(char) != opening.index(recent_char):
                total += char_dict[char]
                is_incomplete = False
                break
    
    if is_incomplete:
        score = 0
        
        while len(q) > 0:
            recent_char = q.pop()
            score *= 5
            score += completion_dict[recent_char]
        
        scores.append(score)

scores.sort()

print(scores[len(scores)//2])