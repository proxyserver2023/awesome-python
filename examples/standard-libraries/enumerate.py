seasons = ['Spring',
           'Summer',
           'Fall',
           'Winter']
print(list(enumerate(seasons)))
print(list(enumerate(seasons, start=1)))


def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
