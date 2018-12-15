#!/usr/bin/env python3

class Cavern:
    def __init__(self, mapstring):
        self.mapstring = mapstring
        self.initialize(mapstring)
        
    def initialize(self, mapstring, elf_attack = 3):
        self.walls = set()
        self.units = {}
        self.elf_initial = 0
        for y, line in enumerate(mapstring.split('\n')):
            for x, c in enumerate(line):
                if c == '#':
                    self.walls.add((y, x))
                if c == 'E':
                    self.units[(y, x)] = Unit(y, x, c, self, elf_attack)
                    self.elf_initial += 1
                if c == 'G':
                    self.units[(y, x)] = Unit(y, x, c, self)
        self.height, self.width = y + 1, x + 1
        self.round = 0

    def neighbours(self, position):
        y, x = position
        direct = set([(y - 1, x), (y, x - 1), (y, x + 1), (y + 1, x)])
        return sorted(direct - self.walls)

    def remaining(self, race):
        return [u for u in self.units.values() if u.race == race]

    def path(self, start, targets):
        visited = {n:(n,) for n in self.neighbours(start) if n not in self.units}
        depth = 1
        def current_depth():
            return [k for k, v in visited.items() if len(v) == depth]
        while True:
            reached = set(visited.keys()) & targets
            if reached:
                return sorted([visited[k] for k in reached])[0]
            for position in current_depth():
                for n_position in self.neighbours(position):
                    if n_position not in self.units and n_position not in visited:
                        visited[n_position] = visited[position] + (n_position,)
            depth += 1
            if not current_depth():
                return None

    def run(self):
        while True:
            for unit in sorted(self.units.values(), key = lambda x: x.position):
                unit.do_action()
            if not self.remaining('E') or not self.remaining('G'):
                return
            self.round += 1

    def run_elf_deathless(self):
        while True:
            for unit in sorted(self.units.values(), key = lambda x: x.position):
                unit.do_action()
            if len(self.remaining('E')) < self.elf_initial:
                return False
            if not self.remaining('G'):
                return True
            self.round += 1

    def outcome(self):
        remaining_hp = sum(u.hp for u in self.units.values())
        return remaining_hp, self.round, remaining_hp*self.round

class Unit:
    def __init__(self, y, x, race, cavern, attack = 3):
        self.y = y
        self.x = x
        self.race = race
        self.enemy_race = {'E':'G', 'G':'E'}[race]
        self.cavern = cavern
        self.attack = attack
        self.hp = 200

    @property
    def position(self):
        return (self.y, self.x)

    def move(self, new_position):
        del self.cavern.units[self.position]
        self.y, self.x = new_position
        self.cavern.units[new_position] = self

    @property
    def neighbours(self):
        return self.cavern.neighbours(self.position)

    def neighbouring_enemies(self):
        enemies = []
        for n in self.neighbours:
            try:
                if self.cavern.units[n].race == self.enemy_race:
                    enemies.append(self.cavern.units[n])
            except KeyError:
                pass
        return sorted(enemies, key = lambda x: x.hp)

    def do_action(self):
        if self.hp <= 0:
            return

        if self.neighbouring_enemies():
            self.fight(self.neighbouring_enemies()[0])
            return

        enemy_adjacent = set()
        for enemy in self.cavern.remaining(self.enemy_race):
            enemy_adjacent.update([p
                for p in enemy.neighbours if p not in self.cavern.units])
        if not enemy_adjacent:
            return
        path = self.cavern.path(self.position, enemy_adjacent)
        if path is None:
            return
        self.move(path[0])

        if self.neighbouring_enemies():
            self.fight(self.neighbouring_enemies()[0])
            return

    def fight(self, enemy):
        enemy.hp -= self.attack
        if enemy.hp <= 0:
            del self.cavern.units[enemy.position]

if __name__ == '__main__':
    with open('input', 'r') as f:
        cavern = Cavern(f.read())
    cavern.run()

    # part 1
    print(cavern.outcome()[2])
    
    # part 2
    elf_attack = 3
    while True:
        elf_attack += 1
        cavern.initialize(cavern.mapstring, elf_attack)
        if cavern.run_elf_deathless():
            print(cavern.outcome()[2])
            break

