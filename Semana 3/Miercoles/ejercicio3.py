words = input("Please enter words in this format <palabra>:<traducción> splitted by commas:")
words = words.split(",")
dictionary = {}
for word_and_translate in words:
    word_list = word_and_translate.split(":")
    print(word_list)
    key = word_list[0]
    value = word_list[1]
    dictionary[key] = value
    print(dictionary)

phrase = input("Please enter a phrase to translate: ")
phrase = phrase.split()
for word in phrase:
    print(dictionary.get(word,word), end=" ")
#[<palabra>:<traducción>,<palabra>:<traducción>,<palabra>:<traducción>,<palabra>:<traducción>,<palabra>:<traducción>]
