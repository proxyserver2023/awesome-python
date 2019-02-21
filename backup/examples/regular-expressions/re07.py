import re
file_handle = open('mbox-short.txt')
for line in file_handle:
    line = line.rstrip()
    x = re.findall(
        '[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line
    )
    if len(x) > 0:
        print(x)
