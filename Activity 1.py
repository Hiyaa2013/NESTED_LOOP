string=input("please enter your word: ")
char=input("please enter your chracter: ")
i=0
count=0
while i<len(string):
    if(string[i]==char):
        count+=1
    i=i+1
print("TOTAL NUMBER OF TIMES ",char,"has occured =",count)
