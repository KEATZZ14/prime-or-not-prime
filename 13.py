number = int(input("Enter any number: "))
if ((number==2)||(number==3)||((number+1)%6==0)||((number-1)%6==0)):
    print(number, "yes")
 else:
    print(number, "no")
