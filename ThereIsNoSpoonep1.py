import sys
import math

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
lines = []
for i in range(height):
    line = input()  # width characters, each either 0 or .
    lines.append(list(line))
for j in range(height):
    for k in range(width):
       if lines[j][k]==".":
           continue
       rk = rj = bk = bj = -1
       try:
           for tk in range(k+1,width):
               if(lines[y][tk]=='0'):
                   rk = tk
                   rj = j
                   break
       except Exception:
           pass
       try:
           for tj in range(j+1, height):
               if(lines[tj][k]=='0'):
                   bk = k
                   bj =tj
                   break
       except Exception:
           pass
       print("{0} {1} {2} {3} {4} {5}".format(k, j, rk, rj, bk, bj))
