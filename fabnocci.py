
number1=input("enter the first number  series : ")
number2=input("enter the second number series : ")

number_of_terms=input("enter the number of terms required : ")
print number1
print number2
while (number_of_terms!=0):
    num3=number1+number2
    number1=number2
    number2=num3
    number_of_terms=number_of_terms-1
    print num3

    
    
