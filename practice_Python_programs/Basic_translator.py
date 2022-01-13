#Giraffe translator : we have to find out vowels and convert that each vowels char into "g"

def translate(word):
    new_word = ""
    for i in word:
        if i in "AEIOUaeiou":  #i.lower() in "aeiou"
            if(i.isupper()):
                new_word += "G"
            else:
                new_word += "g"
        else:
            new_word += i
    return new_word

print(translate(input("Enter one word: ")))