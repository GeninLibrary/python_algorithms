def alphabet_position(given_string):
    # Loops through the given_string testing each value against an arrayed alphabet.
    # posStr will store the index value of each element in given_string

    alphabet = ['','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    posStr = ""
    
    for c in given_string:
        for l in alphabet:
            if l == c:
                posStr = posStr + str(alphabet.index(l)) + " "
            else:
                continue
    posStr = posStr[:-1]        # removes the final character of the array, an unnecessary whitespace 
    print (posStr)
    return posStr



def alphabet_position(text):
return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

# c.isalpha() checks whether c is an *alpha*bet. ' is not an alphabet and is skipped.

# ord() in this case returns the ascii value of the character. If you don't know what ascii values are, you should lookup how characters are stored internally in a computer.
# The ascii values for 'a' to 'z' are 97 to 122 resp. Subtracting 96 gives a number between 1-26.

