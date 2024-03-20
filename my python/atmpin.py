
pin = 2000

inputpin =  int(input("enter your pin:"))

while(inputpin !=pin):
    print("wrong number, try again")
    inputpin= int( input())
print("your balance is $500")    

# make sure to convert the input to int becos a string can not compare a int 
