import re
pattern = 'this'
text = 'Does this text match this pattern?'
match = re.search(pattern, text)
s = match.start()
e = match.end()

print('Found "%s"\nin "%s"\n from %d to %d ("%s")' % \
      (match.re.pattern, match.string, s, e, text[s:e])
)

regexes = [re.compile(p) for p in ['this', 'that']]


for regex in regexes:
    print('Seeking "%s" -> ' % regex.pattern)

    if regex.search(text):
        print("Match")
    else:
        print("No Match")


# Mulitiple Matches

import re
pattern = 'ab'
text = 'abbabbbbbaaaabbbbbbbbaaaaaaa'
for match in re.findall(pattern, text):
    print("Found '%s'" % match)


for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print("Found '%s' at %d:%d" % (text[s:e], s, e))
