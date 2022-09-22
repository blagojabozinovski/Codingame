import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()
bimsg = ''.join(format(ord(x), 'b').zfill(7) for x in message)

to_chuck = ''
for index, n in enumerate(bimsg):
    if index >= 1 and bimsg[index] == bimsg[index-1]:
        to_chuck+='0'
    else: 
        if n == '1':
            to_chuck+=' 0 0'
        elif n == '0':
            to_chuck+=' 00 0'
to_chuck = to_chuck[1:]

# To debug: print("Debug messages...", file=sys.stderr, flush=True)
# solution modified after stackoverflow search


print(to_chuck)