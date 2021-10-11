a,b,c = map(int,input().split())

if a > b:
	buf = a
	a = b
	b = buf

if b > c:
	buf = b
	b = c
	c = buf

if a > b:
    buf = a
    a = b
    b = buf

print(a,b,c)
