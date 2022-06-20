# Given two user inputed words write a program that determines which word is longer

first_word = input('Enter the first word: ')
second_word = input('Enter the second word: ')

if first_word == second_word:
  print('The words are the same, enter a different word each time')
elif len(first_word) > len(second_word):
  print(f'{first_word} is longer than {second_word}')
elif len(second_word) > len(first_word):
  print(f'{second_word} is longer than {first_word}')
else:
  print(f'{first_word} and {second_word} are the same length')
