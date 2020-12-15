string = input("enter a string: ")

count = {}
maxlen = 0

for s in string.split():
    count[s] = count.get(s, 0) + 1
    maxlen = max(maxlen, len(s))

for k, v in count.items():
    print("{:{}} : {}".format(k, maxlen, v))
