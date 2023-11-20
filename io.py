short = open("short.txt", "w")
art = open("articles.txt", "w", encoding="UTF-8")
april = open("april.txt", "w", encoding="UTF-8")

def openAndRead(filename):
    fo=open(filename, encoding="UTF-8")
    lines = [line for line in fo.readlines()]
    fo.close()
    return lines

#print(openAndRead("wiki.txt"))

lines = openAndRead("wiki.txt")

short.write(str([x for x in lines if len(x) < 30]))
art.write(str([x for x in lines if x.startswith("Der") or x.startswith("Die") or x.startswith("Das")]))
april.write(str([x for x in lines if "April" in x]))

short.close()
art.close()
april.close()