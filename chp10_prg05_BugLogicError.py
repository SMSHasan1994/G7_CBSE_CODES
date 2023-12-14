#Bug (error) in a program - Logic error

num1 = 50
num2 = 25

if num1 > num2:
    print("num2:",num2,"is bigger than num1:",num1) #Logic error
else:    
    print("num1:",num1,"is bigger than num2:",num2) #Logic error

#As per the comparison symbols used in the conditional statement
#The print statment should say num1 is bigger, but the program says num2 is bigger
#Here the program will run successfully but the output will be logically worng.
    
    
