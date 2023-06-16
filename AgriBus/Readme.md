# AgriBus Standartları <sup>01.00.00</sup>

**AgriBus** RS485 işetişim protokolünü kullanan cihazlar için ortak bir protokol tanımlanması amacı ile geliştirilmiş bir protokoldür. **AgriBus** ana yapı itibari ile tarımsal amaçla kullanılan her türlü sensör, enerji analizörü, ekran ve I/O cihazlarının tamamında geçerli olacaktır.

***

## Veri İletişim Paketi

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
| 0xB1 | S --> M   | Slave tarafından gönderilen data içeren paket.                 |
| 0xB2 | S --> M   | Slave tarafından gönderilen data ve sıfırlama onayı paketi.    |
| 0xB3 | S --> M   | Slave tarafından gönderilen set onay paketi.                   |
|      |           |                                                                |
| 0xF0 | S --> M   | Slave tarafından gönderilen komut bulunamadı hata paketi.      |

***

### Address Segmenti

İletişim paketinin hangi slave cihazına gönderildiğini veya hangi slave cihazdan dönüş olduğunu belirten byte değeridir. Adres verisi 2. yarısı olan kısım slave cihaza ait ana segment bilgisini. 1. yarısı olan kısın ise (bit0 - bit3) slave cihaza ait öncelik verisini içermektedir. Aşağıdaki değerler dahilinde sabitlenmiştir.

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
| 0xB_ |                                                        |
| 0xC_ |                                                        |
| 0xD_ |                                                        |
| 0xE_ | Ekran cihazları segmenti.                              |
| 0xF_ |                                                        |

***

### Data/Set Segmenti

Slave üzerinden bir verinin alınması veya bir değerin ayarlanması gerekli olan durumlarda bu segment içerisinde data veya set değeri yer alacaktır. 

* Master tarafından gönderilen paketlerde bu alan veri bütünlüğünü bozmamak adına boş (0x0000000000000000) gönderilmektedir. 

* Eğer master slave üzerinden bir değer istedi ise bu segmentte 8 byte uzunluğunda float (eksi değerlerde olabilecek şekilde) değeri dönecektir. İstenen veri integer değeri ise virgülden sonraki kısım sıfır olarak gönderilecektir.

* Eğer master slave üzerinde bir değeri set etmek isterse bu segmentte set edilecek değer 8 byte uzunluğunda float (eksi değerlerde olabilecek şekilde) gönderilecektir. Set edilmek istenen veri integer değeri ise virgülden sonraki kısım sıfır olarak gönderilecektir.

***

### CRC Segmenti

İletişim paketi içerisinde yer alan tüm byte'ların mod 0xFF e göre 0 olması gerekmektedir. Bu sayede veri paketinin doğru iletildiği anlaşılmaktadır. Bu nedenle bu segmentte yer alan veri paketin tamamı için (CRC hariç diğer byte'lar) mod 0xFF tamamlayıcısı olarak kullanılmaktadır.

***

### Stop Segmenti

CRC segmentinde yer alan byte değeri kurgu gereği hiçbir zaman 0xFF olamayacağı için stop segmenti için 0xFF seçilmiştir.