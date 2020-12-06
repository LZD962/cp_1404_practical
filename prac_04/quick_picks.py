import random

MAX = 45
MIN = 1
NUMS = 6
num = int(input("How many quick picks? "))

for i in range(num):
    nums = []
    for j in range(NUMS):
        while len(nums) < 6:
            x = random.randint(MIN, MAX)
            if x not in nums:
                nums.append(x)
    print("{:2} {:2} {:2} {:2} {:2} {:2}".format(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5]))
