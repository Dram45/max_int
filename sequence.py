#Ask for how many numbers user wants

#Run a loop that adds together the numbers wanted

#set control numbers
#control number1 is 1
#control number2 is 0
#control number3 is 0
#while generated number is less than asked print numbers run the loop
    #generate number starting from 1
    #number generated is sum of the last three numbers in the sequence
    #print out sum of control numbers
    
    #change control number2 to 1
    #change control number3 to 1
    #change control number1 to 0

#when loop runs again control numbers should change based on the time of the loop

n = int(input("Enter the length of the sequence: ")) # Do not change this line

initalnumber = 1
controlnumber2 = 0
controlnumber3 = 0

sum = initialnumber + controlnumber2 + controlnumber3

for x in range(0,n):
    print(sum)
    sum = initialnumber 

