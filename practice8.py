try:
    xz = open("text.txt", "r")
    print(xz)
    hi = xz.read()
    print(hi)
    xz.close()
except ValueError:
    print("you got it wrong")

xz = open("text.txt", "r")
print(xz)
for line in xz:
    print(line.rstrip())
xz.close()

with open("text.txt", "a") as xz:
    print(xz)
    line = input("Give me some text, don't be shy: ")
    xz.write(line)
    xz.write("\n")
