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
