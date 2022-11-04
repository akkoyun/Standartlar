# Communication Enable

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

## I2C İletişim Modülleri için

I2C kullanım durumunda modül içerisinde bulunacak olan buffer (zorunlu) ile hem adres çakışması hemde güç anahtarlaması yapılması durumunda ortaya çıkacak olan aksaklıkların önüne geçmek adına **I2C_COMMUNICATION_ENABLE** (buffer enable) sinyali olarak kullanılacaktır.

| Açıklama          | Değer                        |
|-------------------|------------------------------|
| Uzun Adı          | **I2C_COMMUNICATION_ENABLE** |
| Kısa Adı          | **I2C_COMM_EN**              |
| Voltaj Seviyesi   | 3V3                          |
| Varsayılan Seviye | Değişken (AH/AL)             |
| Sinyal            | Girişi (modüle göre)         |

## UART İletişim Modülleri için

UART kullanımı durumunda modül içerisinde ulunacak olan buffer veya voltaj dönüştürücü (zorunlu değil) ile güç anahtarlaması veya gerekli durumlarda çıkacak aksaklıkların önüne geçmek adına **UART_COMMUNICATION_ENABLE** sinyali olarak kullanılacaktır.

| Açıklama          | Değer                         |
|-------------------|-------------------------------|
| Uzun Adı          | **UART_COMMUNICATION_ENABLE** |
| Kısa Adı          | **UART_COMM_EN**              |
| Voltaj Seviyesi   | 3V3                           |
| Varsayılan Seviye | Değişken (AH/AL)              |
| Sinyal            | Girişi (modüle göre           |
