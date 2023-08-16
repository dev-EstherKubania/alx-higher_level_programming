#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    current_value = 0
    previous_value = 0

    for symbol in reversed(roman_string):
        value = roman_numerals.get(symbol, 0)

        if value >= previous_value:
            current_value += value
        else:
            current_value -= value

        previous_value = value

    return current_value
