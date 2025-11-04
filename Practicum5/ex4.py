num=int(input())
def parrots_number(num):
    if num%10==1 and num//10!=1:
        return "попугай"
    elif num%10>1 and num%10<5 and num%10!=1:
        return "попугая"
    else:
        return "попугаев"
print(f"{num} {parrots_number(num)}")
