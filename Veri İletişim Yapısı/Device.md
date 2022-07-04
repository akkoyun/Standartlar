# Device Segment

Proje içerisinde kullanılmakta olan donanıma (cihaz elektronik donanımı) ait teknik verilerin olduğu ana veri paketi segmentidir. Cihaza ait donanım ve firmware versiyonları yanı sıra güç yönetimi ve IoT iletişim parametrelerini içerir.

```json
"Device": {
    "Info": {
        "ID": "70A11D1D01000026",
        "Hardware": "03.00.00",
        "Firmware": "03.00.00"
    },
    "Power": {
        "Battery": {
            "AC": -0.15,
            "FB": 2000,
            "IB": 1300,
            "IV": 4.17,
            "SOC": 92.13,
            "T": 0,
            "Charge": 3
        }
    },
    "IoT": {
        "GSM": {
            "Module": {
                "Firmware": "13.00.007",
                "IMEI": "353613080341871",
                "Manufacturer": 1,
                "Model": 1,
                "Serial": "0001767743"
            },
            "Operator": {
                "Iccid": "8990011916180288985",
                "Code": 28601,
                "RSSI": 10,
                "ConnTime": 22,
                "LAC": "855E",
                "Cell_ID": "BFAB"
            }
        }
    }
}
```

Bu segment içerisinde aşağıdaki alt segmentler yer almaktadır.

***

## 1. Info

Cihaza ait tanımlayıcı bilgileri içermektedir.

### “ID" : Cihaz ID Numarası

Cihaza ait tekil id numarasıdır. Bu numara ile tüm veritabanı kayıt işlemleri indekslenecektir. Seri üretim cihazlarda bu tekil veriyi sağlaması hemde her cihazın ayrı ayrı kodlanması iş yükünü getirmemek adına sistem içerisinde DS28C serial id çipi kullanılacaktır. Bu çip üzerinde fabrika çıkışı olarak kodlanmış 48 bit bir id bulunmaktadır. Elektronik sistemlerde genellikle veriler çip içerisinde bit olarak saklanmaktadır. 

Bu veriler okunduğu zaman HEX formatında okunmaktadır onluk sistemede çevrilebilecek olan bu id değişken taşması yaşamamak adına string olarak işleme alınmaktadır. DS28C çipi üzerinden onunan bu 48 bit id ye ek olarak 8 bit CRC verisi okunmaktadır. Polynomial “X8 + X5 + X4 + 1" doğrulama algoritması yardımı ile id doğrulaması yapılabilmektedir. Bu nedenle veri gönderimi yaparken 48+8 bit veri paketi HEX String formatında gönderilecektir.

```json
"ID": "70A11D1D01000026"
```

### “Hardware" : Donanım Versiyonu

Cihazın donanım tarafına ait tanımlayıcı versiyon bildirimidir. Majör ve minör versiyon yanı sıra (donanım versiyonu içerdiği modüllerde yer alan değişikliklere göre şekillenmektedir) üretim parti numarasını içermektedir. İlk 2 basamak **majör donanım versiyonu** sonraki 2 basamak ise **minör donanım versiyonu** bilgisini vermektedir. Son 2 basamak ise üretim parti numarasını içermektedir. Tüm bu versiyon yapısı GIT reposu üzerindeki release kodlarına aittir ve detayları repo üzerinde açıklanmıştır. XX.XX.XX yapısı şeklinde 8 byte string olarak gönderilmektedir (hep aynı uzunlukta).

```json
"Hardware": "03.00.00"
```

	Versiyon kodlama yapısı semantik kodlama sistemi üzerine kurgulanmıştır.

### “Firmware" : Yazılım Versiyonu

Cihazın firmware tarafına ait tanımlayıcı versiyon bildirimidir. Majör, minör ve hata düzeltme durumlarını içermektedir. İlk 2 basamak **majör yazılım versiyonu** sonraki 2 basamak ise **minör yazılım versiyonu** bilgisini vermektedir. Son 2 basamak ise hata düzeltme kod versiyonu bilgisini içermektedir.

