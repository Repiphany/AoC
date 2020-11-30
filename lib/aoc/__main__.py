#!/usr/bin/env python3

import sys
import argparse
import importlib
import requests
import json
import pathlib

root = pathlib.Path(__file__).parent
with open(root / 'config.json', 'r') as f:
    config = json.load(f)

from .input import download_input

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('YEAR', type = int)
    parser.add_argument('DAY', type = int)
    parser.add_argument('-g', '--get-input', action = 'store_true')
    parser.add_argument('-t', '--test-case', action = 'store_true')
    args = parser.parse_args()
    if args.get_input:
        download_input(args.YEAR, args.DAY, config['session'])
        return
    try:
        day = importlib.import_module(f'.year_{args.YEAR}_day_{args.DAY:02d}', package = 'aoc')
    except ModuleNotFoundError:
        print(f'Puzzle not found: {args.YEAR}/{args.DAY:02d}')
        return
    if args.test_case:
        day.test(args)
    else:
        day.main(args)

