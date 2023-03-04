## create a script that takes a domain name as input and creates a list of potential typo-squatting domains
## write the same script but also replace the letter q with the letter g and vice versa. 
# also replace m with n and vice versa. also replace c with o and vice versa. 
# also replace l with I and vice versa. but only do one the previous replacements not all of them.
# UNTESTED, but output from the AI as examples looks 50/50

import re
import sys

# Define common typos and the rules for replacing letters
TYPOS = {
    'q': 'g',
    'g': 'q',
    'm': 'n',
    'n': 'm',
    'c': 'o',
    'o': 'c',
    'l': 'I',
    'I': 'l',
}

# Function to generate potential typo-squatting domains
def generate_typosquat_domains(domain):
    # Split the domain into the base name and TLD
    base, tld = domain.split('.')

    # Generate a list of potential typo-squatting domains
    typosquat_domains = []
    for typo, replacement in TYPOS.items():
        # Replace the specified letter with the replacement letter
        typo_base = base.replace(typo, replacement)
        # Add the TLD to the end of the base name
        typosquat_domains.append('{}.{}'.format(typo_base, tld))

    return typosquat_domains

if __name__ == '__main__':
    # Get the domain name from the command line arguments
    if len(sys.argv) > 1:
        domain = sys.argv[1]
    else:
        print('Error: no domain name provided')
        sys.exit(1)

    # Generate potential typo-squatting domains for the input domain
    typosquat_domains = generate_typosquat_domains(domain)

    # Print the list of potential typo-squatting domains
    print('Potential typo-squatting domains for {}:'.format(domain))
    for typosquat_domain in typosquat_domains:
        print(typosquat_domain)