```json
"Firmware": "03.00.00"
```

	Versiyon kodlama yapısı semantik kodlama sistemi üzerine kurgulanmıştır.

***

## 2. Power

Geliştirilen donanımların tamamı batarya destekli sistemler olarak tasarlanmaktadır. Herhangi bir güç kaynağına bağlı olarak çalışsa bile güç kesilmesi durumunda sunuculara veri gönderebilmek için yeterli enerjiye sahip olmaları gerekmektedir. Bu nedenle tüm ürünler üzerinde Li-Ion batarya (ürün cinsine göre adedi ve gücü değişmektedir bu bilgi donanım versiyonu içerisinde yer alacaktır) kullanılmaktadır.

Li-Ion bataryalar yapı gereği 3V8 nominal voltaj, 4V2 max voltaj ve 3V0 min voltaj olarak karakterize edilmektedir. Bu değerler teorik değerler olup ortam sıcaklığına göre değişmektedir. Düşük sıcaklıklar bir sorun değil bir avantajdır ve pil yaşlanmasını azaltır. Bununla beraber bataryaların 3V0 değerine düşmesi istenmeyen bir durumdur genellikle 3V2-3V4 aralığına düşmüş bataryalar boş olarak değerlendirilir.

Bu kapsamda donanımlar üzerinde batarya şarj ve batarya ölçümleme sistemleri bulunmaktadır. Bu sistemler üzerinden alınan veriler hem anlık hem de ileri vade sürdürülebilirlik analizleri için kaydedilmelidir.

Bu segment içerisinde cihaza ait güç parametreleri yer alamaktadır. Batarya durumu şarj bilgileri gibi parametreler bu alan içerisinde yer almaktadır. 

```json
"Power": {
    "Battery": {
        "AC": -0.15,
        "FB": 2000,
        "IB": 1300,
        "IV": 4.17,
        "SOC": 92.13,
        "T": 23.12,
        "Charge": 3
    }
}
```

### “Battery"

Sistem içerisinde kullanılmakta olan bataryaların anlık olarak takip edilmesi hem güvenlik hemde sürdürülebilirlik açısından önem teşkil etmektedir. Bu nedenle sistem içerisine MAX17055 batarya ölçüm sistematiği kurgulanmıştır. Bu sayede birçok batarya parametresini ölçümleyebilmekteyiz. Bu veri paketi içersinde analiz için gerekli önemli parametreler gönderilmektedir.

#### "AC" : Ortalama Akım Tüketimi

|                 | Açıklama                                        |
|-----------------|-------------------------------------------------|
| Değişken Adı    | AC                                              |
| Değişken Tanımı | **A**verage **C**urrent (Ortalama Akım)         |
| Değişken Tipi   | Float                                           |
| Değişlen Birimi | mA                                              |
| Örnek Veri      | -51.72                                          |

Sistem güç katmanı üzerinde bulunan MAX17055 batarya ölçümleme çipi üzerinden ölçülen ortalama akım bilgisidir. Batarya ölçüm çipinin kullanılmasında ki birincil öncelik bu veridir (IV ile birlikte). Çip bataryaya bağlı kaldığı süre boyunca ölçümleme yapar ve bu verilerin ortalamalarını iç registerlarında tutar. Bu verinin negatif değer olması tüketim olduğunu (bataryadan güç çekimi), pozitif olması ise şarj olduğunu belirtmektedir (bataryaya doğru güç). Sonraki versiyonlarda akım değeri üzerinden güç analizleri ve batarya sağlığı konusunda analizler yapılabilecektir.

#### "FB" : Tam Dolu Batarya Kapasitesi

|                 | Açıklama                                        |
|-----------------|-------------------------------------------------|
| Değişken Adı    | FB                                              |
| Değişken Tanımı | **F**ull **B**attery (Tam Dolu Kapasite)        |
| Değişken Tipi   | int                                             |
| Değişlen Birimi | mAh                                             |
| Örnek Veri      | 718                                             |

