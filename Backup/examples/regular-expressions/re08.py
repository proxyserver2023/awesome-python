# Search for lines that start with 'X' followed by any
# no whitespace characters and ':' followed by a space
# and any number. The number can include a decimal.
# Then print the number if it is greater than zero.

import re
handle = open('mbox-short.txt')
for line in handle:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)', line)
    if (len(x)) > 0:
        print(x)
        
