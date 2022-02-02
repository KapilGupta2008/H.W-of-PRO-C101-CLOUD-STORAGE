a=input("enter string:")
wordcount=1
charactercount=0
for i in a:
    charactercount=charactercount+1
    if(i==' '):
        wordcount=wordcount+1
print("numbers of characters in a string : ")
print(charactercount)
print("numbers of words in a string : ")
print(wordcount)