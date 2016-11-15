
palabra_prohibidas = ['puta','coño','hostia','imbécil','gilipollas','polla','subnormal','idiota','zorra','mierda']

def censor(text, word):
    result = []
    for wrd in text.split():
        if wrd == word: 
            result.append('*' * len(word))
        else:
            result.append(wrd)
    return " ".join(result)

def censor_lst(text, word_list):
    result = []
    for wrd in text.split():
        if wrd in word_list: 
            result.append('*' * len(wrd))
        else:
            result.append(wrd)
    return " ".join(result)
    
while True:
    text = input("Texto a corregir: ")
    word = input("Palabra prohibida: ")
    print(censor(text,word))
    print(censor_lst(text,palabra_prohibidas))
