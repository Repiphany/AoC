#!/usr/bin/env python3

from .input import get_input
from IPython.terminal.embed import InteractiveShellEmbed
import re

class Passport:
    REQUIRED = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    OPTIONAL = ['cid']
    def __init__(self):
        pass

    def parse_input(self, s):
        s = s.strip()
        if not s:
            return
        for pair in s.split(' '):
            try:
                k, v = pair.split(':')
                self.__setattr__(k, v)
            except:
                pass

    @property
    def is_valid(self):
        return all(f in self.__dict__ for f in Passport.REQUIRED)

    @property
    def is_valid2(self):
        validators = [
                self.byr_valid,
                self.iyr_valid,
                self.eyr_valid,
                self.hgt_valid,
                self.hcl_valid,
                self.ecl_valid,
                self.pid_valid,
                self.cid_valid,
                ]
        return all(validators)

    @property
    def byr_valid(self):
        try:
            return 1920 <= int(self.byr) <= 2002
        except:
            return False

    @property
    def iyr_valid(self):
        try:
            return 2010 <= int(self.iyr) <= 2020
        except:
            return False

    @property
    def eyr_valid(self):
        try:
            return 2020 <= int(self.eyr) <= 2030
        except:
            return False

    @property
    def hgt_valid(self):
        try:
            if 'cm' in self.hgt:
                low, high = 150, 193
            elif 'in' in self.hgt:
                low, high = 59, 76
            else:
                return False
            return low <= int(self.hgt[:-2]) <= high
        except:
            return False

    @property
    def hcl_valid(self):
        try:
            return bool(re.match('#[0-9a-f]{6}$', self.hcl))
        except:
            return False

    @property
    def ecl_valid(self):
        try:
            return self.ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        except:
            return False

    @property
    def pid_valid(self):
        try:
            return bool(re.match('[0-9]{9}$', self.pid))
        except:
            return False

    @property
    def cid_valid(self):
        try:
            return True
        except:
            return False

def get_passports(lines):
    passports = [Passport()]
    for line in lines:
        if not line.strip():
            passports.append(Passport())
            continue
        passports[-1].parse_input(line)
    return passports

def test(args):
    passports = get_passports("""pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021
pid:093154719""".split('\n'))
    assert all(p.is_valid2 for p in passports)
    print('Tests passed')

def main(args):
    passports = [Passport()]
    for line in get_input(args.YEAR, args.DAY):
        if not line.strip():
            passports.append(Passport())
            continue
        passports[-1].parse_input(line)
    print(sum(p.is_valid for p in passports))
    print(sum(p.is_valid2 for p in passports))

