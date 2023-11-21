import io

def process_sentences(input_filename, output_short_filename, output_articles_filename, output_april_filename):
    with io.open(input_filename, 'r', encoding='utf-8') as file:
        sentences = [line.strip() for line in file]

    write_file = lambda filename, content: io.open(filename, 'w', encoding='utf-8').write('\n'.join(content))

    write_file(output_short_filename, [sentence for sentence in sentences if len(sentence) < 30])
    write_file(output_articles_filename, [sentence for sentence in sentences if sentence.startswith(('Der', 'Die', 'Das'))])
    write_file(output_april_filename, [sentence for sentence in sentences if 'April' in sentence])

if __name__ == "__main__":
    process_sentences('wiki.txt', 'short.txt', 'articles.txt', 'april.txt')
