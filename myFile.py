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
