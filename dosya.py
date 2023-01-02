while True:
    print("--------------------------------------------------------------------------------------")
    print("1-Dosya Oluşturma (Oluşturma, zaten bir dosya varsa hata verir.)")
    print("2-Dosya Yazma (Dosyayı yazmak için açar, dosya yoksa yeni bir tane oluşturur.)")
    print("3-Dosya Ekleme(Dosyayı veri eklemek için açar, dosya yoksa yeni bir tane oluşturur.)")
    print("4-Dosya Okuma (Varsayılan değerdir, dosyayı okumak için açar. Dosya yoksa hata verir.)")
    print("--------------------------------------------------------------------------------------")
    secim = int(input("Lütfen Yapmak İstediğiniz İşlemi Seçiniz: "))


    if secim == 1 :
        if FileExistsError:
            continue
        else:
            dosya = open("dosya.txt" , "x")

    if secim == 2 :
        dosya = open("dosya.txt" , "w")
        dosya.write("Selam")
    
    if secim == 3 :
        dosya = open("dosya.txt" , "a")
    
    if secim == 4 :
        dosya = open("dosya.txt" , "r")
    