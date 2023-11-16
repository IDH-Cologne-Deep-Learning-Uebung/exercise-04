wikiText = "./wiki.txt"
with open(wikiText, "r") as f:
    shortText= open("short.txt", 'w')
    articleText= open("articles.txt", "w")
    aprilText =open("april.txt", "w")
    #for line in f.readlines():

    for line in f.readlines():

        if len(line) < 30:
            shortText.write(line)
        
        if line.startswith("Der") or line.startswith("Das") or line.startswith("Die")   :
            articleText.write(line)

        if "April" in line:
            aprilText.write(line)

        


    shortText.close()
    articleText.close()
    aprilText.close()
       
    