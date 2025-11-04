N=int(input())
g=N//(17*29)
s=(N%(17*29))//29
k=N%(17*29)-29*s
if g>0 and s>0 and k<=0:
    print(f"{g} галлеонов")
    print(f"{s} сиклей")
elif g>0 and s<=0 and k<=0:
    print(f"{g} галлеонов")
elif g<=0 and s>0 and k>0:
    print(f"{s} сиклей")
    print(f"{k} кнатов")
elif g<=0 and s>0 and k<=0:
    print(f"{s} сиклей")
elif g>0 and s<=0 and k>0:
    print(f"{g} галлеонов")
    print(f"{k} кнатов")
elif g<=0 and s<=0 and k>0:
    print(f"{k} кнатов")
else:
    print(f"{g} галлеонов")
    print(f"{s} сиклей")
    print(f"{k} кнатов")
