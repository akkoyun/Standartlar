## Kodlama Yapısı (01.03.00)

Geliştirilmekte olan tüm projelerde kullanılan (müşteri bağımsız) tüm modüllere ve projelere ait bir kod sistematiği zorunlu hale gelmiştir. Bu kod sistemi aşağıda detayları anlatıldığı şekilde oluşturulmuştur. Sadece PCB ler değil üründen komponentlere kadar tüm sistem kodlanabilecektir.

Kodlama yapısı aşağıdaki formatta kullanılmaktadır.

</br>
<center><H3>ABbbCD-(Eeeeee)-(Fff)-(G)</H3></center>
</br>

***

<center>
| Kod     | Açıklama                  | Detay |
|:-------:|---------------------------|-------|
| A       | Segment Kodu              | [Açıklama](#) |
| B       | Grup Kodu                 | [Açıklama](#) |
| bb      | Sıra Kodu                 | [Açıklama](#) |
| CD      | Versiyon Kodu             | [Açıklama](#) |
| Eeeeee  | Üretim Parti ve Sıra Kodu | [Açıklama](#) |
| Fff     | Parça Kodu                | [Açıklama](#) |
| G       | Özel Üretim Kodu          | [Açıklama](#) |
</center>

#### Kod kullanım şekilleri.

Kodlar kullanım yerine göre değişiklikler göstermektedir.

| Kullanım Yeri | Açıklama | Örnek |
|:-------------:|----------|:-----:|
| Teknik Doküman | Her ne amaçla olursa olsun (elektronik, mekanik, üretim vb) teknik dokümanlarda (datasheet ürün açıklaması ve diğer yazılı kodümanlarda dahil) yer alan tüm kodlar **ABbbCD-(G)** formatında kullanılacaktır. | B101AA-PCIe |
| Errata Dokümanı | Modül üzerinde bulunan bir komponente dikkat çekilmesi gereken bir hata raporu üzerinde (her türlü dokümanda) **ABbbCD-(G)-Fff** formatında kullanılacaktır. | B101AA-PCIe-C27 |
| Pazarlama | Satış ve faturalama aşamasında her bir ürün (bireysel yada parti olarak) **ABbbCD-(G)-E(eeeee)** formatında kullanılacaktır. | B101AA-PCIe-A |
| Marketing | Özel bir odaklama durumu yok ise her türlü marketing materyalinde (basılı dijital görsel) **ABbb-(G)** formatında kullanılacaktır. | B101-PCIe |

---

### [A] : Segment kodu

**Segment Açıklaması :** [A] basamağı genel olarak segment grubunu temsil etmektedir. Aşağıdaki değerlerden birisini alabilir.

| Segment Kodu | Segment Tanımı | Segment Açıklaması |
|:------------:|:--------------:|:-------------------|
| P | **P**roduct | *Ürün segmentidir.* </br> Tanımlanmış bir amacı olan, çeşitli parçaların birleşimi oluşan bir ürün reçetesine tabi ürünlerin tamamı bu segment içerisinde yer almaktadır. Ürün kullanım hakları ve mülkiyeti müşteri ve/veya Ovoo ya ait olabilir. Ürün kullanım hakları devir sözleşmesi ile müşteriye devredilmemiş tüm ürünler Ovoo zimmetinde sayılmaktadır. Ürün içerisinde kullanılan modül, kablo, plastik veya metal ürünler yeni bir revizyona geçmesi durumunda ürün kodu da yeni bir revizyona geçmektedir. |
| B | **B**oard | *Elektronik modül segmentidir.* </br> Tasarımı (şematik ve PCB) Ovoo yapılmış tüm elektronik modüller bu segment içerisindedir. Modülün kullanım hakları kime ait olduğu önemsenmez. Modül kullanım hakları devir sözleşmesi ile müşteriye devredilmemiş tüm modüller Ovoo zimmetinde sayılmaktadır. |
| C | **C**asting | *Plastik enjeksiyon segmentidir.* </br> Tasarım ve mülkiyetleri üretici firmaya aittir. Ovoo kod sistematiğinde ürün reçetesi çıkartılması tasarımlarım projelendirilmesi vb. uygulamalar için kodlandırılmaktadır. Tekil olarak her bir plastik enjeksiyon üretimi yapılan (tekli yada çoklu kalıp kullanılması gözetmeksizin) tüm parçalar bu segment içersinde yer almaktadır. Bu segmente ait parçaların tasarım dosyaları Ovoo kütüphanesinde yer almayabilir (STL ve/veya Step dosyaları Ovoo kütüphanesinde yer almaktadır). |
| M | **M**etal | *Metal parça segmentidir.* </br> CNC, torna veya sac lazer kesim üretim teknikleri ile üretilen, hammaddesi demir, çelik, krom, bakır, alüminyum vb. maddelerden her türlü parça bu segmenttedir. Tasarım ve mülkiyeti tasarımcı firmaya (Ovoo ve/veya müşteri) aitdir. Ovoo kod sistematiğinde ürün reçetesi çıkartılması tasarımlarım projelendirilmesi vb. uygulamalar için kodlandırılmaktadır. Bu segmente ait parçaların tasarım dosyaları Ovoo kütüphanesinde yer almayabilir (STL ve/veya Step dosyaları Ovoo kütüphanesinde yer almaktadır). |
| H | **H**ardware | *Bağlantı parçaları segmentidir.* </br> Hammaddesi demir, çelik, krom, bakır, alüminyum, plastik, teflon vb. maddelerden üretilen her türlü vida, somun, ayraç, saplama vb elemanlar bu segmentte yer almaktadır. Ovoo kod sistematiğinde ürün reçetesi çıkartılması tasarımlarım projelendirilmesi vb. uygulamalar için kodlandırılmaktadır. Bu segmente ait parçaların tasarım dosyaları Ovoo kütüphanesinde yer almayabilir (STL ve/veya Step dosyaları Ovoo kütüphanesinde yer almaktadır). |
| W | **W**ire | *Kablo segmentidir.* </br> Kullanım amacına, üretim malzemesine ve konnektör yapısına bakılmaksızın modüller ve/veya cihazlar arası iletişim için kullanılan tüm cihaz içi/dışı bağlantı kabloları bu segment içerisinde yer almaktadır. Kablo kullanım hakları kime ait olduğu önemsenmez. Kablo kullanım hakları devir sözleşmesi ile müşteriye devredilmemiş tüm modüller Ovoo zimmetinde sayılmaktadır. |
| S | **S**ticker | *Etiket segmentidir.* </br> Kullanım amacına, üretim malzemesine ve ebatlarına bakılmaksızın, modül üzerine, kablo üzerinde, cihaz üzerinde veya kutu üzerinde yer alan her türlü bilgilendirici ve uyarıcı etiketler bu segment içerisinde yer almaktadır. Kullanım hakları kime ait olduğu önemsenmez. Kullanım hakları devir sözleşmesi ile müşteriye devredilmemiş tüm tasarımlar Ovoo zimmetinde sayılmaktadır. |
| E | **E**lectrical | *Elektrik Malzeme segmentidir.* </br> Kullanım amacına bakılmaksızın üretimi Ovoo tarafından yapılmayan ve cihazlar yada modüller üzerinde kullanılan tüm elektriksel malzemeler (batarya, switch, solar panel, Anten vb.) bu segment içerisinde yer almaktadır. Kullanım hakları kime ait olduğu önemsenmez. |

### [B] : Grup Kodu

[Bbb] basamağı genel olarak parçanın hangi gruba ait olduğunu belirtmektedir. B basamağı ana grup, bb basamağı ise grup içerisindeki sıra numarasını temsil etmektedir. Aşağıdaki değerleri ve ileride eklenecek değerleri alabilir.

#### P (Product) Segmenti Grup Kodları

| Ana Grup Kodu | Grup Tanımı | Grup Açıklaması |
|:-------------:|:-----------:|-----------------|
| P1xx | Meteoroloji | Kullanım yerine bakılmaksızın (dış mekan veya iç mekan) her türlü ortam koşulu parametresini (hava sıcaklığı, bağıl nem, hava basıncı, yağmur, rüzgar, toprak nemi, toprak sıcaklığı vb) ölçen ürün grubudur. |
| P2xx | Enerji | Kullanım yerine ve voltaj seviyesine bakılmaksızın her türlü enerji parametresini (voltaj, akım, güç, frekans vb.) ölçümleyen ürün grubudur. Endüstriyel amaçlı kullanılan enerji ölçüm ürünleri bu grup içerisinde yer almaktadır. |
| P3xx | Uzaktan Okuma | Okunacak parametre tipine bakılmaksızın her türlü uzaktan okuma / ölçümleme (ölçümü yapan cihazlara bağlanarak veri okuma) yapan ürün grubudur. |
| P4xx | Otomasyon | Kullanım yerine (endüstriyel yada tarımsal) bakılmaksızın her türlü kumanda işlevi yapan ürün grubudur. Tümleşik bir ürün olması durumunda (enerji vb. ölçümleme ve otomasyon birleşik ise) ürün bu grup içerisinde yer alacaktır. |
| P5xx | Endüstriyel | Kullanım yerine (endüstriyel yada tarımsal) bakılmaksızın. Müşteriye özel sunulan çözümler bu grup altında yer alacaktır. |
| P6xx | -- | -- |
| P7xx | Güvenlik | Kullanım yerine (endüstriyel yada tarımsal) bakılmaksızın. Güvenlik ana amacı ile üretilen tüm ürünler bu grup altında yer alacaktır. Güvenlik ihlallerini tesbit eden iot tabalı olan yada olmayan her çeşit güvenlik ihlali tesbiti yapan ürünlerdir. |
| P8xx | Programlama | Geliştirilen B1xx segmenti işlemci kartlarının programlanması (ICSP, JTAG vb) için kullanılacak olan bilgisayar bağlantılı ve/veya kendi başına çalışabilen cihaz grubudur.|
| P9xx | Test & Kontrol | Geliştirilen modül, kablo vb donanım için kullanılacak olan test, kontrol vb işlemleri gerçekleştirecek donanım grubudur. |
 
 
#### B (Board) Segmenti Grup Kodları

    Planlanma, tasarım, üretim gibi tamamen kendi üretimimiz olan her türlü 
    elektronik modül bu grup içerisinde yer almaktadır. Bu modüller için planlanmış.
    kategoriler aşağıda tanımlanmıştır.

| Ana Grup Kodu | Grup Tanımı | Grup Açıklaması |
|:-------------:|:-----------:|-----------------|
| B1xx | İşlemci Grubu | Üzerinde Mikro İşlemci veya IoT modülü olan tüm modüller bu grup içerisinde yer almaktadır. Modül üzerinde sadece işlemci veya sadece IoT modül olmaması grup içerisinde yer almaya engel bir özellik değildir. Genellikle işlemci, GSM modem ve SIM çip aynı kart üzerinde tasarlanarak bir bütün halinde sunulmaktadır.|
| B2xx | Ölçüm Grubu | Voltaj seviyesine bakılmaksızın her çeşit (elektrik, su, doğalgaz, kalori vb.) enerji ölçümlemesi yapan modüllerin tamamıdır. Sensör segmentinden farklı olarak ölçüm grubu ölçüm yapan cihazlara bağlanarak uzak cihaz üzerinde bulunan verinin okunmasını sağlayan dönüştürücü (üzerinde sensör bulundurmayan) modüllerdir. Muhtelif haberleşme kanalları üzerinden işlemci ile iletişim kurabilmektedir.|
| B3xx | Girdi Grubu | Voltaj seviyesine bakılmaksızın işlemciye veri sağlayan (sensörler hariç) tüm ADC ve/veya dijital modüller bu grup içerisinde yer almaktadır. Asıl amacı girdi olmayan ve üzerinde görsel çıktı elemanı bulunan modüller görsel çıktı grubu içerisinde değerlendirilecektir. Muhtelif haberleşme kanalları üzerinden işlemci ile iletişim kurabilmektedir. Bu grup ADC sensör ölçümlerini kapsamamaktadır.|
| B4xx | Çıktı Grubu | Voltaj seviyesine ve çıktı yöntemine bakılmaksızın işlemciden gönderilen verileri çıktı olarak verebilen tüm ürünler bu grup içerisinde yer almaktadır. Muhtelif haberleşme kanalları üzerinden işlemci ile iletişim kurabilmektedir. Röle veya SSR yanı sıra motor sürücü gibi fiziksel çıktı üreten modüller bu grup kapsamındadır.|
| B5xx | Sensör Grubu | Ölçülen verinin tipine ve ölçüm yöntemine bakılmaksızın (enerji grubu hariç) tüm sensör içeren ürünler bu grup içerisinde yer almaktadır. Muhtelif haberleşme kanalları üzerinden işlemci ile iletişim kurabilmektedir. Ayrıca sensör İletişim kanallarını (I2C, SPI vb) çoklayabilen multiplexer ve iletişim yöntemi dönüştürücü kartlar da bu grup içerisinde yer almaktadır. |
| B6xx | Güvenlik Grubu | Yöntemine bakılmaksızın güvenlik konusu ile alakalı olan tüm modüller (Seri ID çipi vb) bu grup içerisinde yer almaktadır. Muhtelif haberleşme kanalları üzerinden işlemci ile iletişim kurabilmektedir. |
| B7xx | Görsel Çıktı Grubu | Görüntüleme tipine (LCD, TFT, LED vs) bakılmaksızın görüntüleme kullanım için için özel olarak tasarlanmış olan tüm modüller bu grup içerisinde yer almaktadır. Modül üzerinde girdi birimleri (LED, encoder vb) olması bu grup içerisinde olmasına engel değildir. Asıl amacı girdi olan modüller üzerinde görsel çıktı elemanı bulunmasına rağmen girdi grubu içerisinde değerlendirilecektir. Muhtelif haberleşme kanalları üzerinden işlemci ile iletişim kurabilirler. |
| B8xx | Güç Kaynağı Grubu | Voltaj seviyesine ve yöntemine bakılmaksızın güç kaynağı amacı ile tasarlanmış olan tüm modüller bu grup içersinde yer almaktadır. Batarya kontrol, güç yönetim, buck-boost vb ayrık modüller bu gruba dahildir. Muhtelif haberleşme kanalları üzerinden işlemci ile iletişim kurabilirler. |
| B9xx | Ana Kart Grubu | Komponent içerip içermemesinden bağımsız olarak bir veya birkaç modülü birbirine bağlayan (kablo grubu hariç) tüm modüller bu grup içerisinde yer almaktadır. Modüller arası dönüştürücü adaptörler bu gruba dahildir. |

#### C (Casting) Segmenti Grup Kodları

    Planlanma, tasarım, üretim gibi tamamen kendi üretimimiz olan (müşteri mülkiyetli
    veya değil) her türlü plastik enjeksiyon ürünleri bu grup içerisinde yer almaktadır. 
    Bu modüller için planlanmış kategoriler aşağıda tanımlanmıştır.

| Ana Grup Kodu | Grup Tanımı | Grup Açıklaması |
|:-------------:|:-----------:|-----------------|
| C1xx | Meteoroloji Grubu | Tasarım ve mülkiyetleri üretici firmaya ait, meteoroloji segmentine ait (meteorolojik veri ölçümlerine ait toprak üstü cihazlarının) tüm plastik malzemeler bu grup içerisinde yer almaktadır. Tasarımlar ve kalıp kullanım hakları üretici firmaya aittir. |
| C2xx | Toprak Altı Grubu | Tasarım ve mülkiyetleri üretici firmaya ait, meteoroloji segmentine ait (meteorolojik veri ölçümlerine ait toprak altı cihazlarının) tüm plastik malzemeler bu grup içerisinde yer almaktadır. Tasarımlar ve kalıp kullanım hakları üretici firmaya aittir. |
| C3xx | Endüstriyel Grubu | Tasarım ve mülkiyetleri üretici firmaya ait, endüstriyel amaç için kullanılmakta olan (her türlü ölçüm, girdi, çıktı vb.) tüm plastik malzemeler bu grup içerisinde yer almaktadır. |
| C4xx | -- | -- |
| C5xx | -- | -- |
| C6xx | -- | -- |
| C7xx | -- | -- |
| C8xx | -- | -- |
| C9xx | Overmold       | Tasarımları yapılan her türlü modül, kablo vb. cihazların dış ortam yalıtımı (veya estetik) için gerçekleştirilen düşük basınç ve sıcaklık kullanılarak yapılan plastik kaplama yöntemi içeren tüm malzemeler bu grup içerisinde yer almaktadır. Tasarımlar ve kalıp kullanım hakları üretici firmaya aittir. |

#### M (Metal) Segmenti Grup Kodları

    Ürün geliştirme basamakları içerisinde yer alan ve montaj sırasında kullanılan
    ürün reçetesi içerisinde yer alan her türlü metal parça ürünleri bu grup
    içerisinde yer almaktadır. Bu modüller için planlanmış kategoriler 
    aşağıda tanımlanmıştır.

| Ana Grup Kodu | Grup Tanımı | Grup Açıklaması |
|:-------------:|:-----------:|-----------------|
| M1xx          | -- | -- |
| M2xx          | -- | -- |
| M3xx          | -- | -- |
| M4xx          | -- | -- |
| M5xx          | -- | -- |
| M6xx          | -- | -- |
| M7xx          | -- | -- |
| M8xx          | -- | -- |
| M9xx          | -- | -- |

#### H (Hardware) Segmenti Grup Kodları

    Ürün geliştirme basamakları içerisinde yer alan ve montaj sırasında kullanılan
    ürün reçetesi içerisinde yer alan her türlü bağlantı ürünleri bu grup içerisinde 
    yer almaktadır. 
    Bu modüller için planlanmış kategoriler aşağıda tanımlanmıştır.

| Ana Grup Kodu | Grup Tanımı | Grup Açıklaması |
|:-------------:|:-----------:|-----------------|
| H1xx          | Vida        | Ölçüsüne bakılmaksızın tüm Vida'lar bu grup içerisindedir. |
| H2xx          | Cıvata      | Ölçüsüne bakılmaksızın tüm Cıvata'lar bu grup içerisindedir. |
| H3xx          | Somun       | Ölçüsüne bakılmaksızın tüm Somun'lar bu grup içerisindedir. |
| H4xx          | Pul         | Ölçüsüne bakılmaksızın tüm Pul'lar bu grup içerisindedir. |
| H5xx          | Ayraç       | Ölçüsüne bakılmaksızın tüm Ayraç'lar bu grup içerisindedir.  |
| H6xx          | -- | -- |
| H7xx          | -- | -- |
| H8xx          | -- | -- |
| H9xx          | -- | -- |

#### W (Wire) Segmenti Grup Kodları

    Proje içerisinde kullanılacak olan her türlü elektrik iletim elemanları (kablo, 
    kablo ağacı vb) bu grup içerisinde yer almaktadır. 
    Bu modüller için planlanmış kategoriler aşağıda tanımlanmıştır.

| Ana Grup Kodu | Grup Tanımı | Grup Açıklaması |
|:-------------:|:-----------:|-----------------|
| W1xx          | Sinyal      | Voltaj seviyesine bakılmaksızın tüm sinyal iletişim kabloları bu grup içerisindedir. Sensör vb modüllerin çalışması için gerekli olan (sadece bağlı modül enerjisi için) güç iletim hatlarını içerebilir. |
| W2xx          | Güç         | Voltaj seviyesine bakılmaksızın tüm güç iletişim kabloları bu grup içerisindedir. Ana besleme hatları (batarya, adaptör vb.) gibi sadece güç hattı içeren kablolar. |
| W3xx          | RF          | RF iletişim tipine bakılmaksızın her türlü anten iletişim kabloları bu grup içerisindedir. |
| W4xx          | -- | -- |
| W5xx          | -- | -- |
| W6xx          | -- | -- |
| W7xx          | -- | -- |
| W8xx          | -- | -- |
| W9xx          | -- | -- |

#### S Segmenti Grup Kodları

    Proje içerisinde kullanılacak olan her türlü marketing elemanı (etiket, bilgi kartı
    broşür vb) bu grup içerisinde yer almaktadır. 
    Bu modüller için planlanmış kategoriler aşağıda tanımlanmıştır.

| Ana Grup Kodu | Grup Tanımı | Grup Açıklaması |
|:-------------:|:-----------:|-----------------|
| S1xx | Ürün Künyesi | Ürün özellikleri tanımlanan, ürüne ait tanımlayıcı seri numaralarının olduğu etikettir. |
| S2xx | QR Kod | Ürünü sisteme tanıtmak için kullanılan üretici firmaya has ürün QR kodu etiketidir. |
| S3xx | Marketing | Ürüne ait kullanım broşürü vb pazarlama dokümanlarının tamamı bu grup altında yer aşmaktadır. |
| S4xx | -- | -- |
| S5xx | -- | -- |
| S6xx | -- | -- |
| S7xx | -- | -- |
| S8xx | -- | -- |
| S9xx | -- | -- |

#### E Segmenti Grup Kodları

    Proje içerisinde kullanılacak olan üretimi iç kaynaklı yapılmayan her türlü
    elektrik malzemesi (switch, batarya vb) bu grup içerisinde yer almaktadır. 
    Bu modüller için planlanmış kategoriler aşağıda tanımlanmıştır.

| Ana Grup Kodu | Grup Tanımı | Grup Açıklaması |
|:-------------:|:-----------:|-----------------|
| E1xx | Batarya | Ürünler / modüller içerisinde kullanılan her türlü batarya (şarj edilebilir yada edilemez) voltaj seviyesine bakılmaksızın bu grup içerisinde yer almaktadır. |
| E2xx | Solar Panel | ürünler içerisinde kullanılan değişken ebat, voltaj veya güçte olan her tip solar panel bu grup içerisinde yer almaktadır. |
| E3xx | RF Anten | Ürünler içerisinde kullanılmakta olan her çeşit (çubuk, PCB, sticker vb) ve her frekanstaki antenler bu grup içerisinde yer almaktadır. |
| E4xx | Switch / Buton | ürün içerisinde kullanılan her türlü anahtarlama işlemi yapan elemanların tamamı bu grup içerisinde yer almaktadır. |
| E5xx | -- | -- |
| E6xx | -- | -- |
| E7xx | -- | -- |
| E8xx | -- | -- |
| E9xx | -- | -- |

---

### [b] Sıra Kodları (00-99)
Ürüne ait alt kod belirtilmesi amacı ile verilen sıra kod numarasıdır. Grup içerisinde alt grupları belirten ayrımlar bu alanda yapılmaktadır. 

Örneğin B1xx grubu IoT grubu olmakla beraber, B18x alt grubu Bluetooth grubunu temsil etmektedir.

Alt grup tanımları her segment için ayrıca hazırlanan bir doküman üzerinden tanımlanmaktadır.

---

### [CD] Majör ve Minör versiyon kodları (A-Z, A-Z)
Modüller üzerinde yapılan her değişiklik versiyon kodu ile tanımlanmaktadır. Revizyon kod numarası yapılan her tip majör ve minör değişikliğini tanımlamaktadır. Versiyon değişim dokümanı ile versiyon değişme sebebi tanımlanmaktadır.

Her tip (aktif yada pasif) komponent değişimi (aynı kılıf alternatif komponentler hariç), PCB tasarım vb. gibi değişiklikler majör versiyon değişimine sebep olmaktadır.

Dizgi yapılmayan modül varyasyonları minör değişimine sebep olmaktadır.

---

### [Eeeeee] Üretim Parti ve sıra kodu (A-Z, 00001-99999)
Modül üretim ID numarası olarak da adlandırılmaktadır. geri bildirim ve satış kısmında kullanılacak olan internal kodlama amacı ile kullanılmaktadır.

E : Seri üretim Parti kodu A-Z. 15.12.2016 da üretildi demek yerine A kodunu vermek gibi. Prototip ürünler için X parti kodu rezerve edilmiştir. Prototip ürünler X00001 den başlayarak kodlanmaktadır.

eeeee : Sıra numarası 00000-99999

Üretim parti ve sıra kodu her bir revizyon (majör, minör) için sıfırlanmaktadır.

---

### [Fff] Parça Kodu (Komponentler için, diğer durumlarda opsiyonel)
B kodu ile birlikte kullanılabilir. Komponentlerin şematikte verilen referans numarasıdır. C12 gibi. Fff Boş PCB için "PCB" olarak kodlanacaktır.

Örneğin
B102AA devresinin boş PCB'si (prototip) : B102AA-X00001-PCB
B102AA devresinin C31 kondansatörü : B102AA-X00001-C31 (1uF kondansatör)

### [G] Özel Üretim Kodu (Bağlantı şekli, kullanım şekli vb durumlarda opsiyonel)
Modül üretim yapısı gereği tanımlanması gereken özel bir üretim kodudur. Örneğin PCIe soket yapısına sahip bir modül için **PCIe** eklentisi yapılmaktadır. Bu şekilde kod üzerinden sistemin tam olarak nasıl kullanılacağına ilişkin açıklama içerecektir. 

Tekil kullanım için uygun olan modüller (üzerinde harici çıkış konnektörleri ve soketleri gibi genel bağlantı elemanları bulunduran) için bu kod zorunlu değildir. Fakat özel bir bağlantı sistemine sahip standartları daha önce tanımlanmış yapıdaki modüller için bu kod zorunludur.