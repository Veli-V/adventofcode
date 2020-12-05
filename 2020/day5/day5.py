#!/usr/bin/env python3
import sys

input_file = "test.txt"
#input_file = "input.txt"


with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]

print(data)