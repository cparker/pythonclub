__author__ = 'cparker'


scrambler = {
    "s" : "u",
    "t" : "o",
    "r" : "i",
    "l" : "e",
    "n" : "a",
    "a" : "n",
    "e" : "l",
    "i" : "r",
    "o" : "t",
    "u" : "s",
}

unscrambler = {}
for (original,replacement) in scrambler.items():
    unscrambler[replacement] = original

message = "Q: how many programmers does it take to change a light bulb?  A: none, that's a hardware problem."

secretMessage = ""
for letter in message.lower():
    if letter in scrambler:
        secretMessage += scrambler[letter]
    else:
        secretMessage += letter

clearMessage = ""
for letter in secretMessage:
    if letter in unscrambler:
        clearMessage += unscrambler[letter]
    else:
        clearMessage += letter

print(message)
print(secretMessage)
print(clearMessage)


