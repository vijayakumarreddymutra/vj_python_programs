
a = "malayalam"

b = ""
for i in range(len(a)-1,-1,-1):
    b +=a[i]

print(b)
print(b == a)


c = a[::-1]

print(c == a)