#!/usr/bin/env python3

if __name__ == '__main__':
    scores = [3, 7]
    e1 = 0
    e2 = 1
    puzzle = '074501'
    def make_recipes(scores, e1, e2):
        c = scores[e1] + scores[e2]
        if c < 10:
            scores.append(c)
        else:
            scores.append(c//10)
            scores.append(c%10)
        l = len(scores)
        return (e1 + 1 + scores[e1])%l, (e2 + 1 + scores[e2])%l
    # part 1
    while True:
        e1, e2 = make_recipes(scores, e1, e2)
        if len(scores) >= int(puzzle) + 10:
            print(''.join(str(i) for i in scores[int(puzzle):]))
            break
    # part 2
    puzzle = tuple(int(i) for i in puzzle)
    while True:
        e1, e2 = make_recipes(scores, e1, e2)
        # cases for if 1 or 2 new recipes are added
        if tuple(scores[-len(puzzle):]) == puzzle:
            print(len(scores) - len(puzzle))
            break
        if tuple(scores[-len(puzzle) - 1:-1]) == puzzle:
            print(len(scores) - len(puzzle) - 1)
            break

