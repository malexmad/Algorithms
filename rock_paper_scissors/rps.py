#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  rps = [['rock'], ['paper'], ['scissors']]

  combo = []
  if n == 0:
    return [[]]
  if n == 1:
    return rps

  rounds = rock_paper_scissors(n-1)

  for round in rounds:
    for play in rps:

      np = round+play
      combo.append(np)
  return combo



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')