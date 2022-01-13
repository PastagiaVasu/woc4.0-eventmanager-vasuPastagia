
# some string func
phrase = "My name is Khan"
print("Whole String in Lower Case: "+phrase.lower())
print("Whole String in Upper Case: "+phrase.upper())
print("check given sting is in upper case or not : "+phrase.isupper().__str__())
print("We can you more than one func at time : "+phrase.upper().isupper().__str__())
print("Length of string: "+len(phrase).__str__())
print("Disply first char: "+phrase[0])
print("Find index of given char: "+phrase.index("K").__str__()+"\n start postion of given string: "+phrase.index("name").__str__())
print("Replace string: "+phrase.replace("Khan","Vasu"))
print("Find out how many time this char or word appers in given string: "+phrase.count("a").__str__())