
def filter_sentences():
    """
    Function to filter sentences from the file 'wiki.txt' and produce three output files based on the filtering criteria.
 
    The function reads in the file 'wiki.txt' and filters the sentences based on the following criteria:
    1. Sentences with less than 30 characters are saved in the file 'short.txt'.
    2. Sentences starting with "Der", "Die", or "Das" are saved in the file 'articles.txt'.
    3. Sentences containing the string "April" are saved in the file 'april.txt'.
 
    Raises:
    - FileNotFoundError:
        If the file 'wiki.txt' is not found in the current directory.
 
    Returns:
    - None
    """
 
    # Read the contents of the file 'wiki.txt'
    try:
        with open('wiki.txt', 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print("File 'wiki.txt' not found.")
        return
 
    # Split the content into sentences based on period ('.') as the delimiter
    sentences = content.split('\n')
 
    # Filter sentences based on the criteria and save them in separate files
    short_sentences = [sentence for sentence in sentences if len(sentence.strip()) < 30]
    articles_sentences = [sentence for sentence in sentences if sentence.strip().startswith(('Der ', 'Die ', 'Das '))]
    april_sentences = [sentence for sentence in sentences if 'April' in sentence]
 
    # Save the filtered sentences in separate files
    with open('short.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(short_sentences))
 
    with open('articles.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(articles_sentences))
 
    with open('april.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(april_sentences))
 
# Call the function to filter sentences and create the output files
filter_sentences()