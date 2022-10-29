# SPI Haberleşme Kanalı

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
