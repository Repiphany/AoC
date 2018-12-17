#!/usr/bin/env python3
import re, collections
tracker = collections.defaultdict(collections.Counter)
with open('input', 'r') as f:
    log = sorted([line.strip() for line in f])
for line in log:
    timestamp, action = line.split('] ')
    if action.startswith('G'):
        active_guard = int(re.findall(r'\d+', action)[0])
    elif action.startswith('f'):
        sleep_start = int(re.findall(r'\d+', timestamp)[-1])
    else:
        sleep_end = int(re.findall(r'\d+', timestamp)[-1])
        tracker[active_guard].update(range(sleep_start, sleep_end))
most_asleep, minutes = max(tracker.items(), key = lambda x : sum(x[1].values()))
print(minutes.most_common()[0][0] * most_asleep)
most_asleep, minutes = max(tracker.items(), key = lambda x : max(x[1].values()))
print(minutes.most_common()[0][0] * most_asleep)
