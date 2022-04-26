# Basic - Print all integers from 0 to 150.
for x in range(0, 151, 1):
    print(x)

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for x in range(5,1001):
    if(x%5==0):
        print(x)
    continue

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for x in range(1,101):
    if(x%10==0):
        print("CodingDojo")
    elif x%5==0:
        print("Coding")

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum=0
for x in range(0,500000):
    if(x%2==1):
        sum=sum+x
    else:
        sum=sum+0
print(sum)

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
countdown=2018
while countdown > 0:
    print(countdown)
    countdown=countdown - 4

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum=1
highNum=20
mult=2
for x in range(lowNum, highNum, mult):
    print(x+1)