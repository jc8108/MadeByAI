# write a python program that takes a regular expression as input and outputs examples of what that regular expression could be
# TESTED! does not work haha issue is with main function, have not fully debugged

import re
import random
import string

def generate_examples(regex, num_examples=10):
    examples = []
    for i in range(num_examples):
        while True:
            # Generate a random string of printable ASCII characters
            candidate = ''.join(random.choices(string.printable, k=50))
            # Check if the string matches the regular expression
            if re.match(regex, candidate):
                examples.append(candidate)
                break
    return examples

# Example usage:
regex = input("Enter regular expression to evaluate:\n") #I changed this to specify what the program wants you to do
examples = generate_examples(regex)
print(examples)
