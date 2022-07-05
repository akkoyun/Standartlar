# 2.1. "Command" Ana Segment Tanımı

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

### WeatherStat

| Komut Adı | Açıklama                           |
|-----------|------------------------------------|
| Online    |                                    |
| Timed     |                                    |
| Interrupt |                                    |
| Offline   |                                    |

### WeatherStat

| Komut Adı   | Açıklama                                      | Gönderim Nedeni                         |
|-------------|-----------------------------------------------|-----------------------------------------|
| Manual      | Manual uyandırma ile tam veri gönderimi       | Manual gönderim butonuna basılırsa      |
| Timed       | Zamanlı uyanma ile tam veri gönderimi         | Her 30 dk da bir (saat 12:xx de)        |
| Timed_Tiny  | Zamanlı uyanma ile kısaltılmış veri gönderimi | Her 30 dk da bir (geri kalan saatlerde) |

* Veri paketleri cinsine göre paket içeriğini [ilgili sayfadan](/Veri%20%C4%B0leti%C5%9Fim%20Yap%C4%B1s%C4%B1/WeatherStat/Commands.md) incleyebilirsiniz.