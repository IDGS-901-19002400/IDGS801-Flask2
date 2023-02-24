def addTranslation(spanishWord, englishWord):
    with open('translations.txt', 'a') as file:
        file.write(f"{spanishWord} {englishWord}\n")

def getTranslation(text, language):
    with open('translations.txt', 'r') as file:
        words = file.read().splitlines()
        if language == 'english':
            word = [word.split(' ')[1] for word in words if word.split(' ')[0].lower() == text.lower()]
        else:
            word = [word.split(' ')[0] for word in words if word.split(' ')[1].lower() == text.lower()]

        if len(word) > 0:
            return word[0];
        else:
            return ''
