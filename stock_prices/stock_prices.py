#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # empty list to append all possible profit, setting ndx to change starting position
  profit = []
  ndx = 0

  for i in range(0, len(prices)-1):
    ndx += 1
    for j in range(ndx, len(prices)):
      profit.append(prices[j] - prices[i])

  return max(profit)

# find_max_profit([1050, 270, 1540, 3800, 2])
# find_max_profit([100, 90, 80, 50, 20, 10])

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))