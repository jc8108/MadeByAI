## write a python program that takes input and then does google dorking with all the different parameters and puts the output into a text file called dorks.txt
## UNTESTED 

import googlesearch

# Get user input
query = input("Enter your query: ")

# Define dork parameters
params = ["", "site:", "intitle:", "inurl:", "filetype:"]

# Generate dorks
dorks = [query + param for param in params]

# Open file for writing
with open("dorks.txt", "w") as f:
    # Loop through each dork
    for dork in dorks:
        # Perform Google search
        search_results = googlesearch.search(dork, num_results=10)
        # Write results to file
        f.write("Results for " + dork + ":\n")
        for result in search_results:
            f.write(result + "\n")
        f.write("\n")
