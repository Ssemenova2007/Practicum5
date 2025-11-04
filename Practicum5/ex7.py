N=int(input())
K=int(input())
M=int(input())
if K>M:
    straight = abs(K-M-1)
    reverse=(N-K+M-1)
else:
    straight = abs(M-K-1)
    reverse=(N-M+K-1)
if straight>reverse:
    print(reverse)
else:
    print(straight)