#!/usr/bin/env python3

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

#print(greet('en'))
#print(greet('es'))
#print(greet('fr'))

print(greet('en'), 'Glenn')
print(greet('es'), 'Sally')
print(greet('fr'), 'Michael')

#def greet():
#    return "Hello"

#print(greet(), "Glenn")
#print(greet(), "Sally")
