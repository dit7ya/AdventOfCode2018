# Part 1


def reduce(string):
    l = []
    idx = 0
    while True:
        if string[idx] != string[idx + 1].swapcase():
            l.append(string[idx])
            idx += 1
        else:
            idx += 2
        if idx >= len(string) - 1:
            l.append(string[idx])
            break
        else:
            continue
    s = "".join(l)
    return s


f = open("input.txt", "r")
inp = f.read()


def get_out(inp):
    out = None
    while True:
        out = reduce(inp)
        if out == inp:
            break
        else:
            inp = out
    return out


out = get_out(inp)
new = list(out)
new.remove("\n")

print(len(new))


# Part 2


# NOTE: It does not really matter in which order you react the thing
# So we will just use the previous answer as the new input
letters = list("abcdefghijklmnopqrstuvwxyz")

mini = len(new)

for l in letters:

    removed_list = [item for item in new if (item != l and item != l.upper())]
    new_string = "".join(removed_list)
    reacted = get_out(new_string)

    mini = min(len(reacted), mini)

print(mini)
