def number_of_words(text):
    list_of_punctuation_marks = [',', '.', ';', ' ', ':', ' ', '...', ' ', '(', ' ', ')', ' ', "'", ' ', '"', ' ']
    new_list = []
    for char in text:
        if char in list_of_punctuation_marks:
            text = text.replace(char, ' ')

    list_text = text.split()

    for word in list_text:
        if word not in new_list:
            new_list.append(word)

    return len(new_list)

text_of_the_task = '''Во входной строке записан текст. Словом считается последовательность непробельных символов 
                            идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.
                             Определите, сколько различных слов содержится в этом тексте.'''
print(number_of_words(text_of_the_task))
