weight=int(input('Enter your weight: '))
height=int(input('Enter your height: '))
weight_kg=weight*0.453592
height_m=height*0.0254
IMT=(weight_kg/(height_m**2))
ans=round(IMT,2)
if ans<16:
    print("выраженный дефицит массы тела")
elif ans>=16 and ans<18.49:
    print("недостаточная масса тела")
elif ans>=18.5 and ans<24.99:
    print("норма")
elif ans>=25 and ans<29.99:
    print("избыточная масса тела")
elif ans>=30 and ans<34.99:
    print("ожирение первой степени")
elif ans>=35 and ans<39.99:
    print("ожирение второй степени")
else:
    print("ожирение третьей стпени")
