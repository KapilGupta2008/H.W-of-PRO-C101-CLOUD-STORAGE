def a():
    b=input("enter the file name: ")
    numberofwards=0
    file=open(b,'r')
    for i in file:
        word=i.split()
        numberofwards=numberofwards+len(word)
    print("number of words are: ")
    print(numberofwards)

a()