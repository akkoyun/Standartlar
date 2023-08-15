# PostBox - Veri İletişim Protokolü [01.02.00]

"STF Tarım" için **Temmuz 2022** ve sonrası geliştirilmekte olan tüm IoT cihazları için kullanılacak olan veri iletişim yapısı ve teknik detayları bu doküman içerisinde tanımlanmıştır. Diğer tüm **STF** projeleri ile birlikte yapılan planlama doğrultusunda tüm cihazların tek bir **EndPoint** üzerinden çalışması uygun görülmüştür. End point üzerinden hangi cihazın hangi şartlarda veri göndereceği ve backend üzerinden bu ayrımın nasıl yapılması gerektiği bu düküman üzerinden tanımlanmıştır.

## 1. - Cihaz Veri Gönderim ve IoT Bağlantı Yapısı

Geliştirilmekte olan cihazlar bağantı ve veri gönderim yapısı itibari ile değişiklikler göstermektedir. Bazı cihazlarımız elektrik bağlantılı çalışmaktadır ve bu tip cihazlarımız proje doğrultusunda GSM üzerinden sürekli bağlı kalmaktadır. Bunun yanı sıra bazı cihazlarımız da batarya destekli olarak çalışmaktadır bu nedenle uyu-uyan-uyu yapısında veri gönderimi yapmaktadır. Devamlı uyanık olan sistemlerimiz sunucu üzerinden komut alabilir yapıdadır. Uyu-uyan-uyu sistemlerimiz ise tek yönlü veri gönderim yapısına sahiptir.

Bu sistematik ve cihaz özelliği doğrultusunda veri paketi içerisinde yer alan payload segmenti değişiklik gösterebilecektir. Bu nedenle **device** segmenti içerisinde bir komut tanımı yer almaktadır. Bu komut tanımına göre payload segmenti yapısı ilgili bölümde detaylıca anlatılacaktır.

### 1.A. - WeatherStat Veri Gönderim Yapısı

Tarımsal meteoroloji sistemi kurgu gereği tek yönlü veri trafiğiğine sahip bir sistemdir. Bu kurgu bünyesinde aşağıdaki koşullarda IoT veri transferi yapılacaktır. WeatherStat (P101) sistemi uyuyan uyanan bir donanım kurgusuna sahiptir. Bu kurgu gereği sistem donanım olarak belirlenen süre periodlarında (30 dk da bir) uyanarak veri paketi hazırlayacak ve sunucuya veri gönderimi yapacaktır.

* Cihaz güç altyapısı : Batarya (solar şarjlı)
* Cihaz çalışma sistemi : Uyu-Uyan
* İletişim : Tek yönlü (cihaz --> sunucu)

### 1.B. - PowerStat Veri Gönderim Yapısı

PowerStat sistemi kurgu gereği elektrik panosu üzerine montajlanmaktadır. Bu nedenle güç sorunu bulunmamaktadır. Elektrik olduğu sürece kendisini GSM şebekesine bağlı tutacak elektrik gitmesi durumunda ise elektriğin gittiğini haber ederek GSM i kapatıp uyku moduna geçecektir. Cihaz bağlı durumdayken belirlenen veri tipleri ile gönderim yapacak ve sunucudan veri alabilecektir.

* Cihaz güç altyapısı : Batarya (220V şarjlı)
* Cihaz çalışma sistemi : Devamlı uyanım (enerji varken)
* İletişim : Çift yönlü (cihaz <--> sunucu)

### 1.C. - FilterStat Veri Gönderim Yapısı

...

## 2. - Veri Paketi Yapısı

Tüm projeler ortak bir veri iletişim altyapısı içerisinde birleştirilmiş ve ortak bir iletişim standardı belirlenmiştir. Bu standart doğrultusunda veri paketi aşağıda tanımlandığı şekilde gönderilecektir.

    Örnek Veri Paketi (WeatherStat)

```json
{
    "Command": "STF:WeatherStat.Timed",
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
                    "ConnTime": 22
                }
            }
        }
    },
    "Payload": {
        "TimeStamp": "2022-03-23  14:18:28",
        "WeatherStat": {
            "Location": {
                "Latitude": 47.407614681869745,
                "Longitude": 8.553115781396627
            },
            "Environment": {
                "AT": 22.223,
                "AH": 22.222,
                "AP": 222.22,
                "UV": 3,
                "ST": [
                    22.22,
                    0,
                    0,
                    22.11
                ],
                "R": 22,
                "WD": 329,
                "WS": 22.33
            }
        }
    }
}
```

| Segment | Açıklama                                                                              | Detaylar                                         |
|---------|:--------------------------------------------------------------------------------------|--------------------------------------------------|
| Command | Paketin hangi cihaza ait komut için gönderildiğini tanımlayan komut parametresi.      | [Segment yapısı ve detayları](Command/Readme.md) |
| Device  | Cihaza ait tanımlayıcı bilgilerin yer aldığı segment (tüm cihazlar için aynı yapı).   | [Segment yapısı ve detayları](Device/Readme.md)  |
| Payload | Veri paketine ait ana verinin yer aldığı segment (herbir command için farklı yapıda). | [Segment yapısı ve detayları](Payload/Readme.md) |

## 3. - Cevap Paketi Yapısı

Tüm IoT cihazlarımız sistemi yapı gereği sunuculara veri gönderimi yaptıktan sonra cevap için beklemede kalır. Sunucu tarafından verinin uygun şekilde yakalandığını belirten ibare gelmesi durumunda sistem rutin işlemine devam eder (uyuyan cihazlar tekrar uyku moduna döner). Eğerki onay mesajı gelmemesi durumunda veri kaydını tekrar gönderir (5 deneme yapar ve hala kayıt olmadı ise uyur). Bu nedenle gönderilen veri paketine karşılık olarak aşağıdaki yapıda bir cevap sunucu tarafından dönecektir.

```JSON
"Event": 200
```

Event değişkeni içerisinde gönderilecek olan kod numaraları HTTP Header tanımları ile aynıdır (aşağıda belirtilmiştir). Bu kod numaraları artabilir olduğu ve duruma göre ekleme yapılabileceği unutulmamalıdır (tabloda belirtilen kodlar sabittir).

| Result  | Açıklama                                    |
|---------|---------------------------------------------|
| 200     | Status Ok : Veri düzgün şekilde kaydedildi. |