Sistem güç katmanı üzerinde bulunan MAX17055 batarya ölçümleme çipi üzerinden ölçülen batarya tam dolu kapasite bilgisidir. Bu kapasite bilgisi mAh birimi üzerinden batarya döngüsüne göre anlık olarak hesaplanmaktadır. Herhangi bir harici kaynaktan set edilmemektedir. SOC değeri üzerinden bu veri değeri çarpılarak toplam kapasite bilgisine ulaşılabilmektedir bu nedenle FB değeri gönderilmemiştir.

#### "IB" : Anlık Batarya Kapasitesi

|                 | Açıklama                                        |
|-----------------|-------------------------------------------------|
| Değişken Adı    | IB                                              |
| Değişken Tanımı | **I**nstant **B**attery (Anlık Kapasite)        |
| Değişken Tipi   | int                                             |
| Değişlen Birimi | mAh                                             |
| Örnek Veri      | 718                                             |

Sistem güç katmanı üzerinde bulunan MAX17055 batarya ölçümleme çipi üzerinden ölçülen batarya anlık kapasite bilgisidir. Bu kapasite bilgisi mAh birimi üzerinden batarya döngüsüne göre anlık olarak hesaplanmaktadır. Herhangi bir harici kaynaktan set edilmemektedir. SOC değeri üzerinden bu veri değeri çarpılarak toplam kapasite bilgisine ulaşılabilmektedir bu nedenle FB değeri gönderilmemiştir.

#### "IV" : Anlık Batarya Voltajı

|                 | Açıklama                                        |
|-----------------|-------------------------------------------------|
| Değişken Adı    | IV                                              |
| Değişken Tanımı | **I**nstant **V**oltage (Anlık batarya voltajı) |
| Değişken Tipi   | Float                                           |
| Değişlen Birimi | Volt                                            |
| Örnek Veri      | 3.89                                            |

Sistem kurulu bataryasına ait anlık voltaj bilgilerini vermektedir. Sonraki versiyonlarda voltaj değeri üzerinden güç analizleri ve batarya sağlığı konusunda analizler yapılabilecektir. Kullanılan batarya voltaj alt ve üst limitleri kayıt sırasında kontrol edilebilir.

#### "SOC" : Anlık Batarya Doluluk Oranı

|                 | Açıklama                                        |
|-----------------|-------------------------------------------------|
| Değişken Adı    | SOC                                             |
| Değişken Tanımı | **S**tate **o**f **C**harge (Kapasite yüzdesi)  |
| Değişken Tipi   | Float                                           |
| Değişlen Birimi | %                                               |
| Örnek Veri      | 17.97                                           |

Sistem güç katmanı üzerinde bulunan MAX17055 batarya ölçümleme çipi üzerinden ölçülen batarya doluluk oranı bilgisidir. Batarya paketinin firmware üzerinde ayarlanmış kapasitesi ile anlık olarak ölçümlenen batarya kapasite oranı olarak hesaplanmaktadı. Bu hesap için batarya karakteristik eğrileri kullanılmakta ve lineer olmayan bir hesap ölçüm çipi tarafından anlık olarak yapılmaktadır.

Bu değer UI tasarımlar içerisinde batarya durum bilgisi olarak direkt paylaşılabilir yapıdadır.

    Batarya SOC verisinin tam doğru parametreyi gösterebilmesi için en az bir defa tam deşarj-şarj döngüsü
    tamamlamış olması gerekmektedir. Bu nedenle ilk gelen veriler hatalı olabilir.

#### "T" : Çip Sıcaklığı

|                 | Açıklama                                        |
|-----------------|-------------------------------------------------|
| Değişken Adı    | T                                               |
| Değişken Tanımı | **T**emperature (Anlık Çip Sıcaklığı)           |
| Değişken Tipi   | Float                                           |
| Değişlen Birimi | Santigrat                                       |
| Örnek Veri      | 25.43                                           |

Sistem güç katmanı üzerinde bulunan MAX17055 batarya ölçümleme çipi üzerinden ölçülen kart sıcaklığıdır. Sonraki versiyonlarda sıcaklık değeri üzerinden güç analizleri ve batarya sağlığı konusunda analizler yapılabilecektir.

#### "Charge" : Şarj Durumu

|                 | Açıklama                                        |
|-----------------|-------------------------------------------------|
| Değişken Adı    | Charge                                          |
| Değişken Tanımı | **Charge**r Status (Şarj durumu)                |
| Değişken Tipi   | int                                             |
| Değişlen Birimi | -                                               |
| Örnek Veri      | 2 (0-3)                                         |

BQ24298 şarj entegresi şarj durumlarını tanımlayan register değerine sahiptir. Bu register değeri işlemci tafaından okunarak veri paketi ile birlikte sunuculara kaydedilmektedir. Bu sayede şarj durumu ile güç kaynaklı arıza durumları tesbit edilebilir hale getirilmiştir. Bu register değerlerinin neleri ifade ettiği aşağıdaki tabloda belirtilmiştir.

| Status ID | Durum           | Açıklama                                  |
|-----------|-----------------|-------------------------------------------|
| 0         | Not Charging    | Şarj olmuyor                              |
| 1         | Precharge       | Ön şarj oluyor                            |
| 2         | Fast Charge     | Hızlı şarj oluyor                         |
| 3         | Charge Done     | Şarj tamamlandı                           |

Bu veri alanı gerekli durumlarda UI üzerinde direkt olarak gösterilebilecektir (örneğin şarj oluyor ikonu).

***

## 3. IoT

Geliştirilen cihazların tamamı etkileşimli IoT cihazlar olarak tanımlanmaktadır. Bu nedenle veri paketi içerisinde iletişim alt parametrelerinin olduğu bir alan ihtiyacı doğmuştur.

IoT iletişim bloğuna ait cihaz tarafından gönderilen veri paketi aşağıdaki yapıdadır.

```json
"IoT": {
    "GSM": {
        "Module": {
            "Firmware": "13.00.007",
            "IMEI": "353613080341871",
            "Manufacturer": 1,
            "Model": 1,
            "Serial": "0001767743"
        },
        "Operator": {
            "Iccid": "8990011916180288985",
            "Code": 28601,
            "RSSI": 10,
            "ConnTime": 22
        }
    }
}
```

### GSM

Cihazlarımız Telit firmasının üretmekte olduğu 2G altyapısına sahip haberleşme imkanı sunan GE910QUAD modemini barındırmaktadır. 2G şebeke kullanan en stabil modem olması nedeniyle bu model seçilmiştir ve 3G,LTE,5G bantlarını destekleyen xE910 ailesinin bir ürünüdür. Footprint değişikliği olmadan sadece modül değiştirerek bant seçimi yapılabilmektedir.

    Yeni nesi cihazlarda farklı modemler kullanılabilecektir.

#### Module

Bu veri alanı GSM modeme ait fiziksel özellik değerlerini içermektedir.

##### "Firmware" : GSM Modül Firmware

GSM IoT iletişime ait modül içerisinde çalışmakta olan embeded firmware versiyon bilgisidir. Majör, minör ve hata düzeltme durumlarını içermektedir. İlk 2 basamak **majör yazılım versiyonu** sonraki 2 basamak ise **minör yazılım versiyonu** bilgisini vermektedir. Son 3 basamak ise hata düzeltme kod versiyonu bilgisini içermektedir.

|                 | Açıklama                                             |
|-----------------|------------------------------------------------------|
| Değişken Adı    | Firmware                                             |
| Değişken Tanımı | GSM **Firmware** (GE910 firmware versiyonu)          |
| Değişken Tipi   | String (9 Byte)                                      |
| Değişlen Birimi | -                                                    |
| Örnek Veri      | 13.00.007                                            |

##### "IMEI" : GSM Modül IMEI Numarası

GSM Modemleri fiziksel olarak kayıt altına alabilmek ve devlet regülasyonuları için anahtar oluşturması için her GSM modemde olması gereken tekil 15 byte bir veridir. Bu id sayesinde modem satınalma parti vs gibi bilgiler takip edilebilmektedir.

