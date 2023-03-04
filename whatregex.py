# write a python program that takes a regular expression as input and outputs examples of what that regular expression could be

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
regex = input()
examples = generate_examples(regex)
print(examples)
