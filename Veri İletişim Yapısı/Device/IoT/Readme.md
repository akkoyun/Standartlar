# 3. IoT

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
            "ConnTime": 22,
            "LAC": "855E",
            "Cell_ID": "BFAB"
        }
    }
}
```

## Tiny Paket İçeriği

İlgili komutun içeriğinde tanımlandığı şekilde gerek veri paketini küçültmek gerekse backend işlemlerini aza indirmek amacı ile bazı durumlarda aşağıdaki tabloda belirtildiği üzere bazı parametreler sunucuya gönderilmeyecektir.

| Değişlen Adı  | Normal Paket      | Tiny Paket        | 
|---------------|:-----------------:|:-----------------:|
| Module		|:white_check_mark:	|:x:				|
| Firmware		|:white_check_mark:	|:x:				|
| IMEI			|:white_check_mark:	|:x:				|
| Manufacturer	|:white_check_mark:	|:x:				|
| Model			|:white_check_mark:	|:x:				|
| Serial		|:white_check_mark:	|:x:				|
| Operator		|:white_check_mark:	|:white_check_mark:	|
| Iccid			|:white_check_mark:	|:x:				|
| Code			|:white_check_mark:	|:white_check_mark:	|
| RSSI			|:white_check_mark:	|:white_check_mark:	|
| ConnTime		|:white_check_mark:	|:white_check_mark:	|
| LAC			|:white_check_mark:	|:white_check_mark:	|
| Cell_ID		|:white_check_mark:	|:white_check_mark:	|

***

## GSM

Cihazlarımız Telit firmasının üretmekte olduğu 2G altyapısına sahip haberleşme imkanı sunan GE910QUAD modemini barındırmaktadır. 2G şebeke kullanan en stabil modem olması nedeniyle bu model seçilmiştir ve 3G,LTE,5G bantlarını destekleyen xE910 ailesinin bir ürünüdür. Footprint değişikliği olmadan sadece modül değiştirerek bant seçimi yapılabilmektedir.

    Yeni nesi cihazlarda farklı modemler kullanılabilecektir.

***

### Module

Bu veri alanı GSM modeme ait fiziksel özellik değerlerini içermektedir.

    # Bu veri "tiny" paketlerinde gönderilemyecektir.

***

#### "Firmware" : GSM Modül Firmware

GSM IoT iletişime ait modül içerisinde çalışmakta olan embeded firmware versiyon bilgisidir. Majör, minör ve hata düzeltme durumlarını içermektedir. İlk 2 basamak **majör yazılım versiyonu** sonraki 2 basamak ise **minör yazılım versiyonu** bilgisini vermektedir. Son 3 basamak ise hata düzeltme kod versiyonu bilgisini içermektedir.

|                 | Açıklama                                             |
|-----------------|------------------------------------------------------|
| Değişken Adı    | Firmware                                             |
| Değişken Tanımı | GSM **Firmware** (GE910 firmware versiyonu)          |
| Değişken Tipi   | String (9 Byte)                                      |
| Değişlen Birimi | -                                                    |
| Örnek Veri      | 13.00.007                                            |

    # Bu veri "tiny" paketlerinde gönderilemyecektir.

***

#### "IMEI" : GSM Modül IMEI Numarası

GSM Modemleri fiziksel olarak kayıt altına alabilmek ve devlet regülasyonuları için anahtar oluşturması için her GSM modemde olması gereken tekil 15 byte bir veridir. Bu id sayesinde modem satınalma parti vs gibi bilgiler takip edilebilmektedir.

|                 | Açıklama                                             |
|-----------------|------------------------------------------------------|
| Değişken Adı    | IMEI                                                 |
| Değişken Tanımı | GSM Modem **IMEI** Number (IMEI)                     |
| Değişken Tipi   | String (15 Byte)                                     |
| Değişlen Birimi | -                                                    |
| Örnek Veri      | 353613080341053                                      |

    # Bu veri "tiny" paketlerinde gönderilemyecektir.

***

#### "Manufacturer" : GSM Modül Üretici Kodu

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
| 0  | Unknown      |
| 1  | Telit        |
| 2  | Quectel      |
| 3  | Simcom       |


    # Bu veri "tiny" paketlerinde gönderilemyecektir.

***

#### "Model" : GSM Modül Model Kodu

GSM Modem model bilgisi.

|                 | Açıklama                       |
|-----------------|--------------------------------|
| Değişken Adı    | Model                          |
| Değişken Tanımı | GSM Modem **Model**            |
| Değişken Tipi   | Integer                        |
| Değişlen Birimi | -                              |
| Örnek Veri      | 1                              |

Kullanmakta olduğumuz model bilgileri.

| ID | Model          |
|----|----------------|
| 0  | Unknown        |
| 1  | GE910QUAD      |
| 2  | GE910QUAD-GNSS |
| 3  | LE910          |
| 4  | LE910S1-EAG    |


    # Bu veri "tiny" paketlerinde gönderilemyecektir.

***

#### "Serial" : GSM Modül Seri Numarası

GSM Modem seri numara bilgisi.

|                 | Açıklama                       |
|-----------------|--------------------------------|
| Değişken Adı    | Serial                         |
| Değişken Tanımı | GSM Modem **Serial Number**    |
| Değişken Tipi   | String                         |
| Değişlen Birimi | -                              |
| Örnek Veri      | 0000020273                     |

    # Bu veri "tiny" paketlerinde gönderilemyecektir.

***

### Operator

GSM IoT sistemler içerisinde bir diğer önemli kısımda bağlantı ve operatör değişkenleridir. Bu alan altında GSM modem ile SIM üzerinde belirtilen operatöre bağlantı yapıldıktan sonra elde edişen veriler yer almaktadır.

***

#### "ICCID" : SIM Kart ICCID Numarası

ICCID (Integrated Circuit Card Identifier) olarak bilinen kod numarası GSM şebekelerde telefon numarasının ve mobil operatör faturalandırma alt yapısı için kullanılan dünya genelinde tekil bir koddur. Sistemlerimiz içerisinde mobil operatör tarafında işlemlerin kolayca kontrol edilebilmesi amacı ile bu kod sistemlerimizde saklanacaktır.

|                 | Açıklama                                             |
|-----------------|------------------------------------------------------|
| Değişken Adı    | ICCID                                                |
| Değişken Tanımı | **I**ntegrated **C**ircuit **C**ard **I**dentifier   |
| Değişken Tipi   | String (19/20 byte)                                  |
| Değişlen Birimi | -                                                    |
| Örnek Veri      | 8990011901130266075                                  |

    # Bu veri "tiny" paketlerinde gönderilemyecektir.

***

#### "Code" : Operatör Kodu

GSM in hangi operatöre bağlandığı bilgisidir.

|                 | Açıklama                                             |
|-----------------|------------------------------------------------------|
| Değişken Adı    | Code                                                 |
| Değişken Tanımı | Operator **Code** (Operatör kodu)                    |
| Değişken Tipi   | int                                                  |
| Değişlen Birimi | -                                                    |
| Örnek Veri      | 28601                                                |

Operatör code bilgileri xxxyy yapısında 2 bileşenden oluşmaktadır. İlk 3 rakam (286) ülke kodunu son 2 rakam (01) ise operatör kodunu belirtmektedir. Yurt dışı projelerinde bu alan ülke konunumun belirlenmesinde faydalı olacaktır. Her operatör için dünya genelinde hazırlanmış bir kod [listesi](https://www.mcc-mnc.com) mevcuttur. Türkiye için operatör listesi aşağıdaki gibidir.

| Operator Code | Operator Adı |
|---------------|--------------|
| 28601         | Turkcell     |
| 28602         | Vodafone     |
| 28603         | Turk Telekom |
| 28604         | Turk Telekom |

***

#### "RSSI" : Operatör Sinyal Gücü 

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

dBm için belirlenen sinyal çekim seviyesi 5 üzerinden aşağıdaki gibi hesaplanmaktadır (UI için çekim çubukları) :signal_strength:

| dBm                  | Seviye     | Açıklama                                |
|----------------------|------------|-----------------------------------------|
| >= -70 dBm           | Mükemmel   | Güçlü sinyal ve maksimum veri hızı      |
| -70 dBm <-> -85 dBm  | Güzel      | Güçlü sinyal güçlü veri hızı            |
| -86 dBm <-> -100 dBm | İyi        | Zayıf sinyal fakat kullanışlı veri hızı |
| < -100 dBm           | Zayıf      | Zayıf sinyal problemli veri hızı        |
| -110 dBm             | Kötü       | Kötü bağlantı kopma yaşanabilir         |

***

#### "ConnTime" : Operatör Bağlantı Zamanı

GSM IoT sistemler öncelikle şebeke bağlantısı kurar ve daha sonra 2G alt yapısı üzerine kendisini kaydettirir. Bu iki işlem için gerekli olan süre Bağlanabilme süresi olarak tanımlanır ve operatörün bölgedeki gücünün ölçümünde kullanılır. Bu nedenle büyük ölçekte şebeke haritası çıkartabilmek için bu veri sunuculara gönderilmektedir.

|                 | Açıklama                                             |
|-----------------|------------------------------------------------------|
| Değişken Adı    | ConnTime                                             |
| Değişken Tanımı | **Conn**ection **Time** (Bağlanma Süresi)            |
| Değişken Tipi   | int                                                  |
| Değişlen Birimi | Saniye                                               |
| Örnek Veri      | 32                                                   |

***

#### "LAC" : Operatör Verici Lokasyon Tanımlayıcısı

GSM IoT sistemler sahada yer alan verici ile iletişime geçer ve kendini kaydettirir. Bu vericiye ait unique baz istasyon kodu yer almaktadır. Cihaz içerisinde GPS bulunmasından bağımsız şekilde bu verici kodu sunucuya gönderilmektedir.

"LAC" ve "Cell_ID" değişkenleri ile cihazın hangi GSM vericisine bağlı olduğu bilgisi [ilgili siteden](http://www.cell2gps.com) tesbit edilebilir. Bu sitede Türkiye için MCC:286, MNC:01 olarak alınacaktır.

|                 | Açıklama                                             |
|-----------------|------------------------------------------------------|
| Değişken Adı    | LAC                                                  |
| Değişken Tanımı | **L**ocation **A**rea **C**ode                       |
| Değişken Tipi   | String (4 byte HEX)                                  |
| Değişlen Birimi | -                                                    |
| Örnek Veri      | 855E                                                 |

***

#### "Cell_ID" : Operatör Verici Lokasyon Tanımlayıcısı

GSM IoT sistemler sahada yer alan verici ile iletişime geçer ve kendini kaydettirir. Bu vericiye ait unique baz istasyon kodu yer almaktadır. Cihaz içerisinde GPS bulunmasından bağımsız şekilde bu verici kodu sunucuya gönderilmektedir.

"LAC" ve "Cell_ID" değişkenleri ile cihazın hangi GSM vericisine bağlı olduğu bilgisi [ilgili siteden](http://www.cell2gps.com) tesbit edilebilir. Bu sitede Türkiye için MCC:286, MNC:01 olarak alınacaktır.

|                 | Açıklama                                             |
|-----------------|------------------------------------------------------|
| Değişken Adı    | Cell_ID                                              |
| Değişken Tanımı | Operatör Baz İstasyonu Kodu                          |
| Değişken Tipi   | String (4 byte HEX)                                  |
| Değişlen Birimi | -                                                    |
| Örnek Veri      | BFAB                                                 |

***