# Komut - Veri yapısı

Veri paketi 3 ana başlık altında gruplanmaktadır. Bu başlıklara ait veri gönderim seçenekleri aşağıda tanımlanmıştır.

## Command

Command verisi gönderilen verinin yapısına bağlı olarak aşağıdaki değerleri alabilir. Zorunlu verili olarak her paket içerisinde gönderilecektir.

| Komut      | Veri Gönderim Tipi                                         |
|------------|------------------------------------------------------------|
| Timed      | Hergün belirlenen saatte gönderim yapılan full data paketi |
| Timed_Tiny | Gün içerisinde standart veri gönderimi (her t sürede)      |

## Device

| JSON Variable | Timed         	| Timed_Tiny	    |
|---------------|:-----------------:|:-----------------:|
| Device		|:white_check_mark:	|:white_check_mark:	|
| Info			|:white_check_mark:	|:white_check_mark:	|
| ID			|:white_check_mark:	|:white_check_mark:	|
| Hardware		|:white_check_mark:	|:x:				|
| Firmware		|:white_check_mark:	|:x:				|
| Power			|:white_check_mark:	|:white_check_mark:	|
| Battery		|:white_check_mark:	|:white_check_mark:	|
| AC			|:white_check_mark:	|:white_check_mark:	|
| FB			|:white_check_mark:	|:x:				|
| IB			|:white_check_mark:	|:x:				|
| IV			|:white_check_mark:	|:white_check_mark:	|
| SOC			|:white_check_mark:	|:white_check_mark:	|
| T				|:white_check_mark:	|:x:				|
| Charge		|:white_check_mark:	|:white_check_mark:	|
| IoT			|:white_check_mark:	|:white_check_mark:	|
| GSM			|:white_check_mark:	|:white_check_mark:	|
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

## Payload

| JSON Variable | Timed         	| Timed_Tiny	    |
|---------------|:-----------------:|:-----------------:|
| Payload		|:white_check_mark:	|:white_check_mark:	|
| TimeStamp		|:white_check_mark:	|:white_check_mark:	|
| WeatherStat	|:white_check_mark:	|:white_check_mark:	|
| Location		|:white_check_mark:	|:x:				|
| Latitude		|:white_check_mark:	|:x:				|
| Longitude		|:white_check_mark:	|:x:				|
| Environment	|:white_check_mark:	|:white_check_mark:	|
| AT			|:white_check_mark:	|:white_check_mark:	|
| AH			|:white_check_mark:	|:white_check_mark:	|
| AP			|:white_check_mark:	|:white_check_mark:	|
| UV			|:white_check_mark:	|:white_check_mark:	|
| ST			|:white_check_mark:	|:white_check_mark:	|
| R				|:white_check_mark:	|:white_check_mark:	|
| WD			|:white_check_mark:	|:white_check_mark:	|
| WS			|:white_check_mark:	|:white_check_mark:	|
|               |[JSON](Timed.json) |[JSON](Timed_Tiny.json)|