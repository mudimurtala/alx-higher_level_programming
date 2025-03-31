#!/usr/bin/env python3

import hidden_4

items = dir(hidden_4)

for i in items:
    if not i.startswith("__"):
        print(sorted(items))