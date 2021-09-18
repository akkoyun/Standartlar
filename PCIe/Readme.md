# PCIe Global Soket Yapısı <sup>01.01.02</sup>

Modüler sistem planlaması içerisinde tüm kartlar ve modüller için uyumlu bir veri yolu standardı belirlemek gerekmiştir. Bu nedenle PCIe-mini soketler için aşağıdaki bağlantı mimarisi uygun görülmüştür.

Kurum içi kodlama yapısında her türlü PCIe yapısına sahip modüller için "-PCIe" eklentisi yapılacaktır. Örneğin PCIe iletişim yapısına sahip GSM modülü için **B101AA-PCIe**

## PCIe Kart Yapısı

PCIe standartları doğrultusunda 4 farklı kart ebatı ve yapısı mevcuttur. Bu yapı kodları kart boyutu ve dizgi yönü göz önüne alınarak planlanmıştır. 

Kart bağlantı soketi fiziksel olarak yanlış takmayı engellemek adına 2 parçadan oluşmuştur. 1. küçük kısım iç yapımız gereği güç ve ana güç (veya iletişim) kontrol sinyalleri için ayrılmıştır. 2. ve büyük kısım ise diğer tüm sinyaller için kullanılmaktadır.

### Kart Ebat Standartları

| Standart | Kartı Adı | Açıklama | Ebat |
|:--------:|-----------|----------|------|
| F1 | Full Mini Double | iki tarafıda dizgili büyük boy | 50.95 x 30 mm |
| F2 | Full Mini Single | tek tarafı dizgili büyük boy | 26.80 x 30 mm |
| H1 | Half Mini Double | iki tarafıda dizgili yarım boy | 50.95 x 30 mm |
| H2 | Half Mini Single | tek tarafıda dizgili yarım boy | 26.80 x 30 mm |

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

***

### Soket Güç Bölümü [Power]

#### High Current Power Feed

Sistem gereği 1A den yüksek güç çekecek her türlü güç hattı bu pinler üzerinden aktarılacaktır. Voltaj seviyesi modüle göre değişiklik gösterebilir. 

PCIe soketleri yapı gereği pin başına 500 mA akım çekebilmektedir. Bu güç hattı 6 adet pin ile konumlandırılmış ve toplamda max sürekli 3A akıma dayanıklı olması için planlanmıştır.

Sadece dijital 3V3 voltaj seviyesinin yettiği yüksek akım gereksinimi olmayan durumlarda kullanılmayacaktır.

| Açıklama         | Değer                       |
|------------------|-----------------------------|
| Uzun Adı         | **HIGH_CURRENT_POWER_FEED** |
| Kısa Adı         | **POWER_FEED**              |
| Voltaj Seviyesi  | Değişken                    |
| Max Sürekli Akım | 3 A.                        |

#### Dijital 3V3

Modüller içerisinde kullanılacak olan dijital yapı elemanlarının beslemesi için kullanılacak olan besleme hattıdır. Maksimum 1A sürekli akıma (modül çıkılı 2 pin) dayanıklıdır.

| Açıklama         | Değer                       |
|------------------|-----------------------------|
| Uzun Adı         | **DIGITAL_3V3**             |
| Kısa Adı         | **3V3**                     |
| Voltaj Seviyesi  | Değişken                    |
| Max Sürekli Akım | 1 A.                        |

#### Vcc

Modül içerisinde kullanılacak olan her çeşit (dijital 3V3 den farklı olarak) farklı voltaj seviyelerindeki besleme hattıdır (örneğin VUSB, 5V, 1V8 gibi). 

Modüle giriş veya çıkış olarak kullanılabilmektedir. Pin yapısı maksimum 1A sürekli akıma (modül çıkışı 2 pin) dayanıklıdır. Çıkış pini olarak kullanılması durumunda maksimum çıkış akımı modül içerisindeki güç elemanları tarafından belirlenmektedir.

| Açıklama         | Değer                              |
|------------------|------------------------------------|
| Uzun Adı         | **VCC**                            |
| Kısa Adı         | **Vcc**, **Vusb**, **5V**, **1V8** |
| Voltaj Seviyesi  | Değişken                           |
| Max Sürekli Akım | 1 A.                               |

Kullanılmaması durumunda bağlanmayacaktır. 

#### Power Enable

Modül içerisinde güç anahtarlaması (modül ve/veya içerdiği komponentlerin) yapılması durumunda bu sinyal hattı üzerinden işlem yapılacaktır. 

Aktif HIGH veya aktif LOW olma durumu modüle göre değişiklik göstereceği için PU/PD dirençleri takılacak kart üzerinde yer alacaktır. Voltaj seviyesi 3V3 olarak sabitlenmiştir.

Kullanılmaması durumunda bağlanmayacaktır.

| Açıklama          | Değer                       |
|-------------------|-----------------------------|
| Uzun Adı          | **POWER_ENABLE**            |
| Kısa Adı          | **PWR_EN**                  |
| Voltaj Seviyesi   | 3V3                         |
| Varsayılan Seviye | Değişken (AH/AL)            |
| Sinyal            | Girişi (modüle göre)        |

#### Communication Enable

Modül içerisinde yer alan iletişim hatları (seviye dönüştürücü yada buffer gibi her türlü iletişim kesme donanımı dahil) kontrolü için kullanılmaktadır. 

Aktif HIGH veya aktif LOW olma durumu modüle göre değişiklik göstereceği için PU/PD dirençleri takılacak kart üzerinde yer alacaktır. Voltaj seviyesi 3V3 olarak sabitlenmiştir.

Modüllerimiz genellikle tek bir iletişim kanalı (SPI, UART, I2C) kullanmaktadır. Bu nedenle **COMMUNICATION_ENABLE** sinyali ilgili haberleşme kanalı için aktivite sinyali olarak kullanılacaktır.

Kullanılmaması durumunda bağlanmayacaktır.

| Açıklama          | Değer                       |
|-------------------|-----------------------------|
| Uzun Adı          | **COMMUNICATION_ENABLE**    |
| Kısa Adı          | **COMM_EN**                 |
| Voltaj Seviyesi   | 3V3                         |
| Varsayılan Seviye | Değişken (AH/AL)            |
| Sinyal            | Girişi (modüle göre)        |

##### I2C İletişim Modülleri için

I2C kullanım durumunda modül içerisinde bulunacak olan buffer (zorunlu) ile hem adres çakışması hemde güç anahtarlaması yapılması durumunda ortaya çıkacak olan aksaklıkların önüne geçmek adına **I2C_COMMUNICATION_ENABLE** (buffer enable) sinyali olarak kullanılacaktır.

| Açıklama          | Değer                        |
|-------------------|------------------------------|
| Uzun Adı          | **I2C_COMMUNICATION_ENABLE** |
| Kısa Adı          | **I2C_COMM_EN**              |
| Voltaj Seviyesi   | 3V3                          |
| Varsayılan Seviye | Değişken (AH/AL)             |
| Sinyal            | Girişi (modüle göre)         |

##### UART İletişim Modülleri için

UART kullanımı durumunda modül içerisinde ulunacak olan buffer veya voltaj dönüştürücü (zorunlu değil) ile güç anahtarlaması veya gerekli durumlarda çıkacak aksaklıkların önüne geçmek adına **UART_COMMUNICATION_ENABLE** sinyali olarak kullanılacaktır.

| Açıklama          | Değer                         |
|-------------------|-------------------------------|
| Uzun Adı          | **UART_COMMUNICATION_ENABLE** |
| Kısa Adı          | **UART_COMM_EN**              |
| Voltaj Seviyesi   | 3V3                           |
| Varsayılan Seviye | Değişken (AH/AL)              |
| Sinyal            | Girişi (modüle göre           |

#### USB İletişim Hattı

Modül içerisinde yer alan USB iletişim hattı çıkışları (kullanılması durumunda) test kartlarında kullanılması için (veya başka sebeple) modül dışına bu pinler ile çıkmaktadır. 

USB kullanılması durumunda Vcc pini VUSB beslemesi olarak kullanılacaktır.

Kullanılmaması durumunda bağlanmayacaktır.

| Açıklama          | Değer                            |
|-------------------|----------------------------------|
| Uzun Adı          | **USB_DATA_D+**, **USB_DATA_D-** |
| Kısa Adı          | **USB_D+**, **USB_D-**           |
| Voltaj Seviyesi   | 5V (VUSB)                        |
| Sinyal            | Girişi-Çıkış                     |

#### Ground [GND]

Sistem tüm GND hattı ortak olarak yapılandırılmıştır. Toplam 12 GND çıkışı bulunmakta ve sürekli 6A dönüş akımını desteklemektedir.

***

### Soket iletişim Bölümü [Data Signal]

#### Seri Haberleşme Kanalları [2xUART]

Modüller anakart ile ilgili iletişim kanalları üzerinden haberleşmektedir. Seri haberleşme (UART) bunların en çok kullanılanlarından birisidir. Bu nedenle modül bağlantısı içerisinde 2 kanal UART haberleşme giriş ve çıkışı bulunmaktadır.

GSM, WiFi veya BlueTooth gibi IoT modülleri için gerekli durumlarda (test vb) kullanılmak üzere 2 kanal olarak konumlandırılmıştır.

UART0 ve UART1 olarak gruplanan iletişi hatları için ana iletişim hattı UART0 olarak sabitlenmiştir. Bu ana iletişim hattı **[COMMUNICATION_ENABLE]** sinyali ile kontrol edilmektedir (aktif veya pasif). İletişim hattı sinyal voltaj seviyesi 3V3 olarak tanımlanmıştır (UART1 farklı voltaj seviyelerinde çalışabilmektedir).

| Açıklama          | Değer                              |
|-------------------|------------------------------------|
| Uzun Adı          | **3V3_UART0_TX**, **3V3_UART0_RX** |
| Kısa Adı          | **UART0_TX**, **UART0_RX**         |
| Voltaj Seviyesi   | 3V3                                |
| Sinyal            | Girişi ve Çıkış (modüle Göre)      |

| Açıklama          | Değer                              |
|-------------------|------------------------------------|
| Uzun Adı          | **UART1_TX**, **UART1_RX**         |
| Kısa Adı          | **UART0_TX**, **UART0_RX**         |
| Voltaj Seviyesi   | Değişken                           |
| Sinyal            | Girişi ve Çıkış (modüle Göre)      |

#### SPI Haberleşme Kanalı

Modül iletişim kanalları içerisinde SPI haberleşme kanalı da yer almaktadır. Olası modül yapısı göz önüne alınarak eklenmiştir. İletişim hattı standart voltaj seviyesi 3V3 olarak tanımlanmıştır.

Kullanılmaması durumunda bağlanmayacaktır.

| Açıklama          | Değer                              |
|-------------------|------------------------------------|
| Uzun Adı          | **3V3_SPI_MOSI**, **3V3_SPI_MISO**, **3V3_SPI_SCK**, **3V3_SPI_CS** |
| Kısa Adı          | **SPI_MOSI**, **SPI_MISO**, **SPI_SCK**, **SPI_CS** |
| Voltaj Seviyesi   | 3V3                                                 |
| Sinyal            | Girişi ve Çıkış (Veri Yapısına Göre)                |

    Debug modülü bağlantılarında (ilgili debug soketinde) CS hattı yerine işlemciye ait
    RESET sinyali kullanılacak ve böylece ICSP programlama yapılmasına olanak verecektir. 

#### I2C Haberleşme Kanalı

Modül iletişim kanalları içerisinde I2C haberleşme kanalı da yer almaktadır. Olası modül yapıları göz önüne alınarak eklenmiştir. Soket iletişim hattı ana kart üzerinde yer alan ana I2C hattından gelmektedir ve 3V3 seviyesindedir. 

I2C standartları doğrultusunda (bize özel); her I2C iletişim hattı kullanılam modül için I2C buffer kullanılması zorunlu kılınmıştır. Bu sayede adres çakışması ve güç anahtarlaması durumlarında oluşabilecek sorunlar ortadan kalkmıştır. Bu standartlar ayrıca bir doküman halinde açıklanacaktır.

| Açıklama          | Değer                                  |
|-------------------|----------------------------------------|
| Uzun Adı          | **MASTER_I2C_SCL**, **MASTER_I2C_SDA** |
| Kısa Adı          | **MASTER_I2C_SCL**, **MASTER_I2C_SDA** |
| Voltaj Seviyesi   | 3V3                                    |
| Sinyal            | Girişi ve Çıkış (işlemciye göre)       |

##### I2C Enable Sinyali

Modül içerisinde kullanılmakta olan I2C entegreleri veya sensörleri için eğer mevcut ise enable sinyali bu hatta bağlanacaktır. Power enable yada communication enable sinyallerinden farklı olarak sadece entegre veya sensöre ait aktifleşme sinyalidir sistem geri kalanına etki etmez. Sinyal voltaj seviyesi 3V3 olarak tanımlanmıştır.

Kullanılmaması durumunda bağlanmayacaktır.

| Açıklama          | Değer                              |
|-------------------|------------------------------------|
| Uzun Adı          | **I2C_3V3_IC_ENABLE**              |
| Kısa Adı          | **I2C_IC_EN**                      |
| Voltaj Seviyesi   | 3V3                                |
| Sinyal            | Girişi (modüle Göre)               |

##### I2C Interrupt Sinyali

Modül içerisinde kullanılan I2C entegre/sensör için gerekli olan interrupt çıkış sinyalidir. Sadece I2C bildirimleri için kullanılmaktadır. Sinyal voltaj seviyesi 3V3 olarak tanımlanmıştır.

Kullanılmaması durumunda bağlanmayacaktır.

| Açıklama          | Değer                              |
|-------------------|------------------------------------|
| Uzun Adı          | **I2C_3V3_INTERRUPT**              |
| Kısa Adı          | **I2C_IC_INT**                     |
| Voltaj Seviyesi   | 3V3                                |
| Sinyal            | Çıkış (modüle Göre)                |

#### Analog Sinyal Hatları (4x)

Her türlü analog ölçüm yapılması gereken durumlarda bu sinyal hatları kullanılacaktır. Sensör çıkışı gibi durumlar için işlemci analog pinlerine direkt bağlı bir sinyal hattıdır. 3V3 voltaj seviyesinde olan bu hat için besleme filitresi işlemci tarafında yer almaktadır. Hat herhangi bir sinyal/güç hattı ile yakınlaşmadan direkt olarak modüle girmektedir.

Kullanılmaması durumunda bağlanmayacaktır.

| Açıklama          | Değer                              |
|-------------------|------------------------------------|
| Uzun Adı          | **ANALOG_3V3_1**, **ANALOG_3V3_2** |
| Kısa Adı          | **ANALOG1**, **ANALOG2**           |
| Voltaj Seviyesi   | 3V3                                |
| Sinyal            | Girişi ve Çıkış (modüle Göre)      |

    Gerekli olması durumunda dijital hat olarak kullanılabilecektir. Dijital olarak 
    kullanılması durumunda analog iletişim yapılmayacaktır.

#### Dijital Sinyal Hatları (8x)

Modül içerisinde kullanılacak olan iletişim sinyallerinin tamamı bu pinler üzerinden iletişimde kullanılacaktır. Hem ESD hem filtre kapasitörleri modül ve ana kart üzerinde ayrı ayrı bulunacaktır. 3V3 voltaj seviyesi üzerinden haberleşecek olan porta ait PU/PD dirençleri modül üzerinde bulunacaktır. 

Kullanılmaması durumunda bağlanmayacaktır.

| Açıklama          | Değer                         |
|-------------------|-------------------------------|
| Uzun Adı          | **DIGITAL_3V3_IO1**           |
| Kısa Adı          | **DIO1**                      |
| Voltaj Seviyesi   | 3V3                           |
| Sinyal            | Girişi ve Çıkış (modüle Göre) |

#### PWM Sinyal Hatları (2x)

Modül üzerinde kullanılacak olan her türlü PWM sinyali bu pinler üzerinden iletişim kuracaktır. 3V3 voltaj seviyesine sahip iletişim hattı işlemcinin gerekli PWM pinlerine direkt olarak bağlanacaktır. 

Kullanılmaması durumunda bağlanmayacaktır.

| Açıklama          | Değer                              |
|-------------------|------------------------------------|
| Uzun Adı          | **PWM_3V3_1**, **PWM_3V3_2**       |
| Kısa Adı          | **PWM1**, **PWM2**                 |
| Voltaj Seviyesi   | 3V3                                |
| Sinyal            | Girişi ve Çıkış (modüle Göre)      |

    Gerekli olması durumunda dijital hat olarak kullanılabilecektir. Dijital olarak 
    kullanılması durumunda analog iletişim yapılmayacaktır.
