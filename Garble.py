from random import randint

def garble(text):
    newWord = ""
    result = []
    last_index = []
    for word in text.split():
        for i in range(len(word)):
            index = randint(0,len(word ) - 1)
            while index in last_index:
                index = randint(0,len(word ) - 1)              
            newWord += word[index]
            last_index.append(index)
        result.append(newWord)
        newWord = ""
        #print(last_index)
        last_index = []
    return ' '.join(result)

while True:
    print(garble(input("Palabra a liar: ")))
