#!/usr/bin/env python3

import sys
import logging

class Cavern:
    def __init__(self, fd, elf_attack = 3):
        self.units = []
        self.floor = {}
        for i, line in enumerate(fd):
            for j, c in enumerate(line.rstrip('\n')):
                self.floor[(i, j)] = 0 if c == '#' else 1
                if c == 'E':
                    self.units.append(Unit(i, j, c, self, attack = elf_attack))
                if c == 'G':
                    self.units.append(Unit(i, j, c, self, attack = 3))
        self.height, self.width = i + 1, j + 1
        self.round = 0

    def remaining(self, c):
        return [u for u in self.units if u.c == c and u.hp > 0]

    def is_occupied(self, position):
        occupied = [u for u in self.units if position == u.position]
        if occupied:
            return occupied[0]
        return None

    def step(self):
        end_early = False
        for unit in sorted(self.units, key = lambda x : x.position):
            e = unit.do_action()
            if e:
                end_early = True
        for unit in self.units:
            if unit.hp <= 0:
                self.units.remove(unit)
        if end_early:
            return
        self.round += 1

class Unit:
    def __init__(self, i, j, c, cavern, attack = 3):
        self.i = i
        self.j = j
        self.c = c
        self.cavern = cavern
        self.hp = 200
        self.attack = attack

    @property
    def position(self):
        return (self.i, self.j)

    @property
    def neighbours(self):
        return sorted(((self.i-1, self.j), (self.i, self.j+1),
                (self.i+1, self.j), (self.i, self.j-1)))

    def targets(self):
        e = {'E':'G', 'G':'E'}[self.c]
        enemies = self.cavern.remaining(e)
        t = []
        for unit in enemies:
            if unit.position in self.neighbours:
                t.append(unit)
        return sorted(t, key = lambda x : x.position)

    def do_action(self):
        if self.hp <= 0:
            return
        e = {'E':'G', 'G':'E'}[self.c]
        enemies = self.cavern.remaining(e)
        if not enemies:
            return True

        for t in sorted(self.targets(), key = lambda x : x.hp):
            t.hp -= self.attack
            if t.hp <= 0:
                self.cavern.units.remove(t)
            return

        adjacent = set()
        for enemy in enemies:
            for n in enemy.neighbours:
                if self.cavern.floor[n] and not self.cavern.is_occupied(n):
                    adjacent.add(n)

        if not adjacent:
            return

        def neighbours(i, j):
            return sorted([(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)])

        def search():
            visited = {n:(n,) for n in sorted(self.neighbours) if self.cavern.floor[n]
                    and not self.cavern.is_occupied(n)}
            depth = 1
            while True:
                l = set(visited.keys()) & adjacent
                if l:
                    return sorted([visited[k] for k in l])[0]
                for s in [k for k, v in visited.items() if len(v) == depth]:
                    for sn in sorted(neighbours(*s)):
                        if self.cavern.floor[sn] and not self.cavern.is_occupied(sn):
                            if sn not in visited:
                                visited[sn] = visited[s] + (sn,)
                depth += 1
                if not [k for k, v in visited.items() if len(v) == depth]:
                    return None

        path = search()
        if path is None:
            return
        self.i, self.j = path[0]

        for t in sorted(self.targets(), key = lambda x : x.hp):
            t.hp -= self.attack
            if t.hp <= 0:
                self.cavern.units.remove(t)
            return

if __name__ == '__main__':
    with open('input', 'r') as f:
        cavern = Cavern(f)
    while True:
        cavern.step()
        if not cavern.remaining('G') or not cavern.remaining('E'):
            remaining_hp = sum(u.hp for u in cavern.units)
            print(remaining_hp*cavern.round)
            break

    # part 2
    elf_attack = 3
    end = False
    while not end:
        elf_attack += 1
        with open('input', 'r') as f:
            cavern = Cavern(f, elf_attack)
        starting_elves = len(cavern.remaining('E'))
        while True:
            cavern.step()
            if not len(cavern.remaining('G')):
                remaining_hp = sum(u.hp for u in cavern.units)
                print(remaining_hp*cavern.round)
                end = True
                break
            if len(cavern.remaining('E')) < starting_elves:
                break

