# The re documentation https://docs.python.org/2/library/re.htm
import sys
import re

# sys.argv is the list (of strings) of incoming parameters from the command line with [0] being the file that is running
# so the command: python Searcher.py "New Text Document.txt" "search" "NOTSearch" "Replacement.txt"
# looks like:
# sys.argv[0] = "Searcher.py"
# sys.argv[1] = "New Text Document.txt"
# sys.argv[2] = "search"
# sys.argv[3] = "NOTsearch"
# sys.argv[3] = "Replacement.txt"

# makes sure you have at least File Name and Search Expression
if len(sys.argv) < 3:
    print('Arguments: FileName SearchRegularExpression ReplacementText(Optional) ReplacementFileName(Optional)')
    exit(0)

print("The arguments are: ", str(sys.argv[1:]))
file_name = str(sys.argv[1])
expression = str(sys.argv[2])

# protects against not having Replacement values
try:
    replacement_text = str(sys.argv[3])
    replacement_file_name = str(sys.argv[4])
except IndexError:
    replacement_text = None
    replacement_file_name = file_name
    print('Missing replacement parameter, proceeding with find only.')

item_count = 0
logs = ''
log_file_name = file_name.replace(".", ".log.")  # making a log file so you can see what happened


# if the file has a bunch of escaped line returns this gets messy, but this will be a decent guess at the line number
def get_line_number(text, position):
    return text.count("\n", 0, position) + 1


# 'with' holds open a file reference 'safely'
# Could also be written file_text = open(file_name, "r").read() but then you have to go back and close it out later
with open(file_name, "r") as file:
    file_text = file.read()

    # You compile a pattern first and then "apply" it to strings
    # this lets you set all kinds of options on the pattern and use the same pattern more than once
    pattern = re.compile(expression)

    results = pattern.finditer(file_text)  # results is a list of "MatchObject"s

    # loop over every Match object convert to a string and add it to an output string
    for result in results:
        logs += 'Found: \"' + str(result.group(0)) + '\" estimated line number ' \
                + str(get_line_number(file_text, result.regs[0][0])) + ' ' + '\n'
        item_count += 1
    message = 'Found items: ' + str(item_count)
    print(message)

    if replacement_text:  # if we are doing replacements
        replacement = pattern.subn(replacement_text, file_text)
        # replacement returns a tuple with pos0 = "replaced text" and pos1 = number of replacements
        out_text = replacement[0]
        message = "Replaced items: " + str(replacement[1])
        print(message)

        # Outputs our replaced text into a file
        with open(replacement_file_name, "w") as out:
            out.write(out_text)

    # Outputs what was found and the number of replacements into a log file
    with open(log_file_name, "w") as out:
        out.write(logs)
        out.write(message)


print('See ' + log_file_name + ' for details.')


