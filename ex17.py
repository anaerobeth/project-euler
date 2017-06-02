"""
Find the total number of letters to spell out
all the numbers from 1 to 1000 written out in words
(include 'and' in 'one hundred and fifteen')
"""
def spellout(num):
    converter = {
        0: 'zero',
        1: 'one',
        1000: 'one thousand'
    }
    return converter.get(num, 'out of range')

def count_letters(num):
    return len(spellout(num).replace(' ', ''))

print(count_letters(1000))
