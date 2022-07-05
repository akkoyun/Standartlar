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

Bu segment içerisinde aşağıdaki alt segmentler yer almaktadır. Detaylara aşağıdaki linklerden ulaşabilirsiniz.

* [Info](Info/Readme.md)
* [Power](Power/Readme.md)
* [IoT](IoT/Readme.md)