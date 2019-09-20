#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

questions = {
  "strong": "Do ye like yer drinks strong?",
  "salty": "Do ye like it with a salty tang?",
  "bitter": "Are ye a lubber who likes it bitter?",
  "sweet": "Would ye like a bit of sweetness with yer poison?",
  "fruity": "Are ye one for a fruity finish?",
}
ingredients = {
  "strong": ["glug of rum", "slug of whisky", "splash of gin"],
  "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
  "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
  "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
  "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def fun():
  print('Nhap vao 1 trong cac gia tri sau', questions.keys())
  user_taste = raw_input()

  if user_taste in ingredients:
    tastes = ingredients[user_taste]
    random_taste = random.randint(0, len(tastes)-1)
    print(tastes[random_taste])
  else:
    print('no taste')


#Given two above dictionaries, construct the Python program (using functions) to ask users entering their
#tastes and then match randomly with the ingredients (print out outputs for user).
fun()

