def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Die Datei {file_path} wurde nicht gefunden.")
        return None
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
        return None

def filter_short_sentences(sentences):
    short_sentences = [sentence.strip() for sentence in sentences if len(sentence) < 30]
    return short_sentences
"""
def filter_articles(sentences):
    article_sentences 
    if article_sentences == [sentence.strip() for sentence in sentences if sentence.startswith(("Der")) or sentence.startswith(("Die")) or sentence.startswith(("Das"))]:
        return article_sentences
"""
def filter_articles(sentences):
    article_sentences = [sentence.strip() for sentence in sentences if sentence.startswith(("Der")) or sentence.startswith(("Die")) or sentence.startswith(("Das"))]
    return article_sentences



def filter_april(sentences):
    april_sentences = [sentence.strip() for sentence in sentences if "April" in sentence]
    return april_sentences

file_path = 'wiki.txt'
file_content = read_file(file_path)

if file_content is not None:
    sentences = file_content.split('.')

#Filterung kurze Sätze
    short_sentences = filter_short_sentences(sentences)

#Artikelfilter
    article_sentences = filter_articles(sentences)

#April,April
    april_sentences = filter_april(sentences)
# Hier wird dann alles in Dateien geschrieben
    with open('short.txt', 'w', encoding='utf-8') as short_file:
        short_file.write('\n'.join(short_sentences))

    with open('articles.txt', 'w', encoding='utf-8') as articles_file:
        articles_file.write('\n'.join(article_sentences))

    with open('april.txt', 'w', encoding='utf-8') as april_file:
        april_file.write('\n'.join(april_sentences))

    print("Die Dateien wurden erfolgreich erstellt.")

    # Ausgabe für Überprüfung
    #print("\nGefundene kurze Sätze:", short_sentences) <-- Klappt
    print("\nGefundene Sätze mit Artikeln:", article_sentences)
    #print("\nGefundene Sätze mit 'April':", april_sentences) <-- Klappt nicht
