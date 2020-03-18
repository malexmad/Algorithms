#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients, batches=0):

  for keys in recipe:
    try:
      if ingredients[keys] < recipe[keys]:
        return batches
      else:
        ingredients[keys] = ingredients[keys] - recipe[keys]
    except:
      return 0

  batches += 1
  return recipe_batches(recipe, ingredients, batches)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'cheese': 10 }
  ingredients = { 'milk': 198, 'butter': 52, 'cheese': 10 }
  print("\n{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))