#####################################################First Work Session#####################################################
#Project Euler Problem 1
a=0
for b in range(1,100):
    if b%5==0 or b%3==0:
        a+=b
#The above for loop adds every multiple of 3 and 5 to the answer
print(a)

#Project Euler Problem 2
b=1
temp=1
a=0
while b<4000000:
    temp1=b+temp
    temp=b
    b=temp1
    print(b)
    if b%2==0 and b<4000000:
        a+=b
#The above while loop calculates every element of the fibonacci sequence below 4 million and adds them to answer if they are even
print(a)

#####################################################Second Work Session#####################################################
#Project Euler Problem 3
pf=0
t=600851475143
def prime(n):
    for i in range(2,1000000):
        if n%i==0:
            return i
#This function returns the smallest prime factor of a number
while t!=1:
    if(prime(t)>pf):
        pf=prime(t)
    t=t/prime(t)
#This while loop returns the biggest prime factor of 600851475143 by comparing all of its prime factors
print(pf)

#Project Euler Problem 4
ans=0
for a in range(100,999):
    for b in range(100,999):
        t=a*b
        temp=t
        a1=t%10
        t=t/10
        a2=t%10
        t=t/10
        a3=t%10
        t=t/10
        a4=t%10
        t=t/10
        a5=t%10
        t=t/10
        a6=t%10
        t=t/10
#The above code calculates the digits of the product of every possible pair of 3-digit numbers
        if temp>99999:
            if a1==a6 and a2==a5 and a3==a4:
                if temp>ans:
                    ans=temp
        else:
            if a1==a5 and a2==a4:
                if temp>ans:
                    ans=temp
#The above code first determines if the product of two 3-digit numbers is 5-digit or 6-digit, and then determines if it is a palindrome number. If it is and it is greater than our previous answer, it becomes the new answer
print(ans)

#####################################################Third Work Session#####################################################
#Project Euler Problem 5
#The smallest common multiple of numbers from 1 to 20 can be found by multiplying the largest power of every prime numbers less than 20 that is a factor of one of the numbers in the range 1 to 20
#The greatest power of 2 that is a factor of a number between 1 to 20 is 4: 16=2^4
#The greatest power of 3 that is a factor of a number between 1 to 20 is 2: 9=3^2 18=2*3^2
#The greatest power of 5 that is a factor of a number between 1 to 20 is 1: 5=5^1 10=5^1*2 15=5^1*3 20=5^1*2^2
#The greatest power of 7 that is a factor of a number between 1 to 20 is 1: 7=7^1 14=7^1*2
#The greatest power of 11 that is a factor of a number between 1 to 20 is 1: 11=11^1
#The greatest power of 13 that is a factor of a number between 1 to 20 is 1: 13=13^1
#The greatest power of 17 that is a factor of a number between 1 to 20 is 4: 17=17^1
#The greatest power of 19 that is a factor of a number between 1 to 20 is 4: 19=19^1
#Thus, the smallest common multiple of numbers from 1 to 20 is 2^4*3^2*5*7*11*13*17*19

a=(2**4)*(3**2)*5*7*11*13*17*19
print(a)

#Project Euler Problem 6
squaresum=0
sumsquare=0
sum=0
for i in range(1,100):
    squaresum+=i**2
    sum+=i
#The for loop calculates the sum of the square of the numbers and also the sum of the number
sumsquare=i**2
ans=abs(sumsquare-squaresum)
#After calculating the sum of the square and the square of the sum, we calculate their difference using absolute value
print(ans)

#####################################################Fourth Work Session#####################################################
#Project Euler Problem 7
count=1
prime=[2]
a=3
while count!=10001:
    temp=0
    for i in prime:
        #if a divides any prime numbers smaller than a, it is not a prime number
        if a%i==0:
            temp=1
    if temp==0:
        prime.append(a)
        count+=1
        #if a is a prime, we add it to the prime list and add 1 to count
    a+=2
        #each time we add 2 to a because a prime number greater than 2 can only be odd, so we don't need to consider even numbers
a=a-2
#After the while loop, a is 2 greater than the 10001st prime number, so we subtract it by 2
print(a)

#####################################################Fifth Work Session#####################################################
#Project Euler Problem 8
a=7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
b=str(a)
zeroes=[]
temp=0
ans=0
for i in range(0,999):
    if b[i]=='0':
        zeroes.append(i)
#The above for loop locates the position of 0s
for i in zeroes:
    temp1=temp
    temp=int(i)
    while temp1+13<temp:
        temp2=int(b[temp+13])*int(b[temp+1])*int(b[temp+2])*int(b[temp+3])*int(b[temp+4])*int(b[temp+5])*int(b[temp+6])*int(b[temp+7])*int(b[temp+8])*int(b[temp+9])*int(b[temp+10])*int(b[temp+11])*int(b[temp+12])
        if temp2>ans:
            ans=temp2
#We find all possible sets of 13 adjacent numbers between each 0s and find the biggest product
print(ans)

