import sys
import math
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
m = int(input())
inp_dict={}
out_dict={}

for i in range(n):
    input_name, input_signal = input().split()
    inp_dict[input_name]=input_signal
for i in range(m):
    output_name, _type, input_name_1, input_name_2 = input().split()
    out_dict[output_name]= [_type, input_name_1, input_name_2 ]

for i in range(m):
    # Write an answer using print
    answer = [key for key in out_dict.keys()][i]+" "
    if [value for value in out_dict.values()][i][0] == 'AND':
        x = [value for value in out_dict.values()][i][1]
        y = [value for value in out_dict.values()][i][2]
        op1 = inp_dict[x]
        op2 = inp_dict[y]
        for z in range(len(op1)):
            if op1[z]=="-" and op2[z]=="-":
                answer=answer+"-"
            else:
                answer=answer+"_"
    
    if [value for value in out_dict.values()][i][0] == 'OR':
        x = [value for value in out_dict.values()][i][1]
        y = [value for value in out_dict.values()][i][2]
        op1 = inp_dict[x]
        op2 = inp_dict[y]
        for z in range(len(op1)):
            if op1[z]=="-" or op2[z]=="-":
                answer=answer+"-"
            else:
                answer=answer+"_"
     

    if [value for value in out_dict.values()][i][0] == 'XOR':
        x = [value for value in out_dict.values()][i][1]
        y = [value for value in out_dict.values()][i][2]
        op1 = inp_dict[x]
        op2 = inp_dict[y]
        for z in range(len(op1)):
            if op1[z] == op2[z]:
                answer=answer+"_"
            else:
                answer=answer+"-"
    
    if [value for value in out_dict.values()][i][0] == 'NAND':
        x = [value for value in out_dict.values()][i][1]
        y = [value for value in out_dict.values()][i][2]
        op1 = inp_dict[x]
        op2 = inp_dict[y]
        for z in range(len(op1)):
            if op1[z]=="-" and op2[z]=="-":
                answer=answer+"_"
            else:
                answer=answer+"-"


    if [value for value in out_dict.values()][i][0] == 'NOR':
        x = [value for value in out_dict.values()][i][1]
        y = [value for value in out_dict.values()][i][2]
        op1 = inp_dict[x]
        op2 = inp_dict[y]
        for z in range(len(op1)):
            if op1[z]=="-" or op2[z]=="-":
                answer=answer+"_"
            else:
                answer=answer+"-"
    
    if [value for value in out_dict.values()][i][0] == 'NXOR':
        x = [value for value in out_dict.values()][i][1]
        y = [value for value in out_dict.values()][i][2]
        op1 = inp_dict[x]
        op2 = inp_dict[y]
        for z in range(len(op1)):
            if op1[z]==op2[z]:
                answer=answer+"-"
            else:
                answer=answer+"_"

    print(answer)

    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    
