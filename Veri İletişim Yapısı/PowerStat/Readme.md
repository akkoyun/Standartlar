# "PowerStat" Veri Paketi 

PowerStat projesine ait veri paketi bloğudur. Command alanında belirlenen komuta özel yapıda olacaktır. Ölçümlenen verilere ait paketler ve hangi komutta hangi veri setinin gönderileceği bilgisi [ilgili linkte](Commands.md) tanımlanmıştır.

```json
"Payload": {
	"TimeStamp": "2022-07-19 10:30:17",
	"PowerStat": {
		"DeviceStatus": 240,
		"FaultStatus": 500,
		"Temperature": 31.12024,
		"Humidity": 32.19268,
		"Pressure": {
			"Min": 5.294469,
			"Max": 5.303883,
			"Avg": 5.29606,
			"Inst": 5.296359,
			"Slope": 0.000031,
			"Offset": 5.265226,
			"R2": 0.057676,
			"DataCount": 26
		},
		"Energy": {
			"Voltage": [230.9336, 229.8274, 230.3372],
			"Current": [0.000667, 0.000799, 0.000763],
			"PowerFactor": 0.116505,
			"Consumption": [0, 0],
			"Frequency": 49.99597
		},
        "Fault": [true, true, true, false, true, true, true, true, false, true, true]
	}
}
```

***

## "DeviceStatus" Pompa Durum Bilgisi

PowerStat cihazı bir motora (pompaya) ait çalışma bilgileri analiz etmektedir. Bu nedenle pompanın ve sistemin durumunu belirten bir kod oluşturulmuştur. DeviceStatus kodu pompanın çalışıp çalışmadığı veya sistemin online offline durumunu tanımlayan bir koddur. Aşağıdaki değerleri alabilir.

| Device Status Code | Pompa Durumu     | Sistem Bağlantısı                           |
|--------------------|------------------|---------------------------------------------|
| 400                | Pompa Çalışmıyor | Sistem İnternete Bağlı Değil (Elektrik yok) |
| 240                | Pompa Çalışmıyor | Sistem İnternete Bağlı (Elektrik var)       |
| 220                | Pompa Çalışıyor  | Sistem İnternete Bağlı (Elektrik var)       |

### DeviceStatus : 400

PowerStat sistemi üzerinde bulundurduğu 220V girdi kontrolleri ile sistem elektrik yapısını anlık olarak takip eder. Bu girdilerden ilk üçü R,S,T fazlarıdır. Sistem üzerinde elektrik beslemesi olmadığı durumda PowerStat cihazı bağlantıyı kesip güç koruma moduna girer. Bu nedenle cihaz internet bağlantısı yoktur ve hiçbir aktivite bulunmadan sadece elektrik (besleme) gelmesin bekler. Besleme geldiği an otomatik olarak internete bağlanır ve 240 yada 220 durumuna geçer.

### DeviceStatus : 240

Sistem elektrik girdileri ile kontrol edilen yapıda besleme olması durumunda sistem otomatik olarak 400 durumundan çıkar ve GSM üzerinden internete bağlanarak online olur. Bu esnada diğer girdi uçlarından olan M1,M2,M3 (kontaktör durum girdileri) taranarak kontaktörlerin aktif olup olmadığı analiz edilir. Bu analiz sonucunda kontaktörler pasif ise yani pompa çalışmıyor ise sistem otomatik olarak 240 durumuna geçer.

### DeviceStatus : 220 

Kontaktör durumları yıldız yada üçgen durumuna geçtiği an yani pompa çalıştırılmaya başladığı an sistem otomatik olarak bunu algılar ve sistemi çalışıyor koduna yani 220 durumuna geçer.

***

## "FaultStatus" Arıza Durum Bilgisi

Sistem üzerinde bulunan girdiler ve bu girdileri analiz eden deeplearning algoritması ile sistem üzerinde oluşulabilecek her türlü hata anlık olarak takip edilir. Bu hata durumları bir kod ile ifade edilir ve bu hata kodları üzerinden önceden tanımlanmış işlemler gerçekleştirilir. Bu hata algoritmasında hangi kontrollerin yapılıp yapılmayacağı kullanıcı tarafından seçilebilir (Fault).

| Fault Status Code | Arıza Tanımı                 |
|-------------------|------------------------------|
| 50x               | Durum Hataları               |
| 501               | Faz Kaybı (S veya T yok)     |
| 502               | Enerji Yok (Tüm fazlar yok)  |
| 503               | Faz Kaybı (R fazı yok)       |
| 504               | Termik Röle Arızası          |
| 505               | Motor Koruma Rölesi Arızası  |
| 506               | Kontaktör Anomalisi          |
| 51x               | Enerji Hataları              |
| 511               | Düşük Voltaj                 |
| 512               | Yüksek Voltaj                |
| 513               | Düşük Frekans                |
| 514               | Yüksek Frekans               |
| 515               | Düşük Cos Fi                 |
| 516               | Voltaj Dengesizliği          |
| 517               | Akım Dengesizliği            |

### 50x : Durum Kodları

Sistem elektrik aksamlarından oluşabilecek arıza tiplerini tanımlar. 

#### 501 : Faz Kaybı

Sistem üzerinde bulunan R,S,T fazlarından R fazı var fakat S veya T fazından en az birisi yok.

#### 502 : Enerji Yok

Sistem üzerinde bulunan tüm fazların (R,S,T) olmaması yani elektrik olmaması durumudur.

#### 503 : Besleme Fazı Kaybı

PowerStat sistemi ve diğer tüm elektrikli aksam için besleme voltajı olan R fazının olmaması durumudur.

#### 504 : Termik Röle Arızası

Sistem üzerinde bulunan termik koruma rölesinin (sürekli yüksek akım çekmesi durumunda devreye girer) sistemi korumaya alması durumudur.

#### 505 : Motor Koruma Rölesi Arızası

Eski sistem panolarda faz kaybını önlemek için kullanılan motor koruma rölesinin (çoğu durumda baypas edilir) sistemi korumaya alması durumudur.

#### 506 : Kontaktör Anomalisi

Sistem üzerinde bulunan 3 kontaktör sırası ile M1, M2 ve M3 olarak isimlendirilir. Bu kontaktörler pompa çalışmaya başladığı zaman M1 ve M3 çekerek sistemi yıldız yolvermede çalıştırır. Belirlenen süre sonunda M3 kontaktörü bırakarak M2 kontaktörü çeker ve sistem üçgen yolvermede çalışmaya başlar. Bu sıralamanın bozulması durumunda oluşan durumdur.

### 51x : Elektriksel (şebeke) Hataları

Sistemin bağlı olduğu şebekeden kaynaklanan elektriksel parametre limitlerinin dışarısına çıkması durumunda oluşan arıza tiplerini tanımlar.

#### 511 : Düşük Voltaj

Sistem anma voltajı 230V dur. Bu voltaj seviyesinin %15 altı düşük voltaj seviyesidir. 

#### 512 : Yüksek Voltaj

Sistem anma voltajı 230V dur. Bu voltaj seviyesinin %10 üstü yüksek voltaj seviyesidir. 

#### 513 : Düşük Frekans

Sistem anma frekansı 50Hz dir. Bu frekans seviyesinin %6 altı düşük frekans seviyesidir.

#### 514 : Yüksek Frekans

Sistem anma frekansı 50Hz dir. Bu frekans seviyesinin %4 üstü yüksek frekans seviyesidir.

#### 515 : Düşük Güç Katsayısı

Sisteme tanımlanan güç katsayısının altına düştüğü zaman oluşan hata kodudur.

#### 516 : Voltaj Dengesizliği

3 Fazlı sistemlerde fazlar arası en fazla %6 dengesizlik olması beklenir. Bu dengesizliğin üstü voltaj dengesizliğidir. Voltaj dengesizliği şebeke temelli olabileceği gibi OG sigortalarında veya trafoda oluşan sorunlarda da oluşur.

#### 517 : Akım Dengesizliği

3 Fazlı sistemlerde akımlar arası en fazla %6 dengesizlik olması beklenir. Bu dengesizliğin üstü akım dengesizliğidir. Akım dengesizliği pompa vs gibi ekipmanların dengesiz yük çekmesi gibi durumlarda oluşur.

***

### "Temperature" : PCB (kutu içi) Sıcaklığı Verisi

|                 | Açıklama       |
|-----------------|----------------|
| Değişken Adı    | Temperature    |
| Değişken Tanımı | PCB Sıcaklığı  |
| Değişken Tipi   | Float          |
| Değişlen Birimi | Derece         |
| Örnek Veri      | 22.22          |

Sistemin T (kutu içi / PCB sıcaklığı) sensörüne ait kalibre sıcaklık değeridir. Eğer sistemde donanımsal bir arıza mevcut ise bu veri tipi -1xx olarak gönderilmektedir. Bu veri tipleri daha sonra tanımlanacaktır.

***

