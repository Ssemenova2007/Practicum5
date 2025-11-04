first=int(input())
second=int(input())
third=int(input())
if first==second==third:
    print(3)
elif (first==second and first!=second) or (first==third and first!=second) or (second==third and second!=first):
    print(2)
else:
    print(0)