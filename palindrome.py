# -*- coding: utf-8 -*-

def palindrome2(word):
    reversed_letters = word[::-1]
    if reversed_letters == word:
        return True
    return False

def palindrome(word):
    reversed_letters = []
    for letter in word:
        reversed_letters.insert(0, letter)
    
    reversed_word = ''.join(reversed_letters)

    if reversed_word == word:
        return True

    return False

if __name__ == '__main__':
    word = str(raw_input('Ingrese palabra: '))
    result = palindrome2(word)
    if result is True:
        print('{} es una palabra palindrome'.format(word))
    else:
        print('{} no es una palabra palindrome'.format(word))
