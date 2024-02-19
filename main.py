class Kutuphane:

    def __init__(self):
        self.dosya = open("cook.txt","a+") 


    def listeleme(self):
         with open("cook.txt") as f:                                    # açılan dosyadan işlem olmadığından tekrar açıp kapanması sağlandı(SADECE BU FUNC İÇİN)
             for x in f.readlines():                                    # dosyadan verileri okuduk
                for y in (x.splitlines()):                              # verileri satır sayır ayırdık
                     self.indis=y.find(",")                             # ilk virgülü bulduk ki kitap adını yazdırmada kullanacağız
                     if self.indis != -1:                               # ilk virgül bulunduysa
                         indis1 = y.find(",", self.indis + 1)           # ikinci virgülün indisini bularak kitabın yazarına ulaşacağız
                     print(y[2:self.indis-1], ",", y[(self.indis + 3) :indis1-1]) # bulunan indisler sayesinde kitap adı ve kitap yazarını bulup yazdırdık


    def kitapEkle(self):
        #kullanıcıdan kitapla ilgili girişler alınır.
        self.kitap_adi = input("Kitap adını giriniz =")
        self.kitap_yazari = input("Kitap yazarını giriniz =")
        self.yayin_yili = input("Kitabın yayınlanma yılını giriniz =")
        self.sayfa_sayisi = input("Kitabın sayfa sayısını giriniz =")

        #kitap ile ilgili veriler bir liste olarak tutulur.
        self.kitap_list = [self.kitap_adi,self.kitap_yazari, self.yayin_yili, self.sayfa_sayisi]
        
        # veriler kaydedildikten sonra imlec ilk satıra getirilir ve veriler okunarak dosyaya yazdırma işlemi yapılır
        self.dosya.seek(0) 
        self.dosya.write(str(self.kitap_list) + "\n")

    

    def kitapSil(self):
                sil_adi = input("Silinmesini istediğin kitabı girin =")                       
                with open("cook.txt","r+") as f:                           # açılan dosyadan işlem olmadığından tekrar açıp kapanması sağlandı(SADECE BU FUNC İÇİN)
                  for x in f.readlines():                                  # dosyadan verileri okuduk
                    print("HATA")                                          # hatanın nerede olduğunu anlamak için bakıyorum. Dosyadan okuma sonrasını çalıştırmıyor.
                    for y in (x.splitlines()):                             
                         print("HATA")   
                         self.indis_Sil=y.find(sil_adi)                    # silinmesi istesen kitap adının başlangıç indisini bul                                                     
                         if self.indis_Sil != -1:                          # eğer silinmesi istenen kitap dosyada varsa
                             del y[:]                                      # remove yada pop bu y listinde kullanılamıyor o yüzden del kullanılarak tüm satır değerini sil
 
                           #del ile silinmezse replace ile o satırı boş bırakalım.
                           # self.dosya.write(y.replace(y[:],""))          
                         else:                                             # dosyada öyle bir kitap yoksa
                             print("Öyle bir kitap bulunmamaktadır")
        

    def __del__(self):
        print('dosya kapatıldı')
        self.dosya.close()

lib = Kutuphane()

print("***MENU ***")
print("1)Kitapları Listele")
print("2)Kitap Ekle")
print("3)Kitap Sil")
islem = input("Kaç numaralı İşlemi yapmak istiyorsunuz?")

if int(islem) == 1:
    lib.listeleme()
elif int(islem) == 2:
    lib.kitapEkle()
elif int(islem) == 3:
    lib.kitapSil()
else:
    print("Geçerli bir işlem yapmadınız, girdiğiniz numarayı kontrol ediniz")