### "Humidity" : PCB (kutu içi) Bağıl Nem Verisi

|                 | Açıklama       |
|-----------------|----------------|
| Değişken Adı    | Humidity       |
| Değişken Tanımı | PCB Bağıl Nem  |
| Değişken Tipi   | Float          |
| Değişlen Birimi | %              |
| Örnek Veri      | 22.22          |

Sistemin H (kutu içi / PCB bağıl nem) sensörüne ait kalibre bağıl nem değeridir. Eğer sistemde donanımsal bir arıza mevcut ise bu veri tipi -1xx olarak gönderilmektedir. Bu veri tipleri daha sonra tanımlanacaktır.

***

### "Pressure" Sulama Basıncı Parametreleri

PowerStat cihazının önemli özelliklerinden birisi de sulama hattı üzerinde (pompa çıkışında) bulunan basınç sensörü üzerinden gelen veri ile sulama hattının basınç parametrelerini takip etmektir. Bu Parametreler her 3 sn de bir okunan bir dizi ile bunu analiz eden bir dizi istatistiksel algoritma sonucu çıktılardan oluşmaktadır. Bu veriler ile sulamanın durumu hat kopması vs durumlar tesbit edilebilmektedir.

	Ölçümlenen değerler ve istatistiksel seri her veri gönderiminde sıfırlanır.

#### "Inst" Anlık Basınç

Sistem tarafından her 3 sn de bir okunan basınç bilgisidir. Veri gönderim aralığı doğrultusunda tüm bu ölçümler bir dizi içerisinde toplanır. Veri paketinde göbderilen Inst verisi ise veri gönderimi yapıldığı sırada ölçülen basınç bilgisidir.

#### "DataCount" Ölçülen Veri Sayısı

Herbir veri gönderim aralığında ölçümlenen basınç değeri sayısıdır. Diğer bir değişle ölçüm dizisi büyüklüğüdür.

#### "Min" Minimum Basınç

Herbir veri gönderim aralığında ölçümlenen basınç değerlerinin en küçüğüdür.

#### "Max" Maksimum Basınç

Herbir veri gönderim aralığında ölçümlenen basınç değerlerinin en büyüğüdür.

#### "Avg" Ortalama Basınç

Herbir veri gönderim aralığında ölçümlenen basınç değerlerinin ortalamsıdır.

#### "Slope" Regresyon Eğimi

Ölçümlenen basınç dizisine ait son 20 veri üzerinden hesaplanan regresyon algoritması ile belirlenen eğim verisidir. Hat kopması veya tıkanması durumunda % olarak eğim artar.

#### "Offset" Regresyon Ofset Değeri

Ölçümlenen basınç dizisine ait son 20 veri üzerinden hesaplanan regresyon algoritması ile belirlenen ofset verisidir.

#### "R2" Regresyon Doğruluk Değeri

Hesaplanan regresyona ait R2 değeri yani doğruluk değeridir. % olarak doğruluğu verir.

***

### "Enerji" Şebeke ve Elektriksel Parametreler

PowerStat cihazının önemli özelliklerinden birisi de anlık olarak ölçümlenen enerji parametrlerini analiz etmesidir. Analiz edilen bu parametreler ile ilgili bölümde tanımlanan hata kod parametreleri tesbit edilir.

#### "Voltage" Şebeke Voltaj Verileri

Şebeke voltaj ölçümlerine (anlık) ait dizi verisidir. R,S,T sırası ile son yapılan ölçümleri içerir.

#### "Current" Akım Verileri

Sisteme ait (pano içerisinde bulunan) akım trafoları (X/5) üzerinden okunan akım değerlerine ait dizi verisidir. R,S,T sırası ile son yapılan ölçümleri içerir. Akım trafosu katsayısı ile çarpılıp gerçek değer hesaplanır.

#### "PowerFactor" Sistem Güç Kat Sayısı Cos-Fi

Sistem akım ve voltaj ölçümleri ile aralarındaki faz farkları üzerinden hesaplanan güç katsayısı verisidir. Fazlar için cos-fi değeri ölçmek yerine ortalama sistem güç katsayısı gönderilmektedir.

#### "Consumption" Güç Tüketim Verileri

Sistem üzerinden ölçümlenen aktif ve reaktif güç verilerine ait dizidir. Aktif,Reaktif sıralaması ile gönderilmektedir. Veriler her gönderimde sıfırlanmaktadır.

#### "Frequency" Sistem Frekans Verisi

Şebeke üzeriden ölçümlenen frekans verisidir.

