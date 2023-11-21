fh = open(wiki.txt)
for line in fh.readlines():
    wiki = []
    wiki.append(line)
fh.close()