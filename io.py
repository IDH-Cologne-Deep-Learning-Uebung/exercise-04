
#read wiki.txt
s = open("exercise-04/wiki.txt")
text = []
for l in s.readlines():
    text.append(l)
s.close

#function   -File und Liste rein, write datei
def function1(filename, list):
    Text = open(filename, "w")
    for line in list:
        Text.write(line)
    Text.close


#filters ->3 text files

#short.txt -> 30char max  sentences 
sT = [s for s in text if (len(s)<=30)]
#print(sT)
function1("exercise-04/short.txt", sT)

#articles.txt -> start Der/Die/Das
aT = [s for s in text if s.startswith(("Der ","Die ","Das "))] # Leerzeichen wegen "Dies"...
#print(aT)
function1("exercise-04/article.txt", aT)

#april.txt -> sentences with April
apT = [s for s in text if "April" in s]
#print(apT)
function1("exercise-04/april.txt", apT)