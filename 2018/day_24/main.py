#!/usr/bin/env python3

import re

class Group:
    def __init__(self, n_units, hitpoints, damage, dtype, initiative,
            weak = None, immune = None):
        self.n_units = n_units
        self.hitpoints = hitpoints
        self.damage = damage
        self.dtype = dtype
        self.initiative = initiative
        self.weak = weak
        self.immune = immune
        self.next_target = None

    @property
    def n_units(self):
        return self._n_units

    @n_units.setter
    def n_units(self, v):
        self._n_units = max(0, v)

    @property
    def effective_power(self):
        return self.n_units * self.damage

    def attack(self):
        if self.next_target:
            self.next_target.take_damage(self.damage*self.n_units, self.dtype)
        self.next_target = None

    def take_damage(self, damage, dtype, test = False):
        if dtype in self.immune:
            damage = 0
        if dtype in self.weak:
            damage *= 2
        if test:
            return damage
        killed = min(self.n_units, (damage//self.hitpoints))
        self.n_units -= killed

if __name__ == '__main__':
    def load(boost = 0):
        immune, infection = [], []
        with open('input', 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if line.startswith('Immune'):
                    system = immune
                    continue
                if line.startswith('Infection'):
                    system = infection
                    boost = 0
                    continue
                n, hp, damage, initiative = [int(i) for i in re.findall(r'\d+', line)]
                ws = line.split(' ')
                dtype = ws[ws.index('damage') - 1]
                sp = re.findall(r'\((.+)\)', line)
                kwargs = {'weak':[], 'immune':[]}
                if sp:
                    for s in sp[0].split('; '):
                        ss = s.split(' ')
                        kwargs[ss[0]].extend([i.strip(',') for i in ss[2:]])
                system.append(Group(n, hp, damage + boost, dtype, initiative, **kwargs))
        return immune, infection
    immune, infection = load()

    # target selection
    def target_selection(immune, infection):
        key = lambda x : (x.effective_power, x.initiative)
        immune.sort(key = key, reverse = True)
        infection.sort(key = key, reverse = True)
        t_immune = immune[:]
        t_infection = infection[:]
        key = lambda x : (x.take_damage(i.effective_power, i.dtype, test = True),
                x.effective_power, x.initiative)
        for i in immune:
            t_infection.sort(key = key)
            try:
                if t_infection[-1].take_damage(i.effective_power, i.dtype, test = True):
                    i.next_target = t_infection.pop()
            except IndexError:
                pass
        for i in infection:
            t_immune.sort(key = key)
            try:
                if t_immune[-1].take_damage(i.effective_power, i.dtype, test = True):
                    i.next_target = t_immune.pop()
            except IndexError:
                pass

    def attack_phase(immune, infection):
        key = lambda x : (x.initiative)
        units = sorted(immune + infection, key = key, reverse = True)
        for u in units:
            u.attack()
        for i in immune[:]:
            if not i.n_units:
                immune.remove(i)
        for i in infection[:]:
            if not i.n_units:
                infection.remove(i)

    # part 1
    while True:
        target_selection(immune, infection)
        attack_phase(immune, infection)
        if not immune:
            print(sum(i.n_units for i in infection))
            break
        if not infection:
            print(sum(i.n_units for i in immune))
            break

    # part 2:
    boost = 0
    immune_win = False
    while not immune_win:
        boost += 1
        immune, infection = load(boost)
        while True:
            units = sum(i.n_units for i in immune + infection)
            target_selection(immune, infection)
            attack_phase(immune, infection)
            units_f = sum(i.n_units for i in immune + infection)
            if units == units_f:
                break
            if not immune:
                break
            if not infection:
                print(sum(i.n_units for i in immune))
                immune_win = True
                break
