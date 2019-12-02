#!/usr/bin/env python3

def fuel(mass, recursive = False):
    f = lambda m : max(m//3 - 2, 0)
    f_req = [f(mass)]
    if recursive:
        while f_req[-1]:
            f_req.append(f(f_req[-1]))
    return sum(f_req)

if __name__ == '__main__':
    with open('input', 'r') as f:
        modules = [int(l) for l in f]

    # part 1
    print(sum(fuel(m) for m in modules))

    # part 2
    print(sum(fuel(m, recursive = True) for m in modules))

