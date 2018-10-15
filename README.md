# PythonRegex
Example of how to use python regx to do searching in a file

Put these files in a directory and run the following command (in the directory)

python Searcher.py "New Text Document.txt" "(?<!\d)search" "NOTsearch" "Replaced.txt"

It finds all iterations of the word "search" not preceeded by a number and replaces them with NOTsearch reporting results in a log file
