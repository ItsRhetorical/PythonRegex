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
file_text = file.read()

# You compile a pattern first and then "apply" it to search strings
# this lets you set all kinds of options on the
pattern = re.compile(expression)

outText = ''
results = pattern.finditer(file_text)

for result in results:
    outText += str(result) + '\n'

# Outputs our re command results into a file
out = open("test.txt", "w")
out.write(str(outText))
out.close()

