# PCIe Global Soket Yapısı

Modüler sistem planlaması içerisinde tüm kartlar ve modüller için uyumlu bir veri yolu standardı belirlemek gerekmiştir. Bu nedenle PCIe-mini soketler için aşağıdaki bağlantı mimarisi uygun görülmüştür.

Kurum içi kodlama yapısında her türlü PCIe yapısına sahip modüller için "-PCIe" eklentisi yapılacaktır. Örneğin PCIe iletişim yapısına sahip GSM modülü için **B101AA-PCIe**

## PCIe Kart Yapısı

PCIe standartları doğrultusunda 4 farklı kart ebatı ve yapısı mevcuttur. Bu yapı kodları kart boyutu ve dizgi yönü göz önüne alınarak planlanmıştır. 

Kart bağlantı soketi fiziksel olarak yanlış takmayı engellemek adına 2 parçadan oluşmuştur. 1. küçük kısım iç yapımız gereği güç ve ana güç (veya iletişim) kontrol sinyalleri için ayrılmıştır. 2. ve büyük kısım ise diğer tüm sinyaller için kullanılmaktadır.

### Kart Ebat Standartları

| Standart | Kartı Adı | Açıklama | Ebat |
|----------------|-----------|----------|------|
| F1 | Full Mini Double | iki tarafıda dizgili büyük boy | 50.95 x 30 |
| F2 | Full Mini Single | tek tarafı dizgili büyük boy | 26.80 x 30 |
| H1 | Half Mini Double | iki tarafıda dizgili yarım boy | 50.95 x 30 |
| H2 | Half Mini Single | tek tarafıda dizgili yarım boy | 26.80 x 30 |

## Kart Ebat Detayları

    Full Mini

![Full Mini PCIe](https://github.com/akkoyun/Standartlar/blob/01.00.00/PCIe/Images/Full_Mini_PCIe_Dimension.png)

    Half Mini

![Half Mini PCIe](https://github.com/akkoyun/Standartlar/blob/01.00.00/PCIe/Images/Half_Mini_PCIe_Dimension.png)

## Kart Bağlantı Soketi

Modüller tek veya çift yön dizimine göre farklı soketlere bağlanmaktadır. Fakat modül tipleri standarda bindirmek adına tüm modüller çift yönlü kart olarak düşünülüp yüksek yapıda PCIe soketine bağlanacaktır. 

Örnek : TE-1775862-2 soketi kullanılması durumunda modülün alt yüzü için maksimum komponent yüksekliği 1.35mm olarak tanımlanmıştır. Bu koşullar sağlandığı zaman anakart ile komponent arasında 1.45mm boşluk kalmaktadır. kart-kart mesafesi 2.8mm dir. 

## PinOut

| Top Side | Pin ID | Pin ID | Bottom Side |
|---------:|:------:|:------:|:-------------|
| Power Feed | 01 | 02 | Power Feed |
| Power Feed | 03 | 04 | Power Feed |
| Power Feed | 05 | 06 | Power Feed |
| 3V3 | 07 | 08 | 3V3 |
| Vcc | 09 | 10 | Vcc |
| USB D+ | 11 | 12 | Power Enable |
| USB D- | 13 | 14 | Communication Enable |
| GND | 15 | 16 | GND |
| - | Key | Key | - |
| GND | 17 | 18 | GND |
| UART 1 RX [-] | 19 | 20 | UART 0 RX [3V3] |
| UART 1 TX [-] | 21 | 22 | UART 0 TX [3V3] |
| GND | 23 | 24 | GND |
| Analog 1 [3V3] | 25 | 26 | I/O Signa 1 [3V3] |
| Analog 2 [3V3] | 27 | 28 | I/O Signa 1 [3V3] |
| Analog 3 [3V3] | 29 | 30 | I/O Signa 1 [3V3] |
| Analog 4 [3V3] | 31 | 32 | I/O Signa 1 [3V3] |
| MOSI [3V3] | 33 | 34 | I/O Signa 1 [3V3] |
| MISO [3V3] | 35 | 36 | I/O Signa 1 [3V3] |
| SCK [3V3] | 37 | 38 | I/O Signa 1 [3V3] |
| CS [3V3] | 39 | 40 | I/O Signa 1 [3V3] |
| GND | 41 | 42 | GND |
| PWM 1 [3V3] | 43 | 44 | PWM 2 [3V3] |
| GND | 45 | 46 | GND |
| I2C Enable [3V3] | 47 | 48 | I2C SCL [3V3] |
| I2C Interrupt [3V3] | 49 | 50 | I2C SDA [3V3] |
| GND | 51 | 52 | GND |

### Soket Güç Bölümü [Power]

#### [POWER_FEED]

Sistem gereği 1A den yüksek güç çekecek her türlü güç hattı bu pinler üzerinden aktarılacaktır. Voltaj seviyesi modüle göre değişiklik gösterebilir. PCIe soketleri yapı gereği pin başına 500 mA akım çekebilmektedir. [POWER_FEED] pini 6 adet konumlandırılmış ve toplamda max sürekli 3A akıma dayanıklı olması için planlanmıştır.

Sadece 3V3 voltaj seviyesinin yettiği yüksek akım gereksinimi olmayan durumlarda kullanılmayacaktır.

#### [3V3]

Modüller içerisinde kullanılacak olan dijital yapı beslemesi için kullanılacak olan besleme pinidir. Maksimum 1A sürekli akıma dayanıklıdır.

#### [Vcc]

Modül içerisinde kullanılacak olan her çeşit (3V3 den farklı olarak) farklı voltaj seviyelerindeki besleme pinidir (örneğin VUSB, 5V, 1V8 gibi). Maksimum 1A sürekli akıma dayanıklıdır. 

Kullanılmaması durumunda bağlanmayacaktır. 

#### [POWER_ENABLE]

Modül içerisinde güç anahtarlaması (modül ve/veya içerdiği komponentlerin) yapılması durumunda bu sinyal hattı üzerinden işlem yapılacaktır. Aktif HIGH veya aktif LOW olma durumu modüle göre değişiklik göstereceği için PU/PD dirençleri takılacak kart üzerinde yer alacaktır. Voltaj seviyesi 3V3 olarak sabitlenmiştir.

Kullanılmaması durumunda bağlanmayacaktır.

#### [COMMUNICATION_ENABLE]

Modül içerisinde yer alan iletişim hatları (seviye dönüştürücü yada buffer gibi her türlü iletişim kesme donanımı dahil) kontrolü için kullanılmaktadır. Aktif HIGH veya aktif LOW olma durumu modüle göre değişiklik göstereceği için PU/PD dirençleri takılacak kart üzerinde yer alacaktır. Voltaj seviyesi 3V3 olarak sabitlenmiştir.

Kullanılmaması durumunda bağlanmayacaktır.

#### [USB Data]

Modül içerisinde yer alan USB iletişim hattı çıkışları test kartlarında kullanılması için (veya başka sebeple) modül dışına bu pinler ile çıkmaktadır. USB kullanılması durumunda Vcc pini VUSB beslemesi olarak kullanılacaktır.

Kullanılmaması durumunda bağlanmayacaktır.

#### [GND]

Sistem tüm GND hattı ortak olarak yapılandırılmıştır. Toplam 12 GND çıkışı bulunmakta ve sürekli 6A dönüş akımını desteklemektedir.

### Soket iletişim Bölümü [Data Signal]

#### [UART*]

Modül iletişim kanalları içerisinde seri haberleşme [UART] yapısıda bulunmaktadır. GSM AUX haberleşmesi gibi gerekli olabilecek durumlar düşünülerek 2 kanal UART planlanmış olup ana iletişim hattı UART0 hattıdır. Bu hat [COMMUNICATION_ENABLE] sinyali ile aktif/pasif edilebilmektedir. İletişim hattı standart voltaj seviyesi 3V3 olarak tanımlanmıştır. 

Her 2 kanal için kullanılmaması durumunda bağlanmayacaktır.

#### [SPI]

Modül iletişim kanalları içerisinde SPI haberleşme kanalı da yer almaktadır. Olası modül yapısı göz önüne alınarak eklenmiştir. İletişim hattı standart voltaj seviyesi 3V3 olarak tanımlanmıştır.

Kullanılmaması durumunda bağlanmayacaktır.

#### [I2C]

Modül içerisinde kullanılacak olan I2C iletişim kanalı için gerekli sinyal hattıdır. 3V3 voltaj seviyesinde işlemcinin ana I2C bus hattına bağlanacaktır. Veri yoluna ait PU dirençleri ana kart üzerinde yer alacaktır. 

##### [I2C_ENABLE]

Modül içerisinde kullanılmakta olan I2C entegreleri veya sensörleri için eğer mevcut ise enable sinyali bu hatta bağlanacaktır. Power enable yada communication enable sinyallerinden farklı olarak sadece entegre veya sensöre ait aktifleşme sinyalidir sistem geri kalanına etki etmez. Sinyal voltaj seviyesi 3V3 olarak tanımlanmıştır.

Kullanılmaması durumunda bağlanmayacaktır.

##### [I2C_INTERRUPT] 

Modül içerisinde kullanılan I2C entegre/sensör için gerekli olan interrupt sinyalidir. Sadece I2C bildirimleri için kullanılmaktadır. Sinyal voltaj seviyesi 3V3 olarak tanımlanmıştır.

Kullanılmaması durumunda bağlanmayacaktır.

#### [Analog Data]

Her türlü analog ölçüm yapılması gereken durumlarda bu sinyal hatları kullanılacaktır. Sensör çıkışı gibi durumlar için işlemci analog pinlerine direkt bağlı bir sinyal hattıdır. 3V3 voltaj seviyesinde olan bu hat için besleme filitresi işlemci tarafında yer almaktadır. Hat herhangi bir sinyal/güç hattı ile yakınlaşmadan direkt olarak modüle girmektedir.

Kullanılmaması durumunda bağlanmayacaktır.

#### [Dijital Data]

Modül içerisinde kullanılacak olan iletişim sinyallerinin tamamı bu pinler üzerinden iletişimde kullanılacaktır. Hem ESD hem filtre kapasitörleri modül ve ana kart üzerinde ayrı ayrı bulunacaktır. 3V3 voltaj seviyesi üzerinden haberleşecek olan porta ait PU/PD dirençleri modül üzerinde bulunacaktır. 

Kullanılmaması durumunda bağlanmayacaktır.
#### [PWM Data]

Modül üzerinde kullanılacak olan her türlü PWM sinyali bu pinler üzerinden iletişim kuracaktır. 3V3 voltaj seviyesine sahip iletişim hattı işlemcinin gerekli PWM pinlerine direkt olarak bağlanacaktır. 

Kullanılmaması durumunda bağlanmayacaktır.