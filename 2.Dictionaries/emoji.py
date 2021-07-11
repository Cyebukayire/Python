def convertEmoji(message):
    words = message.split(" ")
    emoji = {
        ":)": "(smily_face)",
        ":(": "(sad_face)"
    }
    output = ""
    for word in words:
        output += emoji.get(word, word) +" "
    return output


message = raw_input(">")
print (convertEmoji(message=message))
