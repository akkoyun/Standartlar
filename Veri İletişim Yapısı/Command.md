# 2.1. "Command" Ana Segment Tanımı

Hangi cihazın (projenin) hangi işlemi yapması için veri gönderdiğini tanımlayan komut açıklamasıdır. 

```json
"Command": "STF:WeatherStat.Timed_Save"
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

| Komut Adı   | Açıklama                                |
|-------------|-----------------------------------------|
| Timed       | Zamanlı uyanma ve sunucuya veri kaydı   |
| Manual      | Manual uyandırma ve sunucuya veri kaydı |