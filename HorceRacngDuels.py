import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
li=([])
for i in range(n):
    pi = int(input())
    li.append(pi)

# Write an answer using print
min=abs(li[1]-li[0])
li.sort()
for i in range(n):
    if ((abs(li[i]-li[i-1]) < min)):
        min = abs(li[i]-li[i-1])
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(min)