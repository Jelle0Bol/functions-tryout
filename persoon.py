m = 1

while m < 2:
    naam = input("Wat is uw naam? : ")
    leeftijd = input("Hou oud bent u? : ")
    print("Hallo " ,naam , " je bent " , leeftijd ,  " jaar oud.")
    doorgaan = input("Wil je doorgaan? : ")
    if doorgaan == "ja":
        m + 0
    elif doorgaan == "nee":
        m + 1
        break
    else:
        print("Gebruik alleen ja of nee.")
