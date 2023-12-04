commands = []

file = open("input.txt", "r")

for line in file:
    commands.append(line.rstrip("\n"))

horizontal_pos = 0
depth = 0
aim = 0

# for command in commands:
#     command, distance = command.split()
#     if command == "forward":
#         horizontal_pos += int(distance)
#     elif command == "up":
#         depth -= int(distance)
#     elif command == "down":
#         depth += int(distance)

for command in commands:
    command, distance = command.split()
    if command == "forward":
        horizontal_pos += int(distance)
        depth += aim*int(distance)
    elif command == "up":
        aim -= int(distance)
    elif command == "down":
        aim += int(distance)


print(depth, horizontal_pos)