# I2C Haberleşme Kanalı

Modül iletişim kanalları içerisinde I2C haberleşme kanalı da yer almaktadır. Olası modül yapıları göz önüne alınarak eklenmiştir. Soket iletişim hattı ana kart üzerinde yer alan ana I2C hattından gelmektedir ve 3V3 seviyesindedir. 

I2C standartları doğrultusunda (bize özel); her I2C iletişim hattı kullanılam modül için I2C buffer kullanılması zorunlu kılınmıştır. Bu sayede adres çakışması ve güç anahtarlaması durumlarında oluşabilecek sorunlar ortadan kalkmıştır. Bu standartlar ayrıca bir doküman halinde açıklanacaktır.

| Açıklama          | Değer                                  |
|-------------------|----------------------------------------|
| Uzun Adı          | **MASTER_I2C_SCL**, **MASTER_I2C_SDA** |
| Kısa Adı          | **MASTER_I2C_SCL**, **MASTER_I2C_SDA** |
| Voltaj Seviyesi   | 3V3                                    |
| Sinyal            | Girişi ve Çıkış (işlemciye göre)       |

## I2C Enable Sinyali

Modül içerisinde kullanılmakta olan I2C entegreleri veya sensörleri için eğer mevcut ise enable sinyali bu hatta bağlanacaktır. Power enable yada communication enable sinyallerinden farklı olarak sadece entegre veya sensöre ait aktifleşme sinyalidir sistem geri kalanına etki etmez. Sinyal voltaj seviyesi 3V3 olarak tanımlanmıştır.

Kullanılmaması durumunda bağlanmayacaktır.

| Açıklama          | Değer                              |
|-------------------|------------------------------------|
| Uzun Adı          | **I2C_3V3_IC_ENABLE**              |
| Kısa Adı          | **I2C_IC_EN**                      |
| Voltaj Seviyesi   | 3V3                                |
| Sinyal            | Girişi (modüle Göre)               |

## I2C Interrupt Sinyali

Modül içerisinde kullanılan I2C entegre/sensör için gerekli olan interrupt çıkış sinyalidir. Sadece I2C bildirimleri için kullanılmaktadır. Sinyal voltaj seviyesi 3V3 olarak tanımlanmıştır.

Kullanılmaması durumunda bağlanmayacaktır.

| Açıklama          | Değer                              |
|-------------------|------------------------------------|
| Uzun Adı          | **I2C_3V3_INTERRUPT**              |
| Kısa Adı          | **I2C_IC_INT**                     |
| Voltaj Seviyesi   | 3V3                                |
| Sinyal            | Çıkış (modüle Göre)                |