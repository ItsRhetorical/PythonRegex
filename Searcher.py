# The re documentation https://docs.python.org/2/library/re.htm
import sys
import re

# sys.argv is the list (of strings) of incoming parameters from the command line with [0] being the file that is running
# so this command: python Searcher.py "New Text Document.txt" "search"
# looks like sys.argv[0] = "Searcher.py"; sys.argv[1] = "New Text Document.txt"; sys.argv[2] = "search"
print("The arguments are: ", str(sys.argv))
filename = str(sys.argv[1])
expression = str(sys.argv[2])

# file is a reference to the open file , f is a reference to the text of that file (as one big string)
file = open(filename, "r")
f = file.read()

results = ''  # a string to store our results
location = 0  # stores the last searched location in the file

# You compile a pattern first and then "apply" it to search strings
# this lets you set all kinds of options on the
pattern = re.compile(expression)

while True:
    # Applies Regular Expression to your file text starting after the last place we found something
    m = pattern.search(f, location)

    # If we didn't find anything or our string was the end of the file stop looping
    if m is None or location >= len(f):
        break

    # add whatever the "MatchObject" was on our search to our new string
    # (and a new line character to make it easier to read)
    results += str(m) + '\n'

    # Update location to the end of the found string so we don't search it again
    location = m.end()



# Outputs our re command results into a file
out = open("test.txt", "w")
out.write(str(results))
out.close()


