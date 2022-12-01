# "WeatherStat" Veri Paketi 

WeatherStat projesine ait veri paketi bloğudur. Command alanında belirlenen komuta özel yapıda olacaktır. Meteoroloji istasyonuna ait veri paketleri ve hangi komutta hangi verisetinin gönderileceği bilgisi [ilgili linkte](Commands.md) tanımlanmıştır.

```json
"Payload": {
    "TimeStamp": "2022-03-23  14:18:28",
    "WeatherStat": {
        "Location": {
            "Latitude": 47.407614681869745,
            "Longitude": 8.553115781396627
        },
        "Environment": {
            "AT": 22.223,   // Air Temperature
            "AH": 22.222,   // Relative Humidity
            "AP": 222.22,   // Air Preassure
            "UV": 3,        // UV Index
            "ST": [         // Soil Temperature
                22.22,      // 10cm
                0,          // 20cm
                22.11       // 30cm
                0,          // 40cm
                0,          // 50cm
                22.11       // 60cm
                0,          // 70cm
                0,          // 80cm
                22.11       // 90cm
                0           // 100cm
            ],
            "R": 22,        // Rain
            "WD": 329,      // Wind Direction
            "WS": 22.33     // Wind Speed
        }
    }
}
```

***

## "Location" Konum Bilgisi

WeatherStat projesi saha üzerinde yer alan konumunu takip etmek amacı ile GPS alıcısı bulundurmaktadır. Bu konum bilgileri Latitude ve Longtitude konumu altında verilmektedir.

***

### "Latitude" : Cihaz Enlem Bilgisi

Cihazlarımız üzerinde anlık konum bilgisi alabilmek adına GPS sensörü bulunmaktadır. Bu GPS sensörü üzerinden günün belirlenen saatleri içerisinde (cihaz konumunın sürekli değişmemesi ve güç tüketiminin gündüz gün ışığı ile karşılanması planlanarak her gün öğle saatlerinde 12-14 saatleri arasında gönderilecektir) gönderilecek olan enlem bilgisidir. 

Bir noktanın enlemi, ekvator düzleminin bu noktayı Dünya'nın merkezine bağlayan doğru ile oluşturduğu açının ölçüsüdür. Yapısal olarak -90° ile 90° arasında oluşur. Negatif değerler güney yarım küre konumları içindir ve ekvatorda enlem 0 ° değerindedir.

***

### "Longtituude" : Cihaz Boylam Bilgisi

Cihazlarımız üzerinde anlık konum bilgisi alabilmek adına GPS sensörü bulunmaktadır. Bu GPS sensörü üzerinden günün belirlenen saatleri içerisinde (cihaz konumunın sürekli değişmemesi ve güç tüketiminin gündüz gün ışığı ile karşılanması planlanarak her gün öğle saatlerinde 12-14 saatleri arasında gönderilecektir) gönderilecek olan boylam bilgisidir. 

Enlem için ekvator gibi doğal bir referans olmaması farkıyla, prensip boylam için aynıdır. Boylam referansı Greenwich Meridian'da keyfi olarak ayarlanmıştır (Londra'nın banliyölerinde Greenwich'teki Royal Greenwich Gözlemevi'nden geçer) ve bir noktanın boylamı, ekseni tarafından oluşturulan yarım düzlemin oluşturduğu açının ölçümüdür. yer ve Greenwich meridyeninden ve dünyanın ekseninin oluşturduğu ve noktadan geçen yarım düzlemden geçer.

***

## "Environment" : Cihaz Sensör Ölçüm Bilgisi

WeatherStat projesi meteoroloji istasyonu olduğu için ölçümlenen verilerde çevresel (environment) verilerdir ve data paketi bu segment içerisindedir. Diğer projelerde bu alan değişebilecektir.

### "AT" : Hava Sıcaklığı Verisi

|                 | Açıklama       |
|-----------------|----------------|
| Değişken Adı    | AT             |
| Değişken Tanımı | Hava Sıcaklığı |
| Değişken Tipi   | Float          |
| Değişlen Birimi | Derece         |
| Örnek Veri      | 22.22          |
| Zorunlu Veri    | Hayır          |

Sistemin T (hava sıcaklığı) sensörüne ait kalibre sıcaklık değeridir. Eğer sistemde donanımsal bir arıza mevcut ise bu veri tipi -1xx olarak gönderilmektedir. Bu veri tipleri daha sonra tanımlanacaktır.

### "AH" : Bağıl Nem Verisi

|                 | Açıklama       |
|-----------------|----------------|
| Değişken Adı    | AH             |
| Değişken Tanımı | Bağıl Nem      |
| Değişken Tipi   | Float          |
| Değişlen Birimi | %              |
| Örnek Veri      | 22.22          |
| Zorunlu Veri    | Hayır          |

Sistemin TH (hava bağıl nem) sensörüne ait kalibre bağıl nem değeridir. Eğer sistemde donanımsal bir arıza mevcut ise bu veri tipi -1xx olarak gönderilmektedir. Bu veri tipleri daha sonra tanımlanacaktır.

### "AP" : Hava Basıncı Verisi

