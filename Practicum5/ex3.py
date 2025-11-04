num=int(input())
a=num//1000
b=(num-a*1000)//100
c=(num%100)//10
d=(num%10)
num_reversed=d*1000+c*100+b*10+a
if num==num_reversed:
    print("настоящее")
else:
    print("кривое")