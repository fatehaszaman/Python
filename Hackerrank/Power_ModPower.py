## You are given three integers: , , and . Print two lines.
## On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).
## Input Format
## The first line contains , the second line contains , and the third line contains 


# Enter your code here. Read input from STDIN. Print output to STDOUT
a= int(input())
b= int(input())
m= int(input())

if ((1<= a <= 10) and (1<= b<= 10) and (2<= m <= 1000)):
    print(pow(a,b))
    print(pow(a,b,m))
