nums = []
for i in range(5):
    num = int(input("Number: "))
    nums.append(num)

print("The first number is {}".format(nums[0]))
print("The last number is {}".format(nums[-1]))
print("The smallest number is {}".format(min(nums)))
print("The largest number is {}".format(max(nums)))
print("The average number is {}".format(sum(nums) / len(nums)))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

name = input("Your username: ")
if name in usernames:
    print("Access granted")
else:
    print("Access denied")
