#!/usr/bin/env python3

import pathlib
import requests
root = pathlib.Path(__file__).parent

def download_input(year, day, session):
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    r = requests.get(url, cookies = {'session': session})
    if r.status_code == 200:
        d = root / f'input/{year}'
        d.mkdir(parents = True, exist_ok = True)
        with open(d / f'{day}', 'w') as f:
            f.write(r.text)
            print(f"{url} saved to {d/f'{day}'}")
    else:
        print(f'Error loading {url}: {r.status_code}')

def get_input(year, day):
    with open(root / f'input/{year}/{day}', 'r') as f:
        yield from f
