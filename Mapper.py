#!/usr/bin/env python

import sys
from collections import Counter

num = 10
local_counter = Counter()

for line in sys.stdin:
    line = line.strip().lower()
    words = line.split()
    for word in words:
        local_counter[word] += 1

sorted_words = sorted(local_counter.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_words[:num]:
    print(f"null\t{word}\t{count}")

