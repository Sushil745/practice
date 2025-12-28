#Temperature convert and advive
celscius=float(input("enter the value of celscius: "))
Fahren=celscius*(9/5)+32
if Fahren<0:
    print("very cold! Wear thick jacket: ",Fahren)
elif 0<=Fahren<=15:
    print("cold.Wear jacket:",Fahren)
elif 16<=Fahren<=25:
    print("Nice Weather:",Fahren)
else:
    print("Hot! Stay hydrated:",Fahren)
    