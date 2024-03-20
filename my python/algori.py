
pin = 2000
baln = 500000
numberoftries =3

inputpin =  input("enter your pin:")
while (numberoftries > 0):
    if(not inputpin.isdigit()):
        print("invalid input, enter valid PIN number")
        break


    if(pin == int(inputpin)):
        print("your balance is "+ str (baln))
        break
    else:
        numberoftries -=1
        if(numberoftries == 0):
            break
        inputpin = input("incorrect PIN:try again ") 
    