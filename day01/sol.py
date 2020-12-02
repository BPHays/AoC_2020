#!/usr/bin/env python3

nums = {int(num) for num in open("input").readlines()}
num_pairs = {x + y: x * y for x in nums for y in nums}

print(num_pairs[2020])

for x, prod in num_pairs.items():
    if (2020 - x) in nums:
        print((2020 - x) * prod)
        break
