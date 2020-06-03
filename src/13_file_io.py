"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"
# YOUR CODE HERE
with open("foo.txt", "r") as fooFile:  # with open to automatically close file, "r" for read only, fooFile variable name
    for words in fooFile:  # for each word/line in fooFile(foo.txt) print them.
        print(words)   # must be cd'd in src to run, (that's where foo.txt exists)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain
# YOUR CODE HERE
barFile = open("bar.txt", "w")
barFile.write("Test line 1\nTest line 2\nTest line 3")
barFile.close()

with open("bar.txt", "r") as barFile:
    for words in barFile:
        print(words)