# "Command" Ana Segment Tanımı

Hangi cihazın (projenin) hangi işlemi yapması için veri gönderdiğini tanımlayan komut açıklamasıdır. 

```json
"Command": "STF:WeatherStat.Timed"
```

Paket komut satırı aşağıdaki yapıda kurgulanmıştır.

| Bölüm | Açıklama                         | Örnek Veri  |
|-------|----------------------------------|-------------|
| Firma | Veri Paketinin Sahibi Firma Kodu | STF         |
| Proje | Veri Paketi Proje Adı            | WeatherStat |
| Komut | Veri Paketi Komut                | Save        |

***

## Proje ve Komut Listesi

Geliştirmekte olduğumuz IoT sistemler birden fazla projeyi kapsamaktadır. Proje özelinde **Payload** paketi değişkenlik göstermektedir. Bu değişiklikleri veri paketinin ilk satırında **Command** parametresi ile tanımlamaktayız. Bu komut seti ve projeye göre veri gönderim nedenleri, içerikleri ve detayları aşağıda tanımlanmıştır.

***

### WeatherStat [P101]

| Komut Adı   | Gönderim Nedeni                         |
|-------------|-----------------------------------------|
| [Timed](/Veri%20%C4%B0leti%C5%9Fim%20Yap%C4%B1s%C4%B1/WeatherStat/Timed.json) | Sistem nominal şartlarda uyku modunda durur. Sistem herhangi bir dış uyandırma olmaksızın sistem içerisinde yer alan zamanlayıcı ile uyanıp veri gönderimi yapar (varsayılan olarak 30dk aralıklarla). Bu zamanlı uyanma ve veri gönderimi sistem iletişim maliyetlerini azaltmak ve sunucu yükünü hafifletmek adına full ve tiny adı altında 2 farklı pakette yapılır. Eğer sistem zamanı 12:00 - 12:59 aralığında ise sistem güncellemesi yapabilmek için full paket gönderilir. Zamanlı full gönderim sunucuya **Timed** komutu ile gönderilir.|
| [Timed_Tiny](/Veri%20%C4%B0leti%C5%9Fim%20Yap%C4%B1s%C4%B1/WeatherStat/Timed_Tiny.json) | Sistem nominal şartlarda uyku modunda durur. Sistem herhangi bir dış uyandırma olmaksızın sistem içerisinde yer alan zamanlayıcı ile uyanıp veri gönderimi yapar (varsayılan olarak 30dk aralıklarla). Bu zamanlı uyanma ve veri gönderimi sistem iletişim maliyetlerini azaltmak ve sunucu yükünü hafifletmek adına full ve tiny adı altında 2 farklı pakette yapılır. Eğer sistem zamanı 12:00 - 12:59 aralığı dışında ise tiny paket gönderilir. Zamanlı tiny gönderim sunucuya **Timed_Tiny** komutu ile gönderilir. |

* Veri paketleri cinsine göre paket içeriğini [ilgili sayfadan](/Veri%20%C4%B0leti%C5%9Fim%20Yap%C4%B1s%C4%B1/WeatherStat/Commands.md) incleyebilirsiniz.

***

### PowerStat [P401]

| Komut Adı | Açıklama                           |
|-----------|------------------------------------|
| [Online](/Veri%20%C4%B0leti%C5%9Fim%20Yap%C4%B1s%C4%B1/PowerStat/Online.json) | Sistem anlık olarak girdi kanallarını taramaktadır. Bu tarama sonucunda sistemde R fazı geldi ise (elektrik geldi ise) sistem otomatik olarak GSM üzerinden internete bağlanır ve cihazı online moda geçirir. Bu mod değişikliğini sunucuya kaydettirir.|
| [Timed](/Veri%20%C4%B0leti%C5%9Fim%20Yap%C4%B1s%C4%B1/PowerStat/Timed.json) | Sistem içerisinde bulunan RTC (saat) online prosedürü sırasında kendisini zaman sunucuları üzerinden senkronize eder ve anlık doğru zaman parametrelerini alır. Ardından pompa durumuna göre zamanlı veri atmak üzere RTC üzerinden alarm  kurar. Sistem varsayılan değerleri olarak pompa çalışıyorken 10dk, pompa duruyorken 30dk zaman aralıkları ile sunucuya veri güncellemesi gönderir. Bu zamanlı gönderimler **Timed** komutu ile sunucuya gönderilir.|
| [Interrupt](/Veri%20%C4%B0leti%C5%9Fim%20Yap%C4%B1s%C4%B1/PowerStat/Interrupt.json) | Sistem anlık olarak girdi kanallarını taramaktadır. Bu tarama sonucunda sistem girdilerinde herhangi bir değişiklik olur ise ve sistem firmware bünyesindeki yapay zeka modülü bu değişikliği bir bildirim olarak etiketler ise sistem sunucuya işlem kaydı oluştururu. Bu işlem kaydı **Interrupt** komutu ile sunucuya gönderilir.|
| [Alarm](/Veri%20%C4%B0leti%C5%9Fim%20Yap%C4%B1s%C4%B1/PowerStat/Alarm.json) | Sistem içerisinde girdi parametreleri yanı sıra enerji ve basınç parametrelerini de anlık takip eder (sistem online yani pompa çalışıyorken). Bu takip sonrasında bir hata yada bildirim kodu oluşur ise (enerji limit değişimi, basınç yükselmesi düşmesi vs gibi) sistem sunucuya işlem kaydı oluştururu. Bu işlem kaydı **Alarm** komutu ile sunucuya gönderilir.|
| [Offline](/Veri%20%C4%B0leti%C5%9Fim%20Yap%C4%B1s%C4%B1/PowerStat/Offline.json) | Sistem anlık olarak girdi kanallarını taramaktadır. Bu tarama sonucunda sistemde R fazı gider ise (elektrik gitmesi durumunda) sistem otomatik olarak sunucuya enerji gitti bildirimi yapar ve internet bağlantısını keser. Bu mod değişikliği sunucuya **Offline** komutu ile gönderilir.|

* Veri paketleri cinsine göre paket içeriğini [ilgili sayfadan](/Veri%20%C4%B0leti%C5%9Fim%20Yap%C4%B1s%C4%B1/PowerStat/Commands.md) incleyebilirsiniz.

***

### FilterStat [P511]

| Komut Adı | Açıklama                           |
|-----------|------------------------------------|
| Online    |                                    |
| Clean     |                                    |
| Offline   |                                    |
***