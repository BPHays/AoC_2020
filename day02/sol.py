#!/usr/bin/env python3

import re

print(len(
    [
        None for
        l, h, c, fack, s in
        [
            re.split("-|:| ", row.strip()) for
            row in
            open("input").readlines()] if
            (x := len([None for c1 in s if c == c1])) >= int(l) and x <= int(h)
    ]
))

print(len([
        None for
        l, h, c, fack, s in
        [
            re.split("-|:| ", row.strip()) for
            row in
            open("input").readlines()] if
            (s[int(l)-1] == c) ^ (s[int(h)-1] == c)
    ]
))
