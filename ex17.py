"""
Find the total number of letters to spell out
all the numbers from 1 to 1000 written out in words
(include 'and' in 'one hundred and fifteen')
"""
def spellout(num):
    converter = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'fourty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        100: 'hundred'
    }
    return converter.get(num, 'not found')

def count_letters(num):
    number_in_words = ""
    if num > 1000 or num < 0:
        return 'Invalid input'
    else:
        if num == 1000:
            return 11
        elif num >= 100:
            hundreds = num / 100
            number_in_words += "{} hundred".format(spellout(hundreds))
        else:
            number_in_words += "{}".format(spellout(num))
        return len(number_in_words.replace(' ', ''))

assert count_letters(1000) == 11
assert count_letters(100) == 10
assert count_letters(200) == 10
assert count_letters(19) == 8
assert count_letters(11) == 6
assert count_letters(10) == 3
assert count_letters(9) == 4
