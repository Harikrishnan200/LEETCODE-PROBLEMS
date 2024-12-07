# Leetcode : Convert an integer to Roman

def int_to_roman(num):

    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    
    roman_numeral = ""
    for i in range(len(val)):
        while num >= val[i]:
            roman_numeral += syms[i]
            num -= val[i]
    return roman_numeral

number = 11
print(f"Roman numeral of {number} is {int_to_roman(number)}")
