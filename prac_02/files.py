# 1. Write code that asks the user for their name,
# then opens a file called "name.txt" and writes that name to it.
name = input("please enter your name: ")
with open("name.txt", "w") as fp:
    fp.write(name)

# 2. Write code that opens "name.txt" and reads the name (as above) then prints,
# "Your name is Bob" (or whatever the name is in the file).
with open("name.txt", "r") as fp:
    read_name = fp.readline()
print("Your name is {}", format(read_name, ))

# 3. Create a text file called numbers.txt and save it in your prac_02 directory.
# Put the following three numbers on separate lines in the file and save it:
with open("numbers.txt", "w") as fp:
    for n in 17, 42, 400:
        fp.write("{}\n".format(n, ))

# Write code that opens "numbers.txt", reads only the first two numbers and adds
# them together then prints the result, which should be... 59.
with open("numbers.txt", "r") as fp:
    s = 0
    for n in fp:
        s += int(n)
    print(s)

# Now write a fourth block of code that prints the total for all
# lines in numbers.txt or a file with any number of numbers.

with open("numbers.txt", "r") as fp:
    line_num = 0
    for n in fp:
        line_num += 1
    print("the total for all lines is {}".format(line_num, ))
