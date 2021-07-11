message = raw_input(">")
words = message.split(" ")
emoji = {
    ":)": "(smile_face)",
    ":(": "(sad_face)"
}

output = ""
for word in words:
    output += emoji.get(word, word) +" "
