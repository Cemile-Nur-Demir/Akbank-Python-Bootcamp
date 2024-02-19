class Kutuphane:
    

    def __init__(self):
        self.dosya = open("book.txt","a+") 
        

    def listeleme(self):
         with open("book.txt") as f:                                    # açılan dosyadan işlem olmadığından tekrar açıp kapanması sağlandı(SADECE BU FUNC İÇİN)
             for x in f.readlines():                                    # dosyadan verileri okuduk
                for y in (x.splitlines()):                              # verileri satır sayır ayırdık
                     indis=y.find(",")                             # ilk virgülü bulduk ki kitap adını yazdırmada kullanacağız
                     if indis != -1:                               # ilk virgül bulunduysa
                         indis1 = y.find(",", indis + 1)           # ikinci virgülün indisini bularak kitabın yazarına ulaşacağız
                     print("Kitap:",y[2:indis-1], ",","Yazar:", y[(indis + 3) :indis1-1]) # bulunan indisler sayesinde kitap adı ve kitap yazarını bulup yazdırdık


    def kitapEkle(self):
        #kullanıcıdan kitapla ilgili girişler alınır.
        kitap_adi = input("Kitap adını giriniz =")
        kitap_yazari = input("Kitap yazarını giriniz =")
        yayin_yili = input("Kitabın yayınlanma yılını giriniz =")
        sayfa_sayisi = input("Kitabın sayfa sayısını giriniz =")

        #kitap ile ilgili veriler bir liste olarak tutulur.
        kitap_list = [kitap_adi,kitap_yazari, yayin_yili, sayfa_sayisi]
        
        # veriler kaydedildikten sonra imlec ilk satıra getirilir ve veriler okunarak dosyaya yazdırma işlemi yapılır
        self.dosya.seek(0) 
        self.dosya.writelines('\n'+ str(kitap_list) )

    

    def kitapSil(self):
                    sil_adi = input("Silinmesini istediğin kitabı girin =")   
                    self.dosya.seek(0)      

                    for y1 in self.dosya.read().splitlines():                  
                         self.dosya.truncate(0)                            
                         indis_virgul=y1.find(",")  
                         if (sil_adi==y1[2:indis_virgul-1]):                          # eğer silinmesi istenen kitap dosyada varsa
                             print("sildi")
                             indis_x =y1.find(",")                             # ilk virgülü bul
                             if indis_x != -1:                               # ilk virgül bulunduysa
                               indis_x1 = y1.find(",", indis_x + 1)           # ikinci virgül var mı ara
                               if indis_x1 != -1:                               #ikinci virgül varsa
                                     indis_x2=y1.find(",", indis_x1 +1 )        #üçüncü virgülü ara
                                     if indis_x2 != -1:                         #üçüncü virgül varsa 
                                        indis_son = y1.find("]")                # satır sonuna gelen indisi bul
                                        if indis_son != -1:
                                            continue
                                        else:
                                          self.dosya.write(y1)      
                              
                                        

                         
        

    def __del__(self):
        print('dosya kapatıldı')
        self.dosya.close()

lib = Kutuphane()
while True:
    print("***MENU ***")
    print("1)Kitapları Listele")
    print("2)Kitap Ekle")
    print("3)Kitap Sil")
    print("4) Çıkış")
    islem = input("Kaç numaralı İşlemi yapmak istiyorsunuz(1-4)) = ")
    
    if str(islem) =="q" or str(islem) == "Q":
         break
    elif int(islem) == 1:
        lib.listeleme()
    elif int(islem) == 2:
        lib.kitapEkle()
    elif int(islem) == 3:
        lib.kitapSil()
    else:
        print("Geçerli bir işlem yapmadınız, girdiğiniz numarayı kontrol ediniz")


