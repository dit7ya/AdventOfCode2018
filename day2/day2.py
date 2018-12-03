# Part 1 Solution. This is ugly because I misunderstood the question in the beginning.

f = open("input.txt", "r")


def appears(string, letters, times):
    d = []
    for i in letters:
        n = string.count(i)
        if n == times:
            d.append(i)
        else:
            pass

    return d


letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

c = [0, 0]

for line in f:
    d2 = appears(str(line), letters, times=2)
    if len(d2) > 0:
        c[0] += 1
    d3 = appears(str(line), letters, times=3)
    if len(d3) > 0:
        c[1] += 1

print(c[0] * c[1])

f.close()
# Part Two

# This is again very ugly and inefficient. I will refactor it later.


def differs(string1, string2):
    l = len(string2)
    ans = None
    for i in range(l):
        if string1[:i] + string1[i + 1:] == string2[:i] + string2[i + 1:]:
            ans = string1[:i] + string1[i + 1:]

    return ans

f2 = open("input.txt", "r")
lst = []

for line in f2:
    lst.append(str(line)[:-1])


for i in range(len(lst)):
    for j in lst[i+1:]:
        if differs(str(lst[i]), j) is not None:
            print(differs(lst[i], j))
