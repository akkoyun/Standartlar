# AgriBus Standartları <sup>01.00.00</sup>

**AgriBus** RS485 işetişim protokolünü kullanan cihazlar için ortak bir protokol tanımlanması amacı ile geliştirilmiş bir protokoldür. **AgriBus** ana yapı itibari ile tarımsal amaçla kullanılan her türlü sensör, enerji analizörü, ekran ve I/O cihazlarının tamamında geçerli olacaktır.

**Örnek**

Sistem üzerinde yer alan 1 adet basınç sensörü üzerinden anlık su basıncını okuma prosedürü.

| Komut Yönü | Start | Address | Command     | Data/Set                                              | CRC  | Stop |
|:----------:|:-----:|:-------:|:-----------:|:-----------------------------------------------------:|:----:|:----:|
| M --> S | 0xA0  | 0x10    | 0x00 - 0x00 | 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 | 0x00 | 0xFF |
| S --> M | 0xB0  | 0x10    | 0x00 - 0x00 | 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 | 0x00 | 0xFF |

***

## Veri İletişim Paketi

Toplam 14 byte içeren veri iletişim paketi yapısı.

| Start | Address | Command     | Data/Set                                              | CRC  | Stop |
|:-----:|:-------:|:-----------:|:-----------------------------------------------------:|:----:|:----:|
| 0xA0  | 0x00    | 0x00 - 0x00 | 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 | 0x00 | 0xFF |

***

### Start Segmenti

İletişim paketinin başladığını belirten byte değeridir. Aşağıdaki değerler dahilinde sabitlenmiştir.

| Byte | Veri Yönü | Açıklama                                                       |
|------|-----------|----------------------------------------------------------------|
| 0xA0 | M --> S   | Master tarafından gönderilen data okuma komutu                 |
| 0xA1 | M --> S   | Master tarafından gönderilen data oku ve değeri sıfırla komutu |
| 0xA2 | M --> S   | Master tarafından gönderilen değişken set komutu               |
|      |           |                                                                |
| 0xB0 | S --> M   | Slave tarafından gönderilen data içeren paket.                 |
| 0xB1 | S --> M   | Slave tarafından gönderilen data ve sıfırlama onayı paketi.    |
| 0xB2 | S --> M   | Slave tarafından gönderilen set onay paketi.                   |
|      |           |                                                                |
| 0xF0 | S --> M   | Slave tarafından gönderilen komut bulunamadı hata paketi.      |
| 0xF1 | X --> X   | Slave tarafından gönderilen CRC hata paketi.                   |

***

### Address Segmenti

İletişim paketinin hangi slave cihazına gönderildiğini veya hangi slave cihazdan dönüş olduğunu belirten byte değeridir. Adres verisi 2. yarısı olan kısım slave cihaza ait ana segment bilgisini. 1. yarısı olan kısın ise (bit0 - bit3) slave cihaza ait öncelik verisini içermektedir. Aşağıdaki değerler dahilinde sabitlenmiştir.

| Adres | Majör Segment | Minör Segment |
|-------|---------------|---------------|
| 0x10  | 0x1_          | 0x_0          |

#### Majör Adres Segmenti (Grup)

AgriBus iletişim protokolü önceden tanımlanmış bir adresleme yapısı kullanmaktadır. Bu sayede hat üzerinde yer alan birden fazla cihaz ile istenilen cihazla anlık olarak iletişim kurabilmeye olanak sağlanmıştır. 

Slave cihazlar üretilirken bu majör adres segmentleri kullanılarak adreslenecektir. 

| Byte | Açıklama                                               |
|------|--------------------------------------------------------|
| 0x00 | Genel çağrı (Tüm slave cihazların kabul edeceği adres) |
| 0x1_ | Su basıncı (WP) ölçümlemesi yapan sensör segmenti.     |
| 0x2_ | Enerji ölçümlemesi yapan cihaz segmenti.               |
| 0x3_ | Meteoroloji ölçümlemesi yapan cihaz segmenti.          |
| 0x4_ |                                                        |
| 0x5_ |                                                        |
| 0x6_ |                                                        |
| 0x7_ |                                                        |
| 0x8_ |                                                        |
| 0x9_ |                                                        |
| 0xA_ | I/O girdisi ve çıktısı yapan cihaz segmenti.           |
| 0xB_ | Otomatik vana segmenti 1                               |
| 0xC_ | Otomatik vana segmenti 2                               |
| 0xD_ |                                                        |
| 0xE_ | Ekran cihazları segmenti.                              |
| 0xF_ |                                                        |

#### Minör Adres Segmenti (Öncelik)

AgriBus iletişim prokolünde birden fazla aynı tip slave cihaz kullanması durumunda veri paketlerinin çakışmasını engellemek için adres segmenti içerisine bir priority (öncelik) alanı eklenmiştir. Bu öncelik alanı varsayılan olak 0 kullanılmaktadır (en üst düzey öncelik). Öncelik seviyesi düştükçe bu değer artmaktadır. Ve öncelik seviyesine göre bir veri gönderim beklemesi devreye girmektedir.

Örneğin aynı dal üzerinde 3 adet basınç sensörü var ise bu sensörlerin adresleri 0x10, 0x11 ve 0x12 olmaktadır. Master tarafından bir basınç okuma istemi gönderildiği zaman her bir adres sahibi istenilen veriyi dönecektir. Bunun yanı sıra bir genel çağrı adresi ile bir basınç okunması istenir ise minör adres segmentinde yer alan değer kadar gecikmeli veri gönderilecektir. Mesela bahsi geçen sistemde master genel okuma komutu gönderir göndermez 0x10 adresli slave cihaz veri dönecek ardından t mS sonra 0x11 ve 2t mS sonra 0x12 adresli cihaz dönüş yapacaktır.

***

### Komut Segmenti

Slave cihaz üzerinde yapılması istenen işlevi tanımlayan (veri isteme yada set etme) işlevler için tanımlanmıştır. 2 byte dan oluşmakta ve aşağıdaki yapıda kurgulanmaktadır.

| Komut  | Majör Komut | Minör Komut |
|--------|-------------|-------------|
| 0x0000 | 0x00        | 0x00        |

#### Majör Komut Segmenti

Majör komut segmenti slave cihaz içerisinden hangi verinin okunacağı yada set edileceği bilgisini içermektedir. Veri tiplerine göre sınıflandırılmıştır.

|      | 0x0_    | 0x1_ | 0x2_ | 0x3_ | 0x4_ | 0x5_  | 0x6_    | 0x7_    | 0x8_    | 0x9_    | 0xA_ | 0xB_ | 0xC_ | 0xD_ | 0xE_ | 0xF_ |
|------|---------|------|------|------|------|-------|---------|---------|---------|---------|------|------|------|------|------|------|
| 0x_0 | Device  | AT   | ST   | V    | IN   | OUT   | VAL-A   | VAL-B   | SEL-A   | SEL-B   | --   | --   | --   | --   | HMI1 | --   |
| 0x_1 | --      | AH   | ST1  | VR   | IN1  | OUT1  | VAL-A1  | VAL-B1  | SEL-A1  | SEL-B1  | --   | --   | --   | --   | HMI2 | --   |
| 0x_2 | --      | AP   | ST2  | VS   | IN2  | OUT2  | VAL-A2  | VAL-B2  | SEL-A2  | SEL-B2  | --   | --   | --   | --   | --   | --   |
| 0x_3 | --      | --   | ST3  | VT   | IN3  | OUT3  | VAL-A3  | VAL-B3  | SEL-A3  | SEL-B3  | --   | --   | --   | --   | --   | --   |
| 0x_4 | --      | WS   | ST4  | I    | IN4  | OUT4  | VAL-A4  | VAL-B4  | SEL-A4  | SEL-B4  | --   | --   | --   | --   | --   | --   |
| 0x_5 | --      | WD   | ST5  | IR   | IN5  | OUT5  | VAL-A5  | VAL-B5  | SEL-A5  | SEL-B5  | --   | --   | --   | --   | --   | --   |
| 0x_6 | --      | --   | ST6  | IS   | IN6  | OUT6  | VAL-A6  | VAL-B6  | SEL-A6  | SEL-B6  | --   | --   | --   | --   | --   | --   |
| 0x_7 | --      | R    | ST7  | IT   | IN7  | OUT7  | VAL-A7  | VAL-B7  | SEL-A7  | SEL-B7  | --   | --   | --   | --   | --   | --   |
| 0x_8 | --      | --   | ST8  | P    | IN8  | OUT8  | VAL-A8  | VAL-B8  | SEL-A8  | SEL-B8  | --   | --   | --   | --   | --   | --   |
| 0x_9 | --      | UVI  | ST9  | PR   | IN9  | OUT9  | VAL-A9  | VAL-B9  | SEL-A9  | SEL-B9  | --   | --   | --   | --   | --   | --   |
| 0x_A | INT     | --   | ST10 | PS   | IN10 | OUT10 | VAL-A10 | VAL-B10 | SEL-A10 | SEL-B10 | --   | --   | --   | --   | --   | --   |
| 0x_B | INT-POL | ULT  | --   | PT   | IN11 | OUT11 | VAL-A11 | VAL-B11 | SEL-A11 | SEL-B11 | --   | --   | --   | --   | --   | --   |
| 0x_C | --      | ULH  | --   | E    | IN12 | OUT12 | VAL-A12 | VAL-B12 | SEL-A12 | SEL-B12 | --   | --   | --   | --   | --   | --   |
| 0x_D | --      | --   | --   | ER   | IN13 | OUT13 | VAL-A13 | VAL-B13 | SEL-A13 | SEL-B13 | --   | --   | --   | --   | --   | --   |
| 0x_E | --      | WP   | --   | ES   | IN14 | OUT14 | VAL-A14 | VAL-B14 | SEL-A14 | SEL-B14 | --   | --   | --   | --   | --   | --   |
| 0x_F | --      | --   | --   | ET   | IN15 | OUT15 | VAL-A15 | VAL-B15 | SEL-A15 | SEL-B15 | --   | --   | --   | --   | --   | --   |

#### Minör Komut Segmenti



***

### Data/Set Segmenti

Slave üzerinden bir verinin alınması veya bir değerin ayarlanması gerekli olan durumlarda bu segment içerisinde data veya set değeri yer alacaktır. Negatif değerlerde alabilen double veri tipi olaak kullanılacaktır.

* Master tarafından gönderilen paketlerde bu alan veri bütünlüğünü bozmamak adına boş (0x00000000) gönderilmektedir. 

* Eğer master slave üzerinden bir değer istedi ise bu segmentte 8 byte uzunluğunda double (eksi değerlerde olabilecek şekilde) değeri dönecektir. İstenen veri integer değeri ise virgülden sonraki kısım sıfır olarak gönderilecektir.

* Eğer master slave üzerinde bir değeri set etmek isterse bu segmentte set edilecek değer 8 byte uzunluğunda double (eksi değerlerde olabilecek şekilde) gönderilecektir. Set edilmek istenen veri integer değeri ise virgülden sonraki kısım sıfır olarak gönderilecektir.

#### Slave Cihazdan Veri Okuma

Slave cihazdan okunması istenen veri komutu gönderildiği zaman, slave üzerinden dönüş paketinde bu kısımda okunması istenen veri yer alacaktır. Geri dönüş değerleri her zaman double to hex (negatif değerleri içerebilir) dönüşümü ile gönderilmektedir. Eğer slave tam değer dönmesi gerekir ise virgülden sonrası sıfır olarak değerlendirilecektir.

**Örnek-1:**

Slave : Toprak altı sıcaklık sensörü.
İstenen Veri : 10 cm derinlikteki sıcaklık değeri.
Slave Ham Veri : 21.439 C

Mastera gönderilen veri paketi data segmenti :

```cpp
DataPack = 0x403570624dd2f1aa
```

**Örnek-2:**

Slave : Kepçeli yağmur sensörü.
İstenen Veri : Toplam kepçe tip sayısı.
Slave Ham Veri : 8 adet

Mastera gönderilen veri paketi data segmenti :

```cpp
DataPack = 0x4020000000000000
```

#### Slave Cihazda Veri Set Etme

Bazı durumlarda slave cihaz üzerinde bazı değişkenlerin set edilmesi gerekmektedir. Bu tip veri paketlerinde master cihaz veriyi gönderirken set değerini de paket içerisinde gönderir. Set değerleri her zaman double to hex (negatif değerleri içerebilir) dönüşümü ile gönderilmektedir. Eğer master tam değer set etmesi gerekir ise virgülden sonrası sıfır olarak değerlendirilecektir.

**Örnek-1:**

Slave : Toprak altı sıcaklık sensörü.
Gönderilen Set Verisi : Sıcaklık kalibrasyonu slope değeri.
Slave Ham Veri : 0.1903

Master tarafından gönderilen veri paketi data segmenti :

```cpp
DataPack = 0x3fc85bc01a36e2eb
```

***

### CRC Segmenti

İletişim paketi içerisinde yer alan tüm byte'ların mod 0xFF e göre 0 olması gerekmektedir. Bu sayede veri paketinin doğru iletildiği anlaşılmaktadır. Bu nedenle bu segmentte yer alan veri paketin tamamı için (CRC hariç diğer byte'lar) mod 0xFF tamamlayıcısı olarak kullanılmaktadır.

**Örnek**

Örneğin master sistemde bulunan 0x10 adresli bir slave basınç sensöründen anlık basınç değerini okuması istendiğinde aşağıda yer alan komutu gönderecektir.

| Start | Address | Command     | Data/Set                                              | CRC  | Stop |
|:-----:|:-------:|:-----------:|:-----------------------------------------------------:|:----:|:----:|
| 0xA0  | 0x10    | 0x20 - 0x10 | 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 | ?    | 0xFF |

Veri paketi toplamı : 0xA0+0x10+0x20+0x10+0xFF = 0x01DF
Mod 0xFF için kalan byte : 0x21
Toplam : 0x21 + 0x01DF = 0x200 --> mod 0xFF de kalan 0

CRC : 0x21

***

### Stop Segmenti

CRC segmentinde yer alan byte değeri kurgu gereği hiçbir zaman 0xFF olamayacağı için stop segmenti için 0xFF seçilmiştir.