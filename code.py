"""
Given an object/dictionary with keys and values that consist of both strings and integers, design an algorithm to calculate and return the sum of all of the numeric values.
For example, given the following object/dictionary as input:
{
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}
Your algorithm should return 41, the sum of the values 23 and 18.
You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.
"""

# loop through all key/value pairs in dictionary
# if value is an integer (numeric) add to some sort running total
# return that total


def add_int(my_dict):
    running_total = 0
    for value in my_dict.values():
        if type(value) == int:
            running_total += value
    return running_total
    # return sum([i for i in my_dict.values() if type(i) == int])


test_dict = {"cat": "bob", "dog": 23, 19: 18, 90: "fish", "test": 10}

print(add_int(test_dict))
