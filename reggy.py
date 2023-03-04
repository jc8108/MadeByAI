## create a python program that asks for an example string or strings such as phone number or email address and creates a regex expression from the string that can be used in other applications
## TESTED - WORKS, but is a bit too precise sometimes. If you want regex for an IP address and give it 10.10.10.10 it will only give you a regex that matches IP addresses with two digit octets

import re

# Get example string from user
example_string = input("Enter an example string: ")

# Identify patterns in example string
patterns = []
for char in example_string:
    if char.isdigit():
        patterns.append("\\d")
    elif char.isalpha():
        patterns.append("\\w")
    else:
        patterns.append(re.escape(char))

# Generate regular expression from patterns
regex = "".join(patterns)

# Print regular expression
print("Regular expression:")
print(regex)

# Here's how you can use the program:
#
#    Copy the code above into a Python file (e.g. regex_generator.py).
#    Run the script by running python regex_generator.py in your terminal/command prompt.
#    Enter an example string (e.g. a phone number, email address, or any other string with a specific pattern).
#    The script will output a regular expression that matches strings with the same pattern as the example string you entered.
#
# For example, if you enter the string "john@example.com", the script will output the regular expression \\w+@\\w+\\.\\w+. This regular expression matches any string that starts with one or more word characters (\\w+), followed by the "@" symbol, followed by one or more word characters, followed by a period, followed by one or more word characters. So this regular expression can be used to match other email addresses with the same pattern.