|                 | Açıklama                                             |
|-----------------|------------------------------------------------------|
| Değişken Adı    | IMEI                                                 |
| Değişken Tanımı | GSM Modem **IMEI** Number (IMEI)                     |
| Değişken Tipi   | String (15 Byte)                                     |
| Değişlen Birimi | -                                                    |
| Örnek Veri      | 353613080341053                                      |

##### "Manufacturer" : GSM Modül Üretici Kodu

GSM Modem üretici bilgisi.

|                 | Açıklama                       |
|-----------------|--------------------------------|
| Değişken Adı    | Manufacturer                   |
| Değişken Tanımı | GSM Modem **Manufacturer**     |
| Değişken Tipi   | Integer                        |
| Değişlen Birimi | -                              |
| Örnek Veri      | 1                              |

Kullanmakta olduğumuz üretici bilgileri.

| ID | Manufacturer |
|----|--------------|
| 1  | Telit        |

##### "Model" : GSM Modül Model Kodu

GSM Modem model bilgisi.

|                 | Açıklama                       |
|-----------------|--------------------------------|
| Değişken Adı    | Model                          |
| Değişken Tanımı | GSM Modem **Model**            |
| Değişken Tipi   | Integer                        |
| Değişlen Birimi | -                              |
| Örnek Veri      | 1                              |

Kullanmakta olduğumuz model bilgileri.

| ID | Model        |
|----|--------------|
| 1  | GE910QUAD    |

##### "Serial" : GSM Modül Seri Numarası

GSM Modem seri numara bilgisi.

|                 | Açıklama                       |
|-----------------|--------------------------------|
| Değişken Adı    | Serial                         |
| Değişken Tanımı | GSM Modem **Serial Number**    |
| Değişken Tipi   | String                         |
| Değişlen Birimi | -                              |
| Örnek Veri      | 0000020273                     |

#### Operator

GSM IoT sistemler içerisinde bir diğer önemli kısımda bağlantı ve operatör değişkenleridir. Bu alan altında GSM modem ile SIM üzerinde belirtilen operatöre bağlantı yapıldıktan sonra elde edişen veriler yer almaktadır.

##### "ICCID" : SIM Kart ICCID Numarası

ICCID (Integrated Circuit Card Identifier) olarak bilinen kod numarası GSM şebekelerde telefon numarasının ve mobil operatör faturalandırma alt yapısı için kullanılan dünya genelinde tekil bir koddur. Sistemlerimiz içerisinde mobil operatör tarafında işlemlerin kolayca kontrol edilebilmesi amacı ile bu kod sistemlerimizde saklanacaktır.

|                 | Açıklama                                             |
|-----------------|------------------------------------------------------|
| Değişken Adı    | ICCID                                                |
| Değişken Tanımı | **I**ntegrated **C**ircuit **C**ard **I**dentifier   |
| Değişken Tipi   | String (19/20 byte)                                  |
| Değişlen Birimi | -                                                    |
| Örnek Veri      | 8990011901130266075                                  |

##### "Code" : Operatör Kodu

