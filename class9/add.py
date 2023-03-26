#!/bin/pypy

def add(a,b):
    return a + b

for _ in range(100000000):
    add(1,4)
