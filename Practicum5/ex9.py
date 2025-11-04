first,second,third=map(int, input().split())
if first>second and second>third:
    print(first,second,third)
elif first>third and third>second:
    print(first,third,second)
elif second>first and first>third:
    print(second,first,third)
elif second>third and third>first:
    print(second,third,first)
elif third>first and first>second:
    print(third,first,second)
else:
    print(third,second,first)