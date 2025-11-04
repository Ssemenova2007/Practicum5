PIN=input()
if (len(str(PIN))==4) and (len(set(PIN))==4) and (int(PIN)<1950 or int(PIN)>2050):
    print("OK")
else:
    print("ERROR")