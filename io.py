shortFile = open("short.txt", "r")
print(shortFile.read())
shortFile.close()

wiki = open("wiki.txt", "r", encoding="utf-8")
lines = wiki.readlines()
numberOfLines = len(lines)
print(numberOfLines)
wiki.close()

for x in range(numberOfLines):
    wiki = open("wiki.txt", "r", encoding="utf-8")
    currentLine = wiki.readline()
    if(len(currentLine) <= 30):
        shortFile = open("short.txt", "w")
        shortFile.write(currentLine)
        shortFile.close()

shortFile = open("short.txt", "r")
print("Finales ShortFile: ")
print(shortFile.read())