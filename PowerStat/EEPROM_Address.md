# EEPROM Address Table

Sistem içerisinde yer alan EEPROM üzerindeki register adresleri ve register isimleri aşağıdaki tabloda belirtilmiştir. Bu değerler sistem boot esnasında okunarak ayarlar ilgili değişkenlere aktarılmaktadır.

Enerji ile ilgili parametreler enerji çipi üzerine kaydedilecektir. Bunun yanı sıra basınç ile ilgili parametreler basınç senörü üzerine kaydedilecektir. 

| Address | Constant Name               | Description             |
|---------|-----------------------------|-------------------------|
| 0x00    | EEPROM_Online_Interval      | Online Interval         |
| 0x01    | EEPROM_Offline_Interval     | Offline Interval        |
| 0x02    |                             |                         |
| 0x03    |                             |                         |
| 0x04    |                             |                         |
| 0x05    |                             |                         |
| 0x06    | EEPROM_V_Min_MSB            | Voltage Min Limit       |
| 0x07    | EEPROM_V_Min_LSB            | Voltage Min Limit       |
| 0x08    | EEPROM_V_Max_MSB            | Voltage Max Limit       |
| 0x09    | EEPROM_V_Max_LSB            | Voltage Max Limit       |
| 0x0A    | EEPROM_I_Max_MSB            | Current Max Limit       |
| 0x0B    | EEPROM_I_Max_LSB            | Current Max Limit       |
| 0x0C    | EEPROM_FQ_Min               | Frequency Min Limit     |
| 0x0D    | EEPROM_FQ_Max               | Frequency Max Limit     |
| 0x0E    |                             |                         |
| 0x0F    |                             |                         |
| 0x10    | EEPROM_VIMB_Max             | Voltage Imbalance Limit |
| 0x11    | EEPROM_IIMB_Max             | Current Imbalance Limit |
| 0x12    |                             |                         |
| 0x13    |                             |                         |
| 0x14    |                             |                         |
| 0x15    | EEPROM_Current_Ratio        | CT Multiplier           |
| 0x16    |                             |                         |
| 0x17    |                             |                         |
| 0x18    |                             |                         |
| 0x19    |                             |                         |
| 0x1A    | EEPROM_PMIN_MSB             | Min Pressure Limit      |
| 0x1B    | EEPROM_PMIN_LSB             | Min Pressure Limit      |
| 0x1C    | EEPROM_PMAX_MSB             | Max Pressure Limit      |
| 0x1D    | EEPROM_PMAX_LSB             | Max Pressure Limit      |
| 0x1E    | EEPROM_PSLOPEMAX            | Max Pressure Slope      |
| 0x1F    |                             |                         |
| 0x20    | STOP_MASK_MSB_1             | Stop Mask MSB           |
| 0x21    | STOP_MASK_MSB_2             | Stop Mask MSB           |
| 0x22    | STOP_MASK_LSB_1             | Stop Mask LSB           |
| 0x23    | STOP_MASK_LSB_2             | Stop Mask LSB           |
| 0x24    | PUBLISH_MASK_MSB_1          | Publish Mask MSB        |
| 0x25    | PUBLISH_MASK_MSB_2          | Publish Mask MSB        |
| 0x26    | PUBLISH_MASK_LSB_1          | Publish Mask LSB        |
| 0x27    | PUBLISH_MASK_LSB_2          | Publish Mask LSB        |
| 0x28    | --                          | Reserved                |
| 0x29    | --                          | Reserved                |
| 0x2A    | --                          | Reserved                |

***

## 0x00 - Pompa Çalışırken Veri Gönderim Aralığı

    Register Adı : [EEPROM_Online_Interval]

Sistem ana kurgusu gereği pompa çalışırken daha sık veri gönderimi yapmakta ve pompa duruyorken daha seyrek veri gönderimi yapmaktadır. Bu sayede sistemdeki veri trafiği azaltılmaktadır. Bu nedenle veri gönderim aralığı 1-255 dakika arasında ayarlanabilmektedir. Register değeri 0x00 olarak ayarlanırsa sistem herhangi bir veri gönderimi yapmayacaktır.

    0x00 : Veri gönderimi yapılmayacak.
    0x01 - 0xFF : Veri gönderimi dakika cinsinden yapılacaktır.

Sistem içerisinde yer alan RTC üzerinde alarm değeri saniye cinsinden ayarlanmaktadır. Bu nedenle EEPROM üzerindeki değer 60 ile çarpılarak RTC alarm değeri olarak ayarlanmaktadır.

    RTC Alarm = EEPROM_Online_Interval * 60

Varsayılan değerler ise aşağıdaki gibidir.

    EEPROM_Online_Interval : 10 dakika

***

## 0x01 - Pompa Duruyorken Veri Gönderim Aralığı

    Register Adı : [EEPROM_Offline_Interval]

Sistem ana kurgusu gereği pompa çalışırken daha sık veri gönderimi yapmakta ve pompa duruyorken daha seyrek veri gönderimi yapmaktadır. Bu sayede sistemdeki veri trafiği azaltılmaktadır. Bu nedenle veri gönderim aralığı 1-255 dakika arasında ayarlanabilmektedir. Register değeri 0x00 olarak ayarlanırsa sistem herhangi bir veri gönderimi yapmayacaktır.

    0x00 : Veri gönderimi yapılmayacak.
    0x01 - 0xFF : Veri gönderimi dakika cinsinden yapılacaktır.

Sistem içerisinde yer alan RTC üzerinde alarm değeri saniye cinsinden ayarlanmaktadır. Bu nedenle EEPROM üzerindeki değer 60 ile çarpılarak RTC alarm değeri olarak ayarlanmaktadır.

    RTC Alarm = EEPROM_Offline_Interval * 60

Varsayılan değerler ise aşağıdaki gibidir.

    EEPROM_Offline_Interval : 30 dakika

***

## 0x06/0x07 - Minimum Voltaj Limiti

    Register Adı : [EEPROM_V_Min_MSB]
    Register Adı : [EEPROM_V_Min_LSB]

Sistem içerisinde yer alan enerji ölçüm analizörü ile ölçülen voltaj değerinin minimum limit değeridir. Bu değer 2 byte olarak ayarlanmaktadır. 1. byte MSB 2. byte LSB değerini içermektedir. Bu değer 0x0000 - 0xFFFF arasında ayarlanabilmektedir. Bu değer 0x0000 olarak ayarlanırsa sistemde herhangi bir voltaj limiti uygulanmayacaktır. Bu limit değeri enerji analizör çipi içerisine interrupt olarak tanımlanmaktadır. Bu nedenle voltaj limiti aşıldığı zaman sistemde interrupt oluşmaktadır.

    0x0000 : Voltaj limiti uygulanmayacak.
    0x0001 - 0xFFFF : Voltaj limiti uygulanacaktır.

Varsayılan değerler ise aşağıdaki gibidir.

    EEPROM_V_Min : 192 V (0x00C0)

    EEPROM_V_Min_MSB : 0x00
    EEPROM_V_Min_LSB : 0xC0

***

## 0x08/0x09 - Maximum Voltaj Limiti

    Register Adı : [EEPROM_V_Max_MSB]
    Register Adı : [EEPROM_V_Max_LSB]

Sistem içerisinde yer alan enerji ölçüm analizörü ile ölçülen voltaj değerinin maximum limit değeridir. Bu değer 2 byte olarak ayarlanmaktadır. 1. byte MSB 2. byte LSB değerini içermektedir. Bu değer 0x0000 - 0xFFFF arasında ayarlanabilmektedir. Bu değer 0x0000 olarak ayarlanırsa sistemde herhangi bir voltaj limiti uygulanmayacaktır. Bu limit değeri enerji analizör çipi içerisine interrupt olarak tanımlanmaktadır. Bu nedenle voltaj limiti aşıldığı zaman sistemde interrupt oluşmaktadır.

    0x0000 : Voltaj limiti uygulanmayacak.
    0x0001 - 0xFFFF : Voltaj limiti uygulanacaktır.

Varsayılan değerler ise aşağıdaki gibidir.

    EEPROM_V_Max : 253 V (0x00FD)

    EEPROM_V_Max_MSB : 0x00
    EEPROM_V_Max_LSB : 0xFD

***

## 0x0A/0x0B - Maximum Akım Limiti

    Register Adı : [EEPROM_I_Max_MSB]
    Register Adı : [EEPROM_I_Max_LSB]

Sistem içerisinde yer alan enerji ölçüm analizörü ile ölçülen akım değerinin maximum limit değeridir. Bu değer 2 byte olarak ayarlanmaktadır. 1. byte MSB 2. byte LSB değerini içermektedir. Bu değer 0x0000 - 0xFFFF arasında ayarlanabilmektedir. Bu değer 0x0000 olarak ayarlanırsa sistemde herhangi bir voltaj limiti uygulanmayacaktır. Bu limit değeri enerji analizör çipi içerisine interrupt olarak tanımlanmaktadır. Bu nedenle akım limiti aşıldığı zaman sistemde interrupt oluşmaktadır.

    0x0000 : Akım limiti uygulanmayacak.
    0x0001 - 0xFFFF : Akım limiti uygulanacaktır.

Varsayılan değerler ise aşağıdaki gibidir.

    EEPROM_I_Max : 400 A (0x0190)

    EEPROM_I_Max_MSB : 0x01
    EEPROM_I_Max_LSB : 0x90

***

## 0x0C - Minimum Frekans Limiti

    Register Adı : [EEPROM_FQ_Min]

Sistem içerisinde yer alan enerji ölçüm analizörü ile ölçülen frekans değerinin minimum limit değeridir. Bu değer 0x00 - 0xFF arasında ayarlanabilmektedir. Bu değer 0x00 olarak ayarlanırsa sistemde herhangi bir frekans limiti uygulanmayacaktır. Bu limit değeri enerji analizör çipi içerisine interrupt olarak tanımlanmaktadır. Bu nedenle frekans limiti aşıldığı zaman sistemde interrupt oluşmaktadır.

    0x00 : Frekans limiti uygulanmayacak.
    0x01 - 0xFF : Frekans limiti uygulanacaktır.

Varsayılan değerler ise aşağıdaki gibidir.

    EEPROM_FQ_Min : 47 Hz (0x2F)

***

## 0x0D - Maximum Frekans Limiti

    Register Adı : [EEPROM_FQ_Max]

Sistem içerisinde yer alan enerji ölçüm analizörü ile ölçülen frekans değerinin maximum limit değeridir. Bu değer 0x00 - 0xFF arasında ayarlanabilmektedir. Bu değer 0x00 olarak ayarlanırsa sistemde herhangi bir frekans limiti uygulanmayacaktır. Bu limit değeri enerji analizör çipi içerisine interrupt olarak tanımlanmaktadır. Bu nedenle frekans limiti aşıldığı zaman sistemde interrupt oluşmaktadır.

    0x00 : Frekans limiti uygulanmayacak.
    0x01 - 0xFF : Frekans limiti uygulanacaktır.

Varsayılan değerler ise aşağıdaki gibidir.
    
        EEPROM_FQ_Max : 53 Hz (0x35)

***

## 0x10 - Voltaj Dengesizlik Limiti

    Register Adı : [EEPROM_VIMB_Max]

Sistem içerisinde yer alan enerji ölçüm analizörü ile ölçülen voltaj dengesizlik değerinin limit değeridir. Bu değer 0x00 - 0xFF arasında ayarlanabilmektedir. Bu değer 0x00 olarak ayarlanırsa sistemde herhangi bir voltaj dengesizlik limiti uygulanmayacaktır. Bu limit değeri enerji analizör çipi içerisine interrupt olarak tanımlanmaktadır. Bu nedenle voltaj dengesizlik limiti aşıldığı zaman sistemde interrupt oluşmaktadır.

    0x00 : Voltaj dengesizlik limiti uygulanmayacak.
    0x01 - 0xFF : Voltaj dengesizlik limiti uygulanacaktır.

Varsayılan değerler ise aşağıdaki gibidir.

    EEPROM_VIMB_Max : 6 % (0x06)

***

## 0x11 - Akım Dengesizlik Limiti

    Register Adı : [EEPROM_IIMB_Max]

Sistem içerisinde yer alan enerji ölçüm analizörü ile ölçülen akım dengesizlik değerinin limit değeridir. Bu değer 0x00 - 0xFF arasında ayarlanabilmektedir. Bu değer 0x00 olarak ayarlanırsa sistemde herhangi bir akım dengesizlik limiti uygulanmayacaktır. Bu limit değeri enerji analizör çipi içerisine interrupt olarak tanımlanmaktadır. Bu nedenle akım dengesizlik limiti aşıldığı zaman sistemde interrupt oluşmaktadır.

    0x00 : Akım dengesizlik limiti uygulanmayacak.
    0x01 - 0xFF : Akım dengesizlik limiti uygulanacaktır.

Varsayılan değerler ise aşağıdaki gibidir.

    EEPROM_IIMB_Max : 6 % (0x06)

***

## 0x1A/0x1B - Minimum Basınç Limiti

    Register Adı : [EEPROM_PMIN_MSB]
    Register Adı : [EEPROM_PMIN_LSB]

Sistem içerisinde yer alan basınç sensörü ile ölçülen basınç değerinin minimum limit değeridir. Bu değer 2 byte olarak ayarlanmaktadır. 1. byte MSB 2. byte LSB değerini içermektedir. Bu değer 0x0000 - 0xFFFF arasında ayarlanabilmektedir. Bu değer 0x0000 olarak ayarlanırsa sistemde herhangi bir basınç limiti uygulanmayacaktır. 

    0x0000 : Basınç limiti uygulanmayacak.
    0x0001 - 0xFFFF : Basınç limiti uygulanacaktır.

Varsayılan değerler ise aşağıdaki gibidir.

    EEPROM_PMIN : 0 Bar (0x0000)

    EEPROM_PMIN_MSB : 0x00
    EEPROM_PMIN_LSB : 0x00

***

## 0x1C/0x1D - Maximum Basınç Limiti

    Register Adı : [EEPROM_PMAX_MSB]
    Register Adı : [EEPROM_PMAX_LSB]

Sistem içerisinde yer alan basınç sensörü ile ölçülen basınç değerinin maximum limit değeridir. Bu değer 2 byte olarak ayarlanmaktadır. 1. byte MSB 2. byte LSB değerini içermektedir. Bu değer 0x0000 - 0xFFFF arasında ayarlanabilmektedir. Bu değer 0x0000 olarak ayarlanırsa sistemde herhangi bir basınç limiti uygulanmayacaktır.

    0x0000 : Basınç limiti uygulanmayacak.
    0x0001 - 0xFFFF : Basınç limiti uygulanacaktır.

Varsayılan değerler ise aşağıdaki gibidir.

    EEPROM_PMAX : 10 Bar (0x000A)

    EEPROM_PMAX_MSB : 0x00
    EEPROM_PMAX_LSB : 0x0A

***

## 0x1E - Basınç Yükseliş/Düşüş Hızı Limiti

    Register Adı : [EEPROM_PSLOPEMAX]

Sistem içerisinde yer alan basınç sensörü ile ölçülen basınç değerinin yükseliş/düşüş hızı limit değeridir. Bu değer 0x00 - 0xFF arasında ayarlanabilmektedir. Bu değer 0x00 olarak ayarlanırsa sistemde herhangi bir basınç yükseliş/düşüş hızı limiti uygulanmayacaktır.

    0x00 : Basınç yükseliş/düşüş hızı limiti uygulanmayacak.
    0x01 - 0xFF : Basınç yükseliş/düşüş hızı limiti uygulanacaktır.

Varsayılan değerler ise aşağıdaki gibidir.

    EEPROM_PSLOPEMAX : 10% (0x0A)

***

## 0x20/0x21/0x22/0x23 - Stop Mask

    Register Adı : [STOP_MASK_MSB_1]
    Register Adı : [STOP_MASK_MSB_2]
    Register Adı : [STOP_MASK_LSB_1]
    Register Adı : [STOP_MASK_LSB_2]

Sistem çalışma algoritması gereğince anlık olarak oluşturulan STATUS registeri istenilen durumlarda pompayı otomatik olarak durdurması istenmektedir. Bu durdurma işlemleri için bit bazında set edilen maskedir. Bu bit değerleri yukarıda belirtilen register tablosu ile aynıdır.

Varsayılan değerler ise aşağıdaki gibidir.

    STOP_MASK_MSB_1 : 0x0F
    STOP_MASK_MSB_2 : 0xF0
    STOP_MASK_LSB_1 : 0x08
    STOP_MASK_LSB_2 : 0x6E

    STOP_MASK : 0x0FF0086E

***

## 0x24/0x25/0x26/0x27 - Publish Mask

    Register Adı : [PUBLISH_MASK_MSB_1]
    Register Adı : [PUBLISH_MASK_MSB_2]
    Register Adı : [PUBLISH_MASK_LSB_1]
    Register Adı : [PUBLISH_MASK_LSB_2]

Sistem çalışma algoritması gereğince anlık olarak oluşturulan STATUS registeri istenilen durumlarda veri gönderimi yapılması istenmektedir. Bu durdurma işlemleri için bit bazında set edilen maskedir. Bu bit değerleri yukarıda belirtilen register tablosu ile aynıdır.

Varsayılan değerler ise aşağıdaki gibidir.

    PUBLISH_MASK_MSB_1 : 0x0F
    PUBLISH_MASK_MSB_2 : 0xF0
    PUBLISH_MASK_LSB_1 : 0x8C
    PUBLISH_MASK_LSB_2 : 0x6F

    PUBLISH_MASK : 0x0FF08C6F

***

## 0x28/0x29/0x2A - Reserved

    Register Adı : [Reserved]

Bu registerlar kullanılmamaktadır.