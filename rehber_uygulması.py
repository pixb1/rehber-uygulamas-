rehber = dict()

def rehber_ekle(x):
    print("***Numara Ekleme Ekranına Hoşgeldiniz***")
    ekle = input("Adı Giriniz :")
    numara = input("Numara Gir :")
    rehber.setdefault(ekle,numara)
    print(f"{ekle} adlı kullanıcı eklendi...")

def rehber_gör(x):

    say = 1
    print("*"*30)
    for i,j in x.items():
        print(say,"-Kullanıcı =",i,":",j)
        say +=1
    print("*"*30)
def sil(x):
    soru = input("Kimi silmek İstersiniz ? :")
    rehber.pop(soru)

while True:
    seçim = input("1-Ekle\n2-Sil\n3-Gör\n")
    if seçim == "1":
        rehber_ekle(rehber)
    elif seçim == "2":
        sil(rehber)
    elif seçim == "3":
        rehber_gör(rehber)