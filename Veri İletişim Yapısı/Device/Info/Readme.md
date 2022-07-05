## 1. Info

Cihaza ait tanımlayıcı bilgileri içermektedir.

```json
"Info": {
    "ID": "70A11D1D01000026",
    "Hardware": "03.00.00",
    "Firmware": "03.00.00"
}
```

## Tiny Paket İçeriği

İlgili komutun içeriğinde tanımlandığı şekilde gerek veri paketini küçültmek gerekse backend işlemlerini aza indirmek amacı ile bazı durumlarda aşağıdaki tabloda belirtildiği üzere bazı parametreler sunucuya gönderilmeyecektir.

| Değişlen Adı  | Normal Paket      | Tiny Paket        | 
|---------------|:-----------------:|:-----------------:|
| ID			|:white_check_mark:	|:white_check_mark:	|
| Hardware		|:white_check_mark:	|:x:				|
| Firmware		|:white_check_mark:	|:x:				|

***

### “ID" : Cihaz ID Numarası

Cihaza ait tekil id numarasıdır. Bu numara ile tüm veritabanı kayıt işlemleri indekslenecektir. Seri üretim cihazlarda bu tekil veriyi sağlaması hemde her cihazın ayrı ayrı kodlanması iş yükünü getirmemek adına sistem içerisinde DS28C serial id çipi kullanılacaktır. Bu çip üzerinde fabrika çıkışı olarak kodlanmış 48 bit bir id bulunmaktadır. Elektronik sistemlerde genellikle veriler çip içerisinde bit olarak saklanmaktadır. 

Bu veriler okunduğu zaman HEX formatında okunmaktadır onluk sistemede çevrilebilecek olan bu id değişken taşması yaşamamak adına string olarak işleme alınmaktadır. DS28C çipi üzerinden onunan bu 48 bit id ye ek olarak 8 bit CRC verisi okunmaktadır. Polynomial “X8 + X5 + X4 + 1" doğrulama algoritması yardımı ile id doğrulaması yapılabilmektedir. Bu nedenle veri gönderimi yaparken 48+8 bit veri paketi HEX String formatında gönderilecektir.

```json
"ID": "70A11D1D01000026"
```

***

### “Hardware" : Donanım Versiyonu

Cihazın donanım tarafına ait tanımlayıcı versiyon bildirimidir. Majör ve minör versiyon yanı sıra (donanım versiyonu içerdiği modüllerde yer alan değişikliklere göre şekillenmektedir) üretim parti numarasını içermektedir. İlk 2 basamak **majör donanım versiyonu** sonraki 2 basamak ise **minör donanım versiyonu** bilgisini vermektedir. Son 2 basamak ise üretim parti numarasını içermektedir. Tüm bu versiyon yapısı GIT reposu üzerindeki release kodlarına aittir ve detayları repo üzerinde açıklanmıştır. XX.XX.XX yapısı şeklinde 8 byte string olarak gönderilmektedir (hep aynı uzunlukta).

    # Bu veri "tiny" paketlerinde gönderilemyecektir.

```json
"Hardware": "03.00.00"
```

	Versiyon kodlama yapısı semantik kodlama sistemi üzerine kurgulanmıştır.

***

### “Firmware" : Yazılım Versiyonu

Cihazın firmware tarafına ait tanımlayıcı versiyon bildirimidir. Majör, minör ve hata düzeltme durumlarını içermektedir. İlk 2 basamak **majör yazılım versiyonu** sonraki 2 basamak ise **minör yazılım versiyonu** bilgisini vermektedir. Son 2 basamak ise hata düzeltme kod versiyonu bilgisini içermektedir.


    # Bu veri "tiny" paketlerinde gönderilemyecektir.

```json
"Firmware": "03.00.00"
```

	Versiyon kodlama yapısı semantik kodlama sistemi üzerine kurgulanmıştır.

***