num=int(input("Enter a number:"))
t=num
numlen=0
while t>0 :
    numlen=numlen+1
    t=int(t/10)
if numlen>=4:
    numlen=int(numlen/2)
    check=0
    while num>0 :
        rem=num%10
        if check==numlen:
            mid1=rem
        elif check==(numlen-1):
            mid2=rem
        num=int(num/10)
        check=check+1
    product=mid1*mid2
    print("The Products Of Mid Digits Are:",product)
else:
    print("It is not a four or more than 4 digit number")
        
