# Mijn programma over hoe je Fibonacci reeks maakt in Python :)

hvl = int(input("Hoeveel getallen wilt u zien? : "))

n1, n2 = 0, 1
getal = 0

if hvl <= 0:
    print("Typ een geldig getal alstublieft.")
elif hvl == 1:
    print("Fibbonacci reeks gaat tot", hvl, ":")
    print(n1)
else:
    print("Fibbonacci reeks")
    while getal < hvl:
        print(n1)
        a1 = n1 + n2
        n1 = n2
        n2 = a1
        getal += 1