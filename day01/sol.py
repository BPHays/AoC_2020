#!/usr/bin/env python3

nums = {int(num) for num in open("input").readlines()}
num_pairs = {x + y: x * y for x in nums for y in nums}

for x in nums:
    if (2020 - x) in nums:
        print(x * (2020 - x))
        break

for x, prod in num_pairs.items():
    if (2020 - x) in nums:
        print((2020 - x) * prod)
        break
