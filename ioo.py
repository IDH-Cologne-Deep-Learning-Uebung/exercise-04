
def opentxt(filepath):
    try:
        content = open(filepath, 'r')
        return content
    except FileNotFoundError:
        print("File not found!")

def check_sentence_length():
    temp = ''
    content = opentxt('wiki.txt')
    for line in content:
        sentences = line.split('.')
        for sentence in sentences:
            if len(sentence.strip()) < 30:
                temp += sentence
    with open('short.txt', 'w') as file:
        file.write(temp)

def startwith():
    temp = ''
    content = opentxt('wiki.txt')
    for line in content:
        sentences = line.split('.')
        for sentence in sentences:
            boolDer = sentence.startswith("Der")
            boolDas = sentence.startswith("Das")
            boolDie = sentence.startswith("Die")
            if boolDie or boolDas or boolDer :
                temp += sentence
    with open('articles.txt', 'w') as file:
        file.write(temp)

def Containsapril():
    temp = ''
    content = opentxt('wiki.txt')
    for line in content:
        sentences = line.split('.')
        for sentence in sentences:
            if sentence.__contains__('April'):
                temp += sentence
    with open('april.txt', 'w') as file:
        file.write(temp)

#check_sentence_length()
#startwith()
#Containsapril()