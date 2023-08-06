# "Payload" Ana Segment Tanımı

Sistemlerin ölçümlediği sensör datalarının tamamını içerisinde barından veri paketi bölümüdür. Bu paket içerisinde ölçüm zamanı yanı sıra ölçümleme nedeni ve veriler yer almaktadır. Tüm iletişim paketi içerisindeki veriler sisteme ait değerler barındırırken bu alan ölçüm yapılacak işleme ait veriler barındırmaktadır.

## 1. : "TimeStamp" Veri Paketi Zaman Etiketi

Veri paketinin oluşum zamana ait zaman etiketidir. Tüm payload verilerinde zorunlu olarak bulunacaktır.

|                 | Açıklama                                             |
|-----------------|------------------------------------------------------|
| Değişken Adı    | TimeStamp                                            |
| Değişken Tanımı | Veri ölçümleme zamanına ait zaman etiketi            |
| Değişken Tipi   | Date/Time                                            |
| Değişlen Birimi | -                                                    |
| Örnek Veri      | 2020-10-23  14:18:28                                 |

## 2. : Cihaz Veri Paketi

Cihaza özel oluşturulan veri paketi bloğudur. Proje ismine göre isimler ile adlandırılmaktadır.  Mevcut projeler için payload paketi ve içerik yapıları aşağıdaki listede verilmiştir.

| Proje Kodu | Proje Adı   | Payload Yapısı                             |
|------------|-------------|--------------------------------------------|
| P101       | WeatherStat | [Payload Yapısı](../WeatherStat/Readme.md) |
| P401       | PowerStat   | [Payload Yapısı](../PowerStat/Readme.md)   |
| P511       | FilterStat  | [Payload Yapısı](../)                      |
