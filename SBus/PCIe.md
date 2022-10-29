# PCIe

PCIe standartları doğrultusunda 4 farklı kart ebatı ve yapısı mevcuttur. Bu yapı kodları kart boyutu ve dizgi yönü göz önüne alınarak planlanmıştır. 

Kart bağlantı soketi fiziksel olarak yanlış takmayı engellemek adına 2 parçadan oluşmuştur. 1. küçük kısım iç yapımız gereği güç ve ana güç (veya iletişim) kontrol sinyalleri için ayrılmıştır. 2. ve büyük kısım ise diğer tüm sinyaller için kullanılmaktadır.

## Kart Ebat Standartları

| Standart | Kartı Adı        | Açıklama                       | Ebat          |
|:--------:|------------------|--------------------------------|---------------|
| F1       | Full Mini Double | iki tarafıda dizgili büyük boy | 50.95 x 30 mm |
| F2       | Full Mini Single | tek tarafı dizgili büyük boy   | 26.80 x 30 mm |
| H1       | Half Mini Double | iki tarafıda dizgili yarım boy | 50.95 x 30 mm |
| H2       | Half Mini Single | tek tarafıda dizgili yarım boy | 26.80 x 30 mm |

## Kart Ebat Detayları

    Full Mini

![Full Mini PCIe](/SBus/Images/Full_Mini_PCIe_Dimension.png)

    Half Mini

![Half Mini PCIe](/SBus/Images/Half_Mini_PCIe_Dimension.png)

## PinOut

| Top Side                                             | Pin ID | Pin ID | Bottom Side                                          |
|-----------------------------------------------------:|:------:|:------:|:-----------------------------------------------------|
| [Power Feed](/SBus/Pin%20Descriptions/POWER_FEED.md) | 01     | 02     | [Power Feed](/SBus/Pin%20Descriptions/POWER_FEED.md) |
| [Power Feed](/SBus/Pin%20Descriptions/POWER_FEED.md) | 03     | 04     | [Power Feed](/SBus/Pin%20Descriptions/POWER_FEED.md) |
| [Power Feed](/SBus/Pin%20Descriptions/POWER_FEED.md) | 05     | 06     | [Power Feed](/SBus/Pin%20Descriptions/POWER_FEED.md) |
| [3V3](/SBus/Pin%20Descriptions/3V3.md)               | 07     | 08     | [3V3](/SBus/Pin%20Descriptions/3V3.md)               |
| [VCC](/SBus/Pin%20Descriptions/VCC.md)               | 09     | 10     | [VCC](/SBus/Pin%20Descriptions/VCC.md)               |
| [USB D+](/SBus/Pin%20Descriptions/USB.md)            | 11     | 12     | [Power Enable](/SBus/Pin%20Descriptions/PWR_EN.md)   |
| [USB D-](/SBus/Pin%20Descriptions/USB.md)            | 13     | 14     | [Comm. Enable](/SBus/Pin%20Descriptions/COMM_EN.md)  |
| [GND](/SBus/Pin%20Descriptions/GND.md)               | 15     | 16     | [GND](/SBus/Pin%20Descriptions/GND.md)               |
| -                                                    | Key    | Key    | -                                                    |
| [GND](/SBus/Pin%20Descriptions/GND.md)               | 17     | 18     | [GND](/SBus/Pin%20Descriptions/GND.md)               |
| [UART1 RX](/SBus/Pin%20Descriptions/UART.md)         | 19     | 20     | [UART0 RX](/SBus/Pin%20Descriptions/UART.md)         |
| [UART1 TX](/SBus/Pin%20Descriptions/UART.md)         | 21     | 22     | [UART0 TX](/SBus/Pin%20Descriptions/UART.md)         |
| [GND](/SBus/Pin%20Descriptions/GND.md)               | 23     | 24     | [GND](/SBus/Pin%20Descriptions/GND.md)               |
| [Analog 1](/SBus/Pin%20Descriptions/ANALOG.md)       | 25     | 26     | [I/O Signal 1](/SBus/Pin%20Descriptions/DIGITAL.md)  |
| [Analog 2](/SBus/Pin%20Descriptions/ANALOG.md)       | 27     | 28     | [I/O Signal 2](/SBus/Pin%20Descriptions/DIGITAL.md)  |
| [Analog 3](/SBus/Pin%20Descriptions/ANALOG.md)       | 29     | 30     | [I/O Signal 3](/SBus/Pin%20Descriptions/DIGITAL.md)  |
| [Analog 4](/SBus/Pin%20Descriptions/ANALOG.md)       | 31     | 32     | [I/O Signal 4](/SBus/Pin%20Descriptions/DIGITAL.md)  |
| [MOSI](/SBus/Pin%20Descriptions/SPI.md)              | 33     | 34     | [I/O Signal 5](/SBus/Pin%20Descriptions/DIGITAL.md)  |
| [MISO](/SBus/Pin%20Descriptions/SPI.md)              | 35     | 36     | [I/O Signal 6](/SBus/Pin%20Descriptions/DIGITAL.md)  |
| [SCK](/SBus/Pin%20Descriptions/SPI.md)               | 37     | 38     | [I/O Signal 7](/SBus/Pin%20Descriptions/DIGITAL.md)  |
| [SS](/SBus/Pin%20Descriptions/SPI.md)                | 39     | 40     | [I/O Signal 8](/SBus/Pin%20Descriptions/DIGITAL.md)  |
| [GND](/SBus/Pin%20Descriptions/GND.md)               | 41     | 42     | [GND](/SBus/Pin%20Descriptions/GND.md)               |
| [PWM 1](/SBus/Pin%20Descriptions/PWM.md)             | 43     | 44     | [PWM 2](/SBus/Pin%20Descriptions/PWM.md)             |
| [GND](/SBus/Pin%20Descriptions/GND.md)               | 45     | 46     | [GND](/SBus/Pin%20Descriptions/GND.md)               |
| [I2C Enable](/SBus/Pin%20Descriptions/I2C.md)        | 47     | 48     | [I2C SCL](/SBus/Pin%20Descriptions/I2C.md)           |
| [I2C Interrupt](/SBus/Pin%20Descriptions/I2C.md)     | 49     | 50     | [I2C SDA](/SBus/Pin%20Descriptions/I2C.md)           |
| [GND](/SBus/Pin%20Descriptions/GND.md)               | 51     | 52     | [GND](/SBus/Pin%20Descriptions/GND.md)               |

## Modül Listesi

| Modül Adı   | Açıklama              | Tasarım Tarihi |
|-------------|-----------------------|----------------|
| B101AA-PCIe | LE910S1-EAG GSM Modül | 2022           |

## Kart Bağlantı Soketi

Modüller tek veya çift yön dizimine göre farklı soketlere bağlanmaktadır. Fakat modül tipleri standarda bindirmek adına tüm modüller çift yönlü kart olarak düşünülüp yüksek yapıda PCIe soketine bağlanacaktır. 

Örnek : TE-1775862-2 soketi kullanılması durumunda modülün alt yüzü için maksimum komponent yüksekliği 1.35mm olarak tanımlanmıştır. Bu koşullar sağlandığı zaman anakart ile komponent arasında 1.45mm boşluk kalmaktadır. kart-kart mesafesi 2.8mm dir. 