GSM in hangi operatöre bağlandığı bilgisidir. Her operatör için dünya genelinde hazırlanmış bir kod [listesi](https://www.mcc-mnc.com) mevcuttur. Türkiye için operatör listesi aşağıdaki gibidir.

|                 | Açıklama                                             |
|-----------------|------------------------------------------------------|
| Değişken Adı    | Code                                                 |
| Değişken Tanımı | Operator **Code** (Operatör kodu)                    |
| Değişken Tipi   | int                                                  |
| Değişlen Birimi | -                                                    |
| Örnek Veri      | 28601                                                |

| Operator Code | Operator Adı |
|---------------|--------------|
| 28601         | Turkcell     |
| 28602         | Vodafone     |
| 28603         | Turk Telekom |
| 28604         | Turk Telekom |

##### "RSSI" : Operatör Sinyal Gücü

|                 | Açıklama                                             |
|-----------------|------------------------------------------------------|
| Değişken Adı    | RSSI                                                 |
| Değişken Tanımı | **R**eceived **S**ignal **S**trength **I**ndicator (Sinyal gücü) |
| Değişken Tipi   | int                                                  |
| Değişlen Birimi | -                                                    |
| Örnek Veri      | 30                                                   |

Sistemi şebekeye bağlantı sinyal gücü hakkında bilgi vermektedir. dBm dönüşümü aşağıdaki şekilde yapılmaktadır.

| RSSI  | dBm           | Açıklama                |
|-------|---------------|-------------------------|
| 0     | <= -113       |                         |
| 1     | -111          |                         |
| 2..30 | -109 <-> -53  | Her 1 basamak için 2dBm |
| 31    | >= -51        |                         |
| 99    |               | Tesbit edilemedi        |

dBm için belirlenen sinyal çekim seviyesi 5 üzerinden aşağıdaki gibi hesaplanmaktadır (UI için çekim çubukları)

| dBm                  | Seviye     | Açıklama                                |
|----------------------|------------|-----------------------------------------|
| >= -70 dBm           | Mükemmel   | Güçlü sinyal ve maksimum veri hızı      |
| -70 dBm <-> -85 dBm  | Güzel      | Güçlü sinyal güçlü veri hızı            |
| -86 dBm <-> -100 dBm | İyi        | Zayıf sinyal fakat kullanışlı veri hızı |
| < -100 dBm           | Zayıf      | Zayıf sinyal problemli veri hızı        |
| -110 dBm             | Kötü       | Kötü bağlantı kopma yaşanabilir         |

##### "ConnTime" : Operatör Bağlantı Zamanı

GSM IoT sistemler öncelikle şebeke bağlantısı kurar ve daha sonra 2G alt yapısı üzerine kendisini kaydettirir. Bu iki işlem için gerekli olan süre Bağlanabilme süresi olarak tanımlanır ve operatörün bölgedeki gücünün ölçümünde kullanılır. Bu nedenle büyük ölçekte şebeke haritası çıkartabilmek için bu veri sunuculara gönderilmektedir.

|                 | Açıklama                                             |
|-----------------|------------------------------------------------------|
| Değişken Adı    | ConnTime                                             |
| Değişken Tanımı | **Conn**ection **Time** (Bağlanma Süresi)            |
| Değişken Tipi   | int                                                  |
| Değişlen Birimi | Saniye                                               |
| Örnek Veri      | 32                                                   |

##### "LAC" : Operatör Verici Lokasyon Tanımlayıcısı

GSM IoT sistemler sahada yer alan verici ile iletişime geçer ve kendini kaydettirir. Bu vericiye ait unique baz istasyon kodu yer almaktadır. Cihaz içerisinde GPS bulunmasından bağımsız şekilde bu verici kodu sunucuya gönderilmektedir.

|                 | Açıklama                                             |
|-----------------|------------------------------------------------------|
| Değişken Adı    | LAC                                                  |
| Değişken Tanımı | **L**ocation **A**rea **C**ode                       |
| Değişken Tipi   | String (4 byte HEX)                                  |
| Değişlen Birimi | -                                                    |
| Örnek Veri      | 855E                                                 |

##### "Cell_ID" : Operatör Verici Lokasyon Tanımlayıcısı

GSM IoT sistemler sahada yer alan verici ile iletişime geçer ve kendini kaydettirir. Bu vericiye ait unique baz istasyon kodu yer almaktadır. Cihaz içerisinde GPS bulunmasından bağımsız şekilde bu verici kodu sunucuya gönderilmektedir.

|                 | Açıklama                                             |
|-----------------|------------------------------------------------------|
| Değişken Adı    | Cell_ID                                              |
| Değişken Tanımı | Operatör Baz İstasyonu Kodu                          |
| Değişken Tipi   | String (4 byte HEX)                                  |
| Değişlen Birimi | -                                                    |
| Örnek Veri      | BFAB                                                 |

***