import time

def getText():
    while True:
        try:
            filename = getFileName()
            with open(filename, "r") as file:
                txt = file.read() #Assuming the file is formmated so each alterable sentence is in its own line.
            break
        except IOError:
            print("There is no such file.\nPlease try again.\n")

    return txt

def getFileName():
    print("What is the name of the text file containing your story?")
    name = input()
    return name

def appendText(originalText):
    newText = ""
    originalText = originalText.split("\n")
    for row in originalText:
        if row == "":
            break
        else:
            print("\nPlease insert you word in the empty spot")
            print(row)
            row = row.replace("___", input())
            newText += row + "\n"
    print("\n\n" + newText)


storyTxt = getText()
print(storyTxt)
print("\n---------------------------")
appendText(storyTxt)
