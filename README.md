# PythonRegex
Example of how to use python regx to do searching in a file

Put these files in a directory and run the followig command (in the directory)
python Searcher.py "New Text Document.txt" "(?<!\d)search"

It finds all iterations of the word "search" not preceeded by a number and outputs them to the text.txt file
