# -*- coding: utf-8 -*-
import collections


# Tally occurances of words in a list
cnt = collections.Counter()
for word in ['red',
             'green',
             'blue',
             'red',
             'green',
             'blue',
             'red',
             'green',
             'blue',
             ]:
    cnt[word] += 1

import pprint
pprint.pprint(cnt)

"""
Counter({'red': 3, 'green': 3, 'blue': 3})
"""


# Find the most common words in hamlet
import time
start = time.time()

import re

words = re.findall(r'\w+', open('hamlet.txt').read().lower())
collections.Counter(words).most_common(10)
result = collections.Counter(words).most_common(10)

end = time.time()

import pprint
pprint.pprint(result)

print(f"for one iteration {end-start}")

# profiling using timeit
logic_statement = """
words=re.findall(r'\w+', open('hamlet.txt').read().lower())
collections.Counter(words).most_common(10)"""
import_statement = """import collections, re"""

from timeit import Timer
t = Timer(logic_statement, import_statement)
print((t.repeat(3, 10)))

"""
OUTPUT: AFTER RUNNING for 3 iterations each 10 TIMES
[0.1311193010005809, 0.13003668999954243, 0.13032713599932322]
"""