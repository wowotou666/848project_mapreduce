#!/usr/bin/env python

import sys
from collections import Counter

global_counter = Counter()
num = 10
current_key = None
values = []

for line in sys.stdin:
    line = line.strip()
    key, word, count = line.split('\t', 2)
    count = int(count)
    global_counter[word] += count

sorted_words = sorted(global_counter.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_words[:num]:
    print(f"{word}\t{count}")