|                 | Açıklama       |
|-----------------|----------------|
| Değişken Adı    | AP             |
| Değişken Tanımı | Hava Basıncı   |
| Değişken Tipi   | Float          |
| Değişlen Birimi | mBar           |
| Örnek Veri      | 222.22         |
| Zorunlu Veri    | Hayır          |

Sistemin P sensörüne ait kalibre hava basıncı değeridir. Eğer sistemde donanımsal bir arıza mevcut ise bu veri tipi -1xx olarak gönderilmektedir. Bu veri tipleri daha sonra tanımlanacaktır.

### "UV" : Güneş UV Şiddeti Verisi

|                 | Açıklama       |
|-----------------|----------------|
| Değişken Adı    | UV             |
| Değişken Tanımı | UV Indisi      |
| Değişken Tipi   | Integer        |
| Değişlen Birimi | -              |
| Örnek Veri      | 1              |
| Zorunlu Veri    | Hayır          |

Sistemin UV sensörüne ait kalibre UV indisi değeridir. Eğer sistemde donanımsal bir arıza mevcut ise bu veri tipi -1xx olarak gönderilmektedir. Bu veri tipleri daha sonra tanımlanacaktır.

### "ST" : Kademeli Toprak Sıcaklığı Verisi

|                 | Açıklama         |
|-----------------|------------------|
| Değişken Adı    | ST               |
| Değişken Tanımı | Toprak Sıcaklığı |
| Değişken Tipi   | Float (Array)    |
| Değişlen Birimi | Derece           |
| Örnek Veri      | 22.22            |
| Zorunlu Veri    | Hayır            |

Sistemin ST sensörüne ait kalibre toprak sıcaklığı değeridir. İleri versiyonlarda birden fazla katman sıcaklık verisi okuma ihtimaline karşı paket içerisinde array olarak gönderilmektedir. Bu array indisi değeri her bir derinliğe karşılık gelmektedir. Eğer sistemde donanımsal bir arıza mevcut ise bu veri tipi -1xx olarak gönderilmektedir. Bu veri tipleri daha sonra tanımlanacaktır.

Not: Son planlama sonrasında ST dizisini 4 kademe olacak şekilde sabitlendi. Fakat ileride yapılabilecek geliştirmeleri karşılayabilmek adına her bir derinliği sabitlemekteyiz.

| Değişken Adı | Sensör Derinliği | V1 Kullanımı       |
|--------------|------------------|--------------------|
| ST[0]        | 10 cm            | :white_check_mark: |
| ST[1]        | 20 cm            | :x:                |
| ST[2]        | 30 cm            | :white_check_mark: |
| ST[3]        | 40 cm            | :x:                |
| ST[4]        | 50 cm            | :x:                |
| ST[5]        | 60 cm            | :white_check_mark: |
| ST[6]        | 70 cm            | :x:                |
| ST[7]        | 80 cm            | :x:                |
| ST[8]        | 90 cm            | :white_check_mark: |
| ST[9]        | 100 cm           | :x:                |

```json
"ST": [
    22.22,  // 10cm
    0,      // 20cm
    22.11   // 30cm
    0,      // 40cm
    0,      // 50cm
    22.11   // 60cm
    0,      // 70cm
    0,      // 80cm
    22.11   // 90cm
    0       // 100cm
]
```

### "R" : Yağmur Kova Ölçüm Verisi

|                 | Açıklama          |
|-----------------|-------------------|
| Değişken Adı    | R                 |
| Değişken Tanımı | Yağmur Miktarı    |
| Değişken Tipi   | int               |
| Değişlen Birimi | mm (litre) / 30dk |
| Örnek Veri      | 222               |
| Zorunlu Veri    | Hayır             |

Sistemin R sensörüne ait yağmur şiddeti değeridir. Kovalı sistem yağmur sensörü için gönderilen bu değer bir hesap yöntemi ile hesaplanıp veritabanına hesaplanan değer kaydedilecektir. Eğer sistemde donanımsal bir arıza mevcut ise bu veri tipi -1xx olarak gönderilmektedir. Bu veri tipleri daha sonra tanımlanacaktır.

### "WD" : Rüzgar Yönü Verisi

|                 | Açıklama             |
|-----------------|----------------------|
| Değişken Adı    | WD                   |
| Değişken Tanımı | Rüzgar yönü          |
| Değişken Tipi   | int                  |
| Değişlen Birimi | Derece (kuzeye göre) |
| Örnek Veri      | 222                  |
| Zorunlu Veri    | Hayır                | 

Sistemin W sensörüne ait rüzgar yönü değeridir. Eğer sistemde donanımsal bir arıza mevcut ise bu veri tipi -1xx olarak gönderilmektedir. Bu veri tipleri daha sonra tanımlanacaktır.

### "WS" : Rüzgar Şiddeti Verisi

|                 | Açıklama             |
|-----------------|----------------------|
| Değişken Adı    | WS                   |
| Değişken Tanımı | Rüzgar şiddeti       |
| Değişken Tipi   | float                |
| Değişlen Birimi | m/sn                 |
| Örnek Veri      | 12.12                |
| Zorunlu Veri    | Hayır                | 

Sistemin W sensörüne ait rüzgar şiddeti değeridir. Eğer sistemde donanımsal bir arıza mevcut ise bu veri tipi -1xx olarak gönderilmektedir. Bu veri tipleri daha sonra tanımlanacaktır.