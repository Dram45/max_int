#input a number 

#control number is 0

#if input number is negative break.

#compare input number to control number

#if input number is higher
#control number is equal to input number
#else control number stays the same

#at end of loop print out control number
num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
max_int = 0 #control number
#run loop aslong as number isn't negative
while num_int >= 0:
    if num_int > max_int:
        max_int = num_int
    num_int = int(input("Input a number: "))
        
#print out the largest number entered
print("The maximum is", max_int)    # Do not change this line
