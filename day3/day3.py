import numpy as np
# part 1

sheet = np.zeros((1000, 1000))

inp = open("input.txt", 'r')

def func(sheet, inp):
    for line in inp:
        s = line.split()[2:]
        x, y = int(s[0][:-1].split(',')[0]),  int(s[0][:-1].split(',')[1])
        xd, yd = int(s[1].split('x')[0]), int(s[1].split('x')[1])
        sheet[x:x+xd,y:y+yd] += 1

    return sheet



filled_sheet = func(sheet, inp)
overlap = filled_sheet > 1
print(np.sum(overlap))

inp.close()

# part 2
inp = open("input.txt", 'r')


def func2(sheet, inp):

    ans = None
    for line in inp:
        s = line.split()[2:]
        x, y = int(s[0][:-1].split(',')[0]),  int(s[0][:-1].split(',')[1])
        xd, yd = int(s[1].split('x')[0]), int(s[1].split('x')[1])

        if np.sum(sheet[x:x+xd,y:y+yd]>1) == 0:
            ans = line.split()[0]
        else:
            pass
    return ans

print(func2(filled_sheet, inp))

inp.close()
