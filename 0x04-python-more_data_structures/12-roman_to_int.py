#!/usr/bin/python3
def roman_to_int(roman_string):
    val = 0
    if roman_string and type(roman_string) is str and roman_string.isalpha():
        r = roman_string.upper()
        for i in range(len(r)):
            if r[i] is 'I':
                if i + 1 >= len(r) or r[i + 1] is 'I':
                    v += 1
                else:
                    v -= 1
            elif r[i] is 'V':
                v += 5
            elif r[i] is 'X':
                if i + 1 >= len(r) or r[i + 1] in 'IVX':
                    v += 10
                else:
                    v -= 10
            elif r[i] is 'L':
                v += 50
            elif r[i] is 'C':
                if i + 1 >= len(r) or r[i + 1] in 'IVXLC':
                    v += 100
                else:
                    v -= 100
            elif r[i] is 'D':
                v += 500
            elif r[i] is 'M':
                if i + 1 >= len(r) or r[i + 1] in 'IVXLCD':
                    v += 1000
                else:
                    v -= 1000
            else:
                return 0
    return v
