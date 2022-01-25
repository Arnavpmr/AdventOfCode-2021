nums = []

file = open("input.txt", "r")

for line in file:
    nums.append(line.rstrip("\n"))

count = 0

nums = [int(number) for number in nums]


#solve 1
for i in range(len(nums) - 2):
    if nums[i] < nums[i+1]:
        count += 1
    
#solve 2
for i in range(len(nums) - 3):
    if nums[i] + nums[i+1] + nums[i+2] < nums[i+1] + nums[i+2] + nums[i+3]:
        count += 1


file.close()
print(count)