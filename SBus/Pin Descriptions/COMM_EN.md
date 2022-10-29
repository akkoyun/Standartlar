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
