/*
Chapter: String Manipulation
Problem Set: Character Manipulation

Source:
Beyond Cracking the Coding Interview

Statement (summary):
This file contains my personal solutions to the first character manipulation
questions from the String Manipulation chapter.

The exercises focus on basic ASCII-based character operations, using only
numeric character conversions such as charCodeAt() and String.fromCharCode().

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
- use of charCodeAt() and String.fromCharCode()

Time Complexity:
Each function in this file is expected to run in O(1), since each operation
depends only on a single character.

Space Complexity:
O(1)
*/

function isUppercase(c) {
  return (
    c.charCodeAt(0) >= "A".charCodeAt(0) && c.charCodeAt(0) <= "Z".charCodeAt(0)
  );
}

function isLowercase(c) {
  return (
    c.charCodeAt(0) >= "a".charCodeAt(0) && c.charCodeAt(0) <= "z".charCodeAt(0)
  );
}

function isDigit(c) {
  return (
    c.charCodeAt(0) >= "0".charCodeAt(0) && c.charCodeAt(0) <= "9".charCodeAt(0)
  );
}

function isAlphanumeric(c) {
  return isUppercase(c) || isLowercase(c) || isDigit(c);
}

if (require.main === module) {
  const string = "Hello, World! 123";
  const c = "ç";
  const c1 = "z";

  //   console.log(isAlphanumeric(c));

  console.log(
    ((string) => {
      return string[0];
    })(string),
  );
  Array(string).map((char) => {
    console.log(char);
    console.log(isAlphanumeric(char));
  });

  //   console.log(isAlphanumeric(c1));
  //   console.log(c.charCodeAt(0));
  //   console.log(c1.charCodeAt(0));

  //   for (let char = 150; char < 300; char++) {
  //     console.log(char);
  //     const character = String.fromCharCode(char);
  //     console.log(character);
  //   }
}

let lowercaseA = "a";

let string = new Number(123);
