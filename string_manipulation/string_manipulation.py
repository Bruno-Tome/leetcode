"""
Chapter: String Manipulation
Problem Set: Character Manipulation

Source:
Beyond Cracking the Coding Interview

Statement (summary):
This file contains my personal solutions to the first character manipulation
questions from the String Manipulation chapter.

The exercises focus on basic ASCII-based character operations, using only
numeric character conversions such as ord() and chr().

Included questions:
- Question 1: implement a function that checks whether a character is
  alphanumeric, that is, whether it is a lowercase letter, an uppercase
  letter, or a digit between '0' and '9'.
- Question 2: implement a function that converts a lowercase character to
  uppercase. If the character is not lowercase, the function should remain
  unchanged.

Approach:
The goal of this file is to practice low-level character manipulation by
working directly with ASCII ranges instead of relying on higher-level
built-in string methods.

Concepts practiced:
- ASCII value ranges
- character classification
- lowercase and uppercase conversion
- use of ord() and chr()

Time Complexity:
Each function in this file is expected to run in O(1), since each operation
depends only on a single character.

Space Complexity:
O(1)
"""

def is_uppercase(c):
    return ord(c) >= ord('A') and ord(c) <= ord("Z")

def is_lowercase(c):
    return ord(c) >= ord('a') and ord(c) <= ord("z")

def is_digit(c):
    return ord(c) >= ord("0") and ord(c) <= ord("9")

def is_alphanumeric(c):
    return is_uppercase(c) or is_lowercase(c) or is_digit(c)

def to_uppercase(c):
    if not is_lowercase(c):
        return c
    return chr(ord(c) - ord('a') + ord("A"))

def split(string, char):
    string_array = []
    temp_string = ""
    for character in string:
        if char == character:
            string_array.append(temp_string)
            temp_string = ""
        else:
            temp_string += character
    string_array.append(temp_string)
    return string_array

def join(array, string):
    string_to_build = ""

    for item in array:
        string_to_build += item
        if item is not array[-1]:
            string_to_build += string

    return string_to_build

def index_of(string,substring):
    substr_length = len(substring)
    index = -1
    if(substring == ""):
        return -1
    for i,character in enumerate(string):
        if i + substr_length <= len(string):
            tempString = string[i:i+substr_length]
            if(tempString == substring):
                index = i
                break
            
    return index

if __name__ == "__main__":
    print("=== TESTES DE CARACTERE ===")
    test_chars = ["a", "Z", "5", "@", "ç"]

    for ch in test_chars:
        print(f"Caractere: {ch}")
        print(f"  is_uppercase: {is_uppercase(ch)}")
        print(f"  is_lowercase: {is_lowercase(ch)}")
        print(f"  is_digit: {is_digit(ch)}")
        print(f"  is_alphanumeric: {is_alphanumeric(ch)}")
        print(f"  to_uppercase: {to_uppercase(ch)}")
        print()

    print("=== TESTES DE SPLIT ===")
    placeholder_text_1 = "lorem ipsum dolor sit amet"
    placeholder_text_2 = "alpha-beta-gamma-delta"
    placeholder_text_3 = "one,two,three,four"

    print(f"Texto: {placeholder_text_1}")
    print("Split por espaço:", split(placeholder_text_1, " "))
    print()

    print(f"Texto: {placeholder_text_2}")
    print("Split por '-':", split(placeholder_text_2, "-"))
    print()

    print(f"Texto: {placeholder_text_3}")
    print("Split por ',':", split(placeholder_text_3, ","))
    print()

    print("=== TESTES DE JOIN ===")
    array_1 = ["lorem", "ipsum", "dolor", "sit", "amet"]
    array_2 = ["alpha", "beta", "gamma"]
    array_3 = ["one", "two", "three"]

    print("Join com espaço:")
    print(join(array_1, " "))
    print()

    print("Join com hífen:")
    print(join(array_2, "-"))
    print()

    print("Join com vírgula e espaço:")
    print(join(array_3, ", "))
    print()

    test_cases = [
    # Casos em que funciona
    ("abcde", "a", 0),
    ("abcde", "ab", 0),
    ("abcde", "abc", 0),
    ("hello", "h", 0),
    ("hello", "he", 0),

    # Casos que mostram problema da função
    ("abcde", "b", 1),
    ("abcde", "cd", 2),
    ("hello world", "world", 6),
    ("banana", "ana", 1),

    # Casos de borda
    ("abc", "abc", 0),
    ("abc", "abcd", -1),
    ("abc", "qwer", -1),
    ("", "", -1),
    ("abc", "", -1),
]

for string, substring, expected in test_cases:
    result = index_of(string, substring)
    print(f"string='{string}' | substring='{substring}'")
    print(f"esperado: {expected} | obtido: {result}")
    print(f"status: {'OK' if result == expected else 'FALHOU'}")
    print()