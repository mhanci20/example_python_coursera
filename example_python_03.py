#!/usr/bin/env python3

while True:
      line = input('> ')
      if line[0] == '#' :
          continue
      if line == 'done' :
          break
      print(line)
print('Done!')
