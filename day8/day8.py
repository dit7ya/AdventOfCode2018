# Part 1
fl = open('input.txt', 'r')

inp = fl.read()
inp = [int(x) for x in inp.split()]



def f(start_idx):

    meta_sum = 0

    n_child, n_meta = inp[start_idx], inp[start_idx+1]

    next_start = start_idx +2
    for child_node in range(n_child):
        child_sum, next_start = f(next_start)
        meta_sum += child_sum

    meta_sum += sum(inp[next_start: next_start+n_meta])
    next_start+= n_meta
    return meta_sum, next_start



print(f(0))
