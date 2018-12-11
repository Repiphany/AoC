#!/usr/bin/env python3

import re
import collections

def part_1(log):
    sleep_tracker = collections.defaultdict(collections.Counter)
    for line in log:
        timestamp, action = line.split('] ')
        if action.startswith('G'):
            active_guard = int(re.findall(r'\d+', action)[0])
        if action.startswith('f'):
            sleep_start = int(re.findall(r'\d+', timestamp)[-1])
        if action.startswith('w'):
            sleep_end = int(re.findall(r'\d+', timestamp)[-1])
            sleep_tracker[active_guard].update(range(sleep_start, sleep_end)) 
    most_asleep, minutes = sorted(sleep_tracker.items(),
            key = lambda x : sum(x[1].values()))[-1]
    m = minutes.most_common()[0][0]
    print(m*most_asleep)

def part_2(log):
    sleep_tracker = collections.defaultdict(collections.Counter)
    for line in log:
        timestamp, action = line.split('] ')
        if action.startswith('G'):
            active_guard = int(re.findall(r'\d+', action)[0])
        if action.startswith('f'):
            sleep_start = int(re.findall(r'\d+', timestamp)[-1])
        if action.startswith('w'):
            sleep_end = int(re.findall(r'\d+', timestamp)[-1])
            sleep_tracker[active_guard].update(range(sleep_start, sleep_end)) 
    most_asleep, minutes = sorted(sleep_tracker.items(),
            key = lambda x : max(x[1].values()))[-1]
    m = minutes.most_common()[0][0]
    print(m*most_asleep)

if __name__ == '__main__':
    with open('input', 'r') as f:
        log = [line.strip() for line in f]

    # sorting chronologically
    log.sort(key = lambda x : tuple(int(i) for i in re.findall(r'\d+', x)))
    part_1(log)
    part_2(log)
