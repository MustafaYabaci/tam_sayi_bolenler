def tambölenleribulma(sayı):
    tam_bölenler=[]
    for i in range(2,sayı):
        if(sayı % i ==0):
            tam_bölenler.append(i)
    return tam_bölenler
while True:
    sayı = input("sayı")
    if(sayı=="q"):
        print("programı sonlandır")
        break
    else:
        sayı=int(sayı)
        print("tam bölenler",tambölenleribulma(sayı))