# Write a func that create a dictionary with each key/value pair being the lowercase/uppercase versions of a letter.
# All letters will always be lowercase.

# input letters will be a list of single character
# lowercase strings (a-z)
def mapping(letters):
    # create dictionary
    result = {}
    # loop through the input
    for letter in letters:
        # add to the dictionary
        # make the letter uppercase for the value
        # leave lowercase for the key
        result[letter] = letter.upper()
    # return value
    return result
    # dictionary with key-values where the
    # key is the lowercase letter from the input
    # and value is the correlating uppercase letter
print(mapping(["a", "b", "e", "g"]))