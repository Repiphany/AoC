#!/usr/bin/env python3

import sys
import argparse
import importlib
import requests
import json
import pathlib
import shutil
import re
import time

root = pathlib.Path(__file__).parent
with open(root / 'config.json', 'r') as f:
    config = json.load(f)

from .input import download_input

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('YEAR', type = int, nargs = '?')
    parser.add_argument('DAY', type = int, nargs = '?')
    parser.add_argument('-l', '--list', action = 'store_true')
    parser.add_argument('-n', '--new', action = 'store_true')
    parser.add_argument('-g', '--get-input', action = 'store_true')
    parser.add_argument('-t', '--test-case', action = 'store_true')
    args = parser.parse_args()
    if args.YEAR is None or args.list:
        for f, match in [(f, match) for f in sorted(root.iterdir())
                if (match := re.findall(f'year_(\d+)_day_(\d+).py', str(f)))]:
            y, d = [int(i) for i in match[0]]
            print(f'{f}, {y}/{d:02d}')
    if args.get_input:
        download_input(args.YEAR, args.DAY, config['session'])
        return
    if args.new:
        template = pathlib.Path(root / 'template.py')
        day = pathlib.Path(root / f'year_{args.YEAR}_day_{args.DAY:02d}.py')
        shutil.copy(template, day)
        print(f'Template copied to {day}')
        return
    try:
        day = importlib.import_module(f'.year_{args.YEAR}_day_{args.DAY:02d}', package = 'aoc')
    except ModuleNotFoundError:
        print(f'Puzzle not found: {args.YEAR}/{args.DAY:02d}')
        return
    if args.test_case:
        day.test(args)
    else:
        st = time.time()
        day.main(args)
        print(f'Runtime: {time.time() - st:.3f} s')

