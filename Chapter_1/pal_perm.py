# Check if a given string is a permutation of a palindrome
# EXAMPLE:
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco cta", etc.)

import re

def clean_string(string):
    regex = re.compile('[^a-zA-z]')
    return regex.sub('', string).lower()

def pal_perm(string):

    # Get rid of any whitespace or non-letter characters
    string = clean_string(string)

    char_count = set()
    for c in string:
        if c in char_count:
            char_count.remove(c)
        else:
            char_count.add(c)

    return len(char_count) <= 1

if __name__ == "__main__":
    # TEST
    print("Taco Cat:", pal_perm("Taco Cat"))
    # print True

    print("Taco59Cat:", pal_perm("Taco59Cat"))
    # print True

    print("FooBar:", pal_perm("FooBar"))
    # print False