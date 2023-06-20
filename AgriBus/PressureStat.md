# PressureStat Komut Seti

RS485 donanım mimarisi ile iletişim kuran PressureStat modülü, AgriBus iletişim protokolü ile su basıncı ölçümlemesi yapan bir sensördür. Aşağıdaki komut setlerini kullanmaktadır.

## Sensör Kalibrasyonu

PressureStat cihazı içerisinde EEPROM üzerine kayıtlı kalibrasyon parametreleri yer almaktadır. Bu parametreler lineer kalibrasyon parametrelerini (Y=aX+b - a:Slope b:Offset) içeren **slope** ve **offset** değerleridir. Bu kaibraston parametreleri ayrı ayrı set edilebildiği gibi (2 ayrı komut ile) tek seferde de set edilebilmektedir. Bu komut setleri aşağıda belirtilmiştir.

### Tek Komutlu Kalibrasyon

Tek komutlu kalibrasyon prosedüründe **Data/Set** verisi içerisinde 4+4 byte olarak (a ve b parametreleri) 2 farklı kalibrasyon parametresi float veri tipi ile (negatif değerler içerebilen float->HEX verisi) kalibre edilmektedir. 

| Açıklama           | 1. Segment | 2. Segment |
|--------------------|------------|------------|
| Veri Tipi          | Slope      | Offset     |
| Örnek Veri (float) | 1.5777     | -1.1925    |
| Örnek Veri (HEX)   | 0x3FC9F213 | 0xBF98A3D7 |

Komut seti aşağıdaki gibidir.

| Komut Yönü | Start | Address | Command     | Data/Set                                              | CRC  | Stop |
|:----------:|:-----:|:-------:|:-----------:|:-----------------------------------------------------:|:----:|:----:|
| M --> S    | 0xA2  | 0x10    | 0x1E - 0xFE | 0x3F - 0xC9 - 0xF2 - 0x13 - 0xBF - 0x98 - 0xA3 - 0xD7 | 0x55 | 0xFF |
| S --> M    | 0xB2  | 0x10    | 0x1E - 0xFE | 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 | 0x23 | 0xFF |

### Çok Komutlu Kalibrasyon

Çok komutlu kalibrasyon prosedüründe 2 ayrı komut ile kalibrasyon parametreleri double olarak (negatif değerler içerebilen double->HEX verisi) kalibre edilmektedir.

| Açıklama            | Slope              | Offset             |
|---------------------|--------------------|--------------------|
| Örnek Veri (double) | 1.5777             | -1.1925            |
| Örnek Veri (HEX)    | 0x3FF93E425AEE6320 | 0xBFF3147AE147AE14 |

* Slope değeri ayarlama

| Komut Yönü | Start | Address | Command     | Data/Set                                              | CRC  | Stop |
|:----------:|:-----:|:-------:|:-----------:|:-----------------------------------------------------:|:----:|:----:|
| M --> S    | 0xA2  | 0x10    | 0x1E - 0xFA | 0x3F - 0xF9 - 0x3E - 0x42 - 0x5A - 0xEE - 0x63 - 0x20 | 0xB4 | 0xFF |
| S --> M    | 0xB2  | 0x10    | 0x1E - 0xFA | 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 | 0x27 | 0xFF |

* Offset değeri ayarlama

| Komut Yönü | Start | Address | Command     | Data/Set                                              | CRC  | Stop |
|:----------:|:-----:|:-------:|:-----------:|:-----------------------------------------------------:|:----:|:----:|
| M --> S    | 0xA2  | 0x10    | 0x1E - 0xFB | 0xBF - 0xF3 - 0x14 - 0x7A - 0xE1 - 0x47 - 0xAE - 0x14 | 0xFC | 0xFF |
| S --> M    | 0xB2  | 0x10    | 0x1E - 0xFB | 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 | 0x26 | 0xFF |

## Ölçümleri ve İstatistik Verilerini Sıfırlama

Sensör üzerinde yapılan bir kalibrasyon değişikliği yada sistem gereksinimleri gereği veri setinin sıfırlanması gerektiği durumlarda sensör üzerinde sıfırlama komutu ile işlem yapılacaktır. Aşağıdaki komut prosedürü ile sıfırlanmaktadır.

| Komut Yönü | Start | Address | Command     | Data/Set                                              | CRC  | Stop |
|:----------:|:-----:|:-------:|:-----------:|:-----------------------------------------------------:|:----:|:----:|
| M --> S    | 0xA2  | 0x10    | 0x1E - 0x0F | 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 | 0x22 | 0xFF |
| S --> M    | 0xB2  | 0x10    | 0x1E - 0x0F | 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 | 0x12 | 0xFF |

## Sensör İnterrupt Aktif Etme

Sensör üzerinde yapılan limit alarları dışına çıktığı zaman sensör tarafından interrupt sinyali üretilmektedir. Bu interruptın aktif veya pasif edilmesi aşağıdaki komut prosedürü ile yapılmaktadır.

* İnterrupt aktif etme

| Komut Yönü | Start | Address | Command     | Data/Set                                              | CRC  | Stop |
|:----------:|:-----:|:-------:|:-----------:|:-----------------------------------------------------:|:----:|:----:|
| M --> S    | 0xA2  | 0x10    | 0x1E - 0x0D | 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x01 | 0x21 | 0xFF |
| S --> M    | 0xB2  | 0x10    | 0x1E - 0x0D | 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 | 0x12 | 0xFF |

* İnterrupt pasif etme

| Komut Yönü | Start | Address | Command     | Data/Set                                              | CRC  | Stop |
|:----------:|:-----:|:-------:|:-----------:|:-----------------------------------------------------:|:----:|:----:|
| M --> S    | 0xA2  | 0x10    | 0x1E - 0x0D | 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 | 0x22 | 0xFF |
| S --> M    | 0xB2  | 0x10    | 0x1E - 0x0D | 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 | 0x12 | 0xFF |

## Anlık Hat Basıncı Ölçümleme

| Komut Yönü | Start | Address | Command     | Data/Set                                              | CRC  | Stop |
|:----------:|:-----:|:-------:|:-----------:|:-----------------------------------------------------:|:----:|:----:|
| M --> S    | 0xA0  | 0x10    | 0x1E - 0x10 | 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 | 0x23 | 0xFF |
| S --> M    | 0xB0  | 0x10    | 0x1E - 0x10 | 0x40 - 0x14 - 0x7A - 0xE1 - 0x47 - 0xEA - 0x14 - 0x7B | 0xA4 | 0xFF |

## Max Hat Basıncı Ölçümleme (Ölçüm Sonrası Sıfırla)

| Komut Yönü | Start | Address | Command     | Data/Set                                              | CRC  | Stop |
|:----------:|:-----:|:-------:|:-----------:|:-----------------------------------------------------:|:----:|:----:|
| M --> S    | 0xA1  | 0x10    | 0x1E - 0x11 | 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 | 0x21 | 0xFF |
| S --> M    | 0xB1  | 0x10    | 0x1E - 0x11 | 0x40 - 0x09 - 0xB5 - 0x0B - 0x0F - 0x27 - 0xBB - 0x30 | 0xE7 | 0xFF |

## Max Hat Basıncı Ölçümleme (Ölçüm Sonrası Sıfırlama)

| Komut Yönü | Start | Address | Command     | Data/Set                                              | CRC  | Stop |
|:----------:|:-----:|:-------:|:-----------:|:-----------------------------------------------------:|:----:|:----:|
| M --> S    | 0xA0  | 0x10    | 0x1E - 0x11 | 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 | 0x22 | 0xFF |
| S --> M    | 0xB0  | 0x10    | 0x1E - 0x11 | 0x40 - 0x09 - 0xB5 - 0x0B - 0x0F - 0x27 - 0xBB - 0x30 | 0xE8 | 0xFF |

## Min Hat Basıncı Ölçümleme (Ölçüm Sonrası Sıfırla)

| Komut Yönü | Start | Address | Command     | Data/Set                                              | CRC  | Stop |
|:----------:|:-----:|:-------:|:-----------:|:-----------------------------------------------------:|:----:|:----:|
| M --> S    | 0xA1  | 0x10    | 0x1E - 0x12 | 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 | 0x20 | 0xFF |
| S --> M    | 0xB1  | 0x10    | 0x1E - 0x12 | 0x40 - 0x09 - 0xB5 - 0x0B - 0x0F - 0x27 - 0xBB - 0x30 | 0xE6 | 0xFF |

## Min Hat Basıncı Ölçümleme (Ölçüm Sonrası Sıfırlama)

| Komut Yönü | Start | Address | Command     | Data/Set                                              | CRC  | Stop |
|:----------:|:-----:|:-------:|:-----------:|:-----------------------------------------------------:|:----:|:----:|
| M --> S    | 0xA0  | 0x10    | 0x1E - 0x12 | 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 | 0x21 | 0xFF |
| S --> M    | 0xB0  | 0x10    | 0x1E - 0x12 | 0x40 - 0x09 - 0xB5 - 0x0B - 0x0F - 0x27 - 0xBB - 0x30 | 0xE7 | 0xFF |

## Ortalama Hat Basıncı Ölçümleme (Ölçüm Sonrası Sıfırla)

| Komut Yönü | Start | Address | Command     | Data/Set                                              | CRC  | Stop |
|:----------:|:-----:|:-------:|:-----------:|:-----------------------------------------------------:|:----:|:----:|
| M --> S    | 0xA1  | 0x10    | 0x1E - 0x16 | 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 | 0x1C | 0xFF |
| S --> M    | 0xB1  | 0x10    | 0x1E - 0x16 | 0x40 - 0x09 - 0xB5 - 0x0B - 0x0F - 0x27 - 0xBB - 0x30 | 0xE2 | 0xFF |

## Ortalama Hat Basıncı Ölçümleme (Ölçüm Sonrası Sıfırlama)

| Komut Yönü | Start | Address | Command     | Data/Set                                              | CRC  | Stop |
|:----------:|:-----:|:-------:|:-----------:|:-----------------------------------------------------:|:----:|:----:|
| M --> S    | 0xA0  | 0x10    | 0x1E - 0x16 | 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 | 0x1D | 0xFF |
| S --> M    | 0xB0  | 0x10    | 0x1E - 0x16 | 0x40 - 0x09 - 0xB5 - 0x0B - 0x0F - 0x27 - 0xBB - 0x30 | 0xE3 | 0xFF |

## Gelişmiş Ortalama Hat Basıncı Ölçümleme (Ölçüm Sonrası Sıfırla)

| Komut Yönü | Start | Address | Command     | Data/Set                                              | CRC  | Stop |
|:----------:|:-----:|:-------:|:-----------:|:-----------------------------------------------------:|:----:|:----:|
| M --> S    | 0xA1  | 0x10    | 0x1E - 0x17 | 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 | 0x1B | 0xFF |
| S --> M    | 0xB1  | 0x10    | 0x1E - 0x17 | 0x40 - 0x09 - 0xB5 - 0x0B - 0x0F - 0x27 - 0xBB - 0x30 | 0xE1 | 0xFF |

## Gelişmiş Ortalama Hat Basıncı Ölçümleme (Ölçüm Sonrası Sıfırlama)

| Komut Yönü | Start | Address | Command     | Data/Set                                              | CRC  | Stop |
|:----------:|:-----:|:-------:|:-----------:|:-----------------------------------------------------:|:----:|:----:|
| M --> S    | 0xA0  | 0x10    | 0x1E - 0x17 | 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 - 0x00 | 0x1E | 0xFF |
| S --> M    | 0xB0  | 0x10    | 0x1E - 0x17 | 0x40 - 0x09 - 0xB5 - 0x0B - 0x0F - 0x27 - 0xBB - 0x30 | 0xE2 | 0xFF |
