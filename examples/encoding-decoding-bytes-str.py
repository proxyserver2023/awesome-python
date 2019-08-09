# encoding.py
a = 'Md. Alamin Mahamud'
print(type(a))

b = b'Md. Alamin Mahamud'
print(type(b))

c = a.encode('ASCII')
print(c)
print(type(c))

d = a.encode('UTF-8')
print(d)
print(type(d))

e = a.encode()
print(e)
print(type(e))

if b == c:
    print('Encoded')
if b == d:
    print('Encoded')
if b == e:
    print('Encoded')


g = 'Hello, চিন্তা করতেছি এখন থেকে গুগল ট্রান্সলেট বাদে আপনাকে ইউজ করব'
print(type(g))
h = g.encode()
print(h)
print(type(h))

i = g.encode('UTF-8')
print(i)
print(type(i))