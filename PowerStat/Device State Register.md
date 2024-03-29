# Cihaz Durum Kodu ve Kontrol Algoritması

PowerStat cihazı yapısı gereği bir çok girdiyi aynı anda kontrol etme, belirtilen koşullarda otomatik karar ile aksiyon alma ve aynı zamanda belirtilen koşullarda kullanıcı bildirimi yapabilen bir yapay zeka modülüne sahiptir. 

Bu işlemleri hem cihaz üzerinde çok fazla sistem kaynağı tüketmemesi için dört register ile işlem yapabilme altyapısı kullanılmaktadır. Bu regiseterlar ve maskeler aşağıda tanımlanmıştır.

| Register Tipi     | Açıklama                                        | Veri Tipi |
|-------------------|-------------------------------------------------|-----------|
| Status_Register   | Sistem durumlarını değerlendiren ana register.  | uint32_t  |
| Buffer_Register   | Durum karşılaştırması yapan register.           | uint32_t  |
| Publish_Mask      | Durumların kullanıcıya bildirim maskesi.        | uint32_t  |
| Stop_Mask         | Durumlara göre otomatik aksiyon alma maskesi.   | uint32_t  |

Status_Register bit değerleri interruptlar ile değişebileceği gibi tanımlanan ölçüm aşımlarında da değişebilecektir. Sistem durum registeri anlık olarak güncel tutulacaktır.

Sistem döngüsü sırasında buffer ve status registerları karşılaştırılacak ve eğer bir fark görülür ise aşağıdaki veri tiplerinde gönderim yapılacaktır. Gönderim sonrası ise buffer değişleni status değişkeni ile eşitlenecektir. Örneğin girdilerde oluşan değişimler "Interrupt" paketi ile yada ölçümlerde oluşan limit aşım durumları "Alarm" paketi ile gönderilecektir.


***

## Status Register

	Değişken Adı : Status_Register
	Değişken tipi : uint32_t

Sistem içerisinde gerçekleşen durumların koşul oluştuğu an otomatik olarak güncellendiği register verisidir. Aşağıda tanımlanan veri yapısındadır.

***

## Buffer Register

	Değişken Adı : Buffer_Register
	Değişken tipi : uint32_t

Sistemde oluşan her türlü koşulda veri gönderim yapısını düzene sokabilmek için (çoklu veri gönderimin önüne geçmek için) tanımlanmış bir register değeridir. 

***

## Publish Register

	Değişken Adı : Publish_Register
	Değişken tipi : uint32_t

Sistem içerisinde gerçekleşen durumların hangilerinin IoT üzerinden bulut sunucularına gönderileceği değerini tutan register verisidir.

***

## Stop Register

	Değişken Adı : Stop_Register
	Değişken tipi : uint32_t

Sistem içerisinde gerçekleşen durumların hangilerinin otomatik olarak pompayı durduracağı değerini tutan register verisidir.

***

# Register Bit Yapısı

| Bit | Register Name      | Status_Register | Stop_Register | Publish_Register | Pack Type |
|:---:|:-------------------|:----------------|:-------------:|:----------------:|:---------:|
| 31  | STATUS_SYSTEM      | X               | 0             | 0                | Online    |
| 30  | STATUS_CT_T        | 0               | 0             | 0                | Online    |
| 29  | STATUS_CT_S        | 0               | 0             | 0                | Online    |
| 28  | STATUS_CT_R        | 0               | 0             | 0                | Online    |
| 27  | -                  | 0               | 0             | 0                |           |
| 26  | STATUS_I_IMBALANCE | X               | 0             | 0                | Alarm     |
| 25  | STATUS_V_IMBALANCE | X               | 0             | 1                | Alarm     |
| 24  | STATUS_FQ_HIGH     | X               | 1             | 1                | Alarm     |
| 23  | STATUS_FQ_LOW      | X               | 1             | 1                | Alarm     |
| 22  | STATUS_I_HIGH      | X               | 0             | 0                | Alarm     |
| 21  | STATUS_V_HIGH      | X               | 1             | 1                | Alarm     |
| 20  | STATUS_V_LOW       | X               | 1             | 1                | Alarm     |
| 19  | -                  | 0               | 0             | 0                |           |
| 18  | -                  | 0               | 0             | 0                |           |
| 17  | -                  | 0               | 0             | 0                |           |
| 16  | -                  | 0               | 0             | 0                |           |
| 15  | -                  | 0               | 0             | 0                |           |
| 14  | -                  | 0               | 0             | 0                |           |
| 13  | STATUS_P_RISE      | X               | 0             | 0                | Alarm     |
| 12  | STATUS_P_DROP      | X               | 0             | 0                | Alarm     |
| 11  | STATUS_P_HIGH      | X               | 0             | 1                | Alarm     |
| 10  | STATUS_P_LOW       | X               | 0             | 1                | Alarm     |
| 9   | -                  | 0               | 0             | 0                |           |
| 8   | STATUS_INPUT       | X               | 0             | 1                | Interrupt |
| 7   | STATUS_FAULT_SA    | X               | 0             | 1                | Interrupt |
| 6   | STATUS_FAULT_MP    | X               | 1             | 1                | Interrupt |
| 5   | STATUS_FAULT_TH    | X               | 1             | 1                | Interrupt |
| 4   | -                  | 0               | 0             | 0                |           |
| 3   | STATUS_PHASE_T     | X               | 1             | 1                | Interrupt |
| 2   | STATUS_PHASE_S     | X               | 1             | 1                | Interrupt |
| 1   | STATUS_PHASE_R     | X               | 1             | 1                | Interrupt |
| 0   | STATUS_PUMP        | X               | 0             | 1                | Interrupt |
|     | **Default**        |                 | 0x0FF0086E    | 0x0FF08C6F       |

***

## Bit.0 - Pompa Durumu 

	Bit Adı : [STATUS_PUMP]

Sistem girdi pinleri içerisinde yer alan M1 (ana kontaktör), M2 (üçgen kontaktörü) ve M3 (yıldız kontaktörü) girdileri algoritma dahilinde analiz edilerek M1 ve M2 çektiği zaman yani sistem üçgen durumda yol verilmiş ise pompa durumu aktif olarak değiştirilir.

	High : Pompa çalışıyor.
	Low : Pompa çalışmıyor.

	Publish : Etkin
	Stop : Pasif

Bu bit sadece interrupt değişimlerinde güncellenecektir. Güncellemeler "Interrupt" veri tipi ile gönderilecektir.

***

## Bit.1-2-3 - Faz Durumu

	Bit Adı : [STATUS_PHASE_R] [STATUS_PHASE_S] [STATUS_PHASE_T]

Belirli elektriksel girdiler anlık olarak kontrol edilmekte ve analiz edilmektedir. Bu girdilerden 3 ü sistem faz beslemesidir. Fazlarda herhangi bir kayıp olduğu zaman bu sinyaller kaybolmakta böylece sistemde faz kaybı arızaları tesbit edilebilmektedir.

	High : Faz var.
	Low : Faz yok.

	Publish : Etkin
	Stop : Etkin

Bu bit sadece interrupt değişimlerinde güncellenecektir.

***

## Bit.4 - Rezerve

	Bit Adı : [--]

İleride belirlenebilecek kullanım alanları için ayrılmıştır.

***

## Bit.5 - Termik Arıza

	Bit Adı : [STATUS_FAULT_TH]

Belirli elektriksel girdiler anlık olarak kontrol edilmekte ve analiz edilmektedir. Bu girdilerden birisi de termik koruma rölesi arızasını belirtir bir girdidir. Sistem içerisinde yer alan termik kontrol rölesi üzerinde yer alan NO kontağı üzerinden geçen sinyal sisteme girmektedir. Böylece bir arıza oluştuğunda bu sinyal aktif olmaktadır.

	High : Termik arızası var.
	Low : Termik arızası yok.

	Publish : Etkin
	Stop : Etkin

Bu bit sadece interrupt değişimlerinde güncellenecektir.

***

## Bit.6 - Motor Koruma Arızası

	Bit Adı : [STATUS_FAULT_MP]

Belirli elektriksel girdiler anlık olarak kontrol edilmekte ve analiz edilmektedir. Bu girdilerden birisi de motor koruma arızasını belirtir bir girdidir. Sistem içerisinde yer alan motor koruma rölesi üzerinde yer alan NO kontağı üzerinden geçen sinyal sisteme girmektedir. Böylece bir arıza oluştuğunda bu sinyal aktif olmaktadır.

	High : Motor Koruma arızası var.
	Low : Motor Koruma arızası yok.

	Publish : Etkin
	Stop : Etkin

Bu bit sadece interrupt değişimlerinde güncellenecektir.

***

## Bit.7 - Sistem Anomalisi Arızası

	Bit Adı : [STATUS_FAULT_SA]

Belirli elektriksel girdiler anlık olarak kontrol edilmekte ve analiz edilmektedir. Bu girdiler içerisinde aşağıdaki koşulların oluşması durumunda bir sistem anomalisi durumu oluşmaktadır. 

* M1, M2 ve M3 aynı anda çekerse.
* M2 ve M3 aynı anda çekerse.
* M3 kendi başına çekerse.
* M2 kendi başına çekerse.
* M1 kendi başına çekerse.
* Termik arızası varken herhangi bir kontaktör çekerse.
* Motor koruma arızası varken 3 fazda var ise.
* Motor koruma arızası varken herhangi bir kontaktör çekerse.

<br>

	High : Anomali var.
	Low : Anomali yok.

	Publish : Pasif
	Stop : Pasif

Bu bit sadece interrupt değişimlerinde güncellenecektir.

***

## Bit.8 - Harici Girdi Durum Bilgisi

	Bit Adı : [STATUS_INPUT]

Cihaz üzerinde seçimsel durumlarda belirtilen girdi pini (cihaz üzerindeki motor koruma rölesi girişi) anlık olarak kontrol edilmekte ve analiz edilmektedir. Bu girdi pininin durumu aşağıdaki koşulların oluşması durumunda aktif olarak değiştirilir.

* Pano kapağının açılması yada kapanması.
* Sistemin otomatik (zamanlı) start fonksyonunun aktif edilmesi.

<br>

	High : Harici girdi aktif.
	Low : Harici girdi pasif.

	Publish : Pasif
	Stop : Pasif

Bu bit sadece interrupt değişimlerinde güncellenecektir.

***

## Bit.9 - Rezerve

	Bit Adı : [--]

İleride belirlenebilecek kullanım alanları için ayrılmıştır.

***

## Bit.10 - Düşük Basınç Arızası

	Bit Adı : [STATUS_P_LOW]

Sistem ana sulama hattı üzerinde bulunan basınç sensörü belirlenen periyodlarla (default 3sn) ölçümleme yaparak istatistiksel bir dizi analize tabi tutar. Bu ölçümlemeler sistem tarafından belirlenmiş limitin altında olup olmadığını anlık olarak tesbit eder.

	High : Basınç değeri eşik değerin altında.
	Low : Basınç değeri eşik değerin altımda değil.

	Publish : Aktif
	Stop : Pasif

Bu bit sadece ilgili sensör tarafından gönderilen ölçüm ve limit aşımı sonrasında güncellenecektir.

***

## Bit.11 - Yüksek Basınç Arızası

	Bit Adı : [STATUS_P_HIGH]

Sistem ana sulama hattı üzerinde bulunan basınç sensörü belirlenen periyodlarla (default 3sn) ölçümleme yaparak istatistiksel bir dizi analize tabi tutar. Bu ölçümlemeler sistem tarafından belirlenmiş limitin üstünde olup olmadığını anlık olarak tesbit eder.

	High : Basınç değeri eşik değerin üstünde.
	Low : Basınç değeri eşik değerin üstünde değil.

	Publish : Aktif
	Stop : Aktif

Bu bit sadece ilgili sensör tarafından gönderilen ölçüm ve limit aşımı sonrasında güncellenecektir.

***

## Bit.12 - Ani Basınç Düşüşü Arızası

	Bit Adı : [STATUS_P_DROP]

Sistem ana sulama hattı üzerinde bulunan basınç sensörü belirlenen periyodlarla (default 3sn) ölçümleme yaparak istatistiksel bir dizi analize tabi tutar. Bu ölçümlemeler sistem tarafından belirlenmiş bir limitin üzerinde eğim ile düşüş olup olmadığını anlık olarak tesbit eder.

	High : Ani basınç düşüşü mevcut.
	Low : Ani basınç düşüşü yok.

	Publish : Pasif
	Stop : Pasif

Bu bit sadece ilgili sensör tarafından gönderilen ölçüm ve limit aşımı sonrasında güncellenecektir.

***

## Bit.13 - Ani Basınç Yükselişi Arızası

	Bit Adı : [STATUS_P_RISE]

Sistem ana sulama hattı üzerinde bulunan basınç sensörü belirlenen periyodlarla (default 3sn) ölçümleme yaparak istatistiksel bir dizi analize tabi tutar. Bu ölçümlemeler sistem tarafından belirlenmiş bir limitin üzerinde eğim ile yükseliş olup olmadığını anlık olarak tesbit eder.

	High : Ani basınç yükselişi mevcut.
	Low : Ani basınç yükselişi yok.

	Publish : Pasif
	Stop : Pasif

Bu bit sadece ilgili sensör tarafından gönderilen ölçüm ve limit aşımı sonrasında güncellenecektir.

***

## Bit.14 - Rezerve

	Bit Adı : [--]

İleride belirlenebilecek kullanım alanları için ayrılmıştır.

***

## Bit.15 - Voltaj Dengesizliği Arızası

	Bit Adı : [STATUS_V_IMBAL]

Sistemin bağlı olduğu şebeke üzerinde meydana gelen voltaj dengesizliğini belirten bit değeridir.

	High : Voltaj dengesizliği mevcut.
	Low : Voltaj dengesizliği yok.

	Publish : Aktif
	Stop : Pasif

Bu bit sadece ilgili sensör tarafından gönderilen ölçüm ve limit aşımı sonrasında güncellenecektir.

***

## Bit.16 - Akım Dengesizliği Arızası

	Bit Adı : [STATUS_I_IMBAL]

Sistemin bağlı olduğu şebeke üzerinde meydana gelen akım dengesizliğini belirten bit değeridir.

	High : Akım dengesizliği mevcut.
	Low : Akım dengesizliği yok.

	Publish : Pasif
	Stop : Pasif

Bu bit sadece ilgili sensör tarafından gönderilen ölçüm ve limit aşımı sonrasında güncellenecektir.

***

## Bit.17 - R Fazı Düşük Voltaj Arızası

	Bit Adı : [STATUS_UN_VRMS_R]

Sistemin bağlı olduğu şebeke üzerinde (R fazında) düşük voltaj arızasını belirten bit değeridir.

	High : R Fazında voltaj minimum limit değeri altında.
	Low : R Fazında voltaj minimum değer üzerinde.

	Publish : Aktif
	Stop : Aktif

Bu bit sadece ilgili sensör tarafından gönderilen ölçüm ve limit aşımı sonrasında güncellenecektir.

***

## Bit.18 - R Fazı Yüksek Voltaj Arızası

	Bit Adı : [STATUS_OV_VRMS_R]

Sistemin bağlı olduğu şebeke üzerinde (R fazında) yüksek voltaj arızasını belirten bit değeridir.

	High : R Fazında voltaj maksimum limit değeri üzerinde.
	Low : R Fazında voltaj maksimum değer altında.

	Publish : Aktif
	Stop : Aktif

Bu bit sadece ilgili sensör tarafından gönderilen ölçüm ve limit aşımı sonrasında güncellenecektir.

***

## Bit.19 - S Fazı Düşük Voltaj Arızası

	Bit Adı : [STATUS_UN_VRMS_S]

Sistemin bağlı olduğu şebeke üzerinde (S fazında) düşük voltaj arızasını belirten bit değeridir.

	High : S Fazında voltaj minimum limit değeri altında.
	Low : S Fazında voltaj minimum değer üzerinde.

	Publish : Aktif
	Stop : Aktif

Bu bit sadece ilgili sensör tarafından gönderilen ölçüm ve limit aşımı sonrasında güncellenecektir.

***

## Bit.20 - S Fazı Yüksek Voltaj Arızası

	Bit Adı : [STATUS_OV_VRMS_S]

Sistemin bağlı olduğu şebeke üzerinde (S fazında) yüksek voltaj arızasını belirten bit değeridir.

	High : S Fazında voltaj maksimum limit değeri üzerinde.
	Low : S Fazında voltaj maksimum değer altında.

	Publish : Aktif
	Stop : Aktif

Bu bit sadece ilgili sensör tarafından gönderilen ölçüm ve limit aşımı sonrasında güncellenecektir.

***

## Bit.21 - T Fazı Düşük Voltaj Arızası

	Bit Adı : [STATUS_UN_VRMS_T]

Sistemin bağlı olduğu şebeke üzerinde (T fazında) düşük voltaj arızasını belirten bit değeridir.

	High : T Fazında voltaj minimum limit değeri altında.
	Low : T Fazında voltaj minimum değer üzerinde.

	Publish : Aktif
	Stop : Aktif

Bu bit sadece ilgili sensör tarafından gönderilen ölçüm ve limit aşımı sonrasında güncellenecektir.

***

## Bit.22 - T Fazı Yüksek Voltaj Arızası

	Bit Adı : [STATUS_OV_VRMS_T]

Sistemin bağlı olduğu şebeke üzerinde (T fazında) yüksek voltaj arızasını belirten bit değeridir.

	High : T Fazında voltaj maksimum limit değeri üzerinde.
	Low : T Fazında voltaj maksimum değer altında.

	Publish : Aktif
	Stop : Aktif

Bu bit sadece ilgili sensör tarafından gönderilen ölçüm ve limit aşımı sonrasında güncellenecektir.

***

## Bit.23 - Düşük Frekans Arızası

	Bit Adı : [STATUS_UN_FREQ]

Sistemin bağlı olduğu şebeke üzerinde düşük frekans arızasını belirten bit değeridir.

	High : Şebeke frekansı belirtilen eşik değerin altında.
	Low : Şebeke frekansı belirtilen eşik değerin altında değil.

	Publish : Aktif
	Stop : Aktif

Bu bit sadece ilgili sensör tarafından gönderilen ölçüm ve limit aşımı sonrasında güncellenecektir.

***

## Bit.24 - Yüksek Frekans Arızası

	Bit Adı : [STATUS_OV_FREQ]

Sistemin bağlı olduğu şebeke üzerinde yüksek frekans arızasını belirten bit değeridir.

	High : Şebeke frekansı belirtilen eşik değerin üstünde.
	Low : Şebeke frekansı belirtilen eşik değerin üstünde değil.

	Publish : Aktif
	Stop : Aktif

Bu bit sadece ilgili sensör tarafından gönderilen ölçüm ve limit aşımı sonrasında güncellenecektir.

***

## Bit.25 - R Fazı Yüksek Akım Arızası

	Bit Adı : [STATUS_OV_IRMS_R]

Sistemin bağlı olduğu şebeke üzerinde (R fazında) yüksek akım arızasını belirten bit değeridir.

	High : R Fazında akım maksimum limit değeri üzerinde.
	Low : R Fazında akım maksimum değer altında.

	Publish : Aktif
	Stop : Aktif

Bu bit sadece ilgili sensör tarafından gönderilen ölçüm ve limit aşımı sonrasında güncellenecektir.

***

## Bit.26 - S Fazı Yüksek Akım Arızası

	Bit Adı : [STATUS_OV_IRMS_S]

Sistemin bağlı olduğu şebeke üzerinde (S fazında) yüksek akım arızasını belirten bit değeridir.

	High : S Fazında akım maksimum limit değeri üzerinde.
	Low : S Fazında akım maksimum değer altında.

	Publish : Aktif
	Stop : Aktif

Bu bit sadece ilgili sensör tarafından gönderilen ölçüm ve limit aşımı sonrasında güncellenecektir.

***

## Bit.27 - T Fazı Yüksek Akım Arızası

	Bit Adı : [STATUS_OV_IRMS_T]

Sistemin bağlı olduğu şebeke üzerinde (T fazında) yüksek akım arızasını belirten bit değeridir.

	High : T Fazında akım maksimum limit değeri üzerinde.
	Low : T Fazında akım maksimum değer altında.

	Publish : Aktif
	Stop : Aktif

Bu bit sadece ilgili sensör tarafından gönderilen ölçüm ve limit aşımı sonrasında güncellenecektir.

***

## Bit.28 - Rezerve

	Bit Adı : [--]

İleride belirlenebilecek kullanım alanları için ayrılmıştır.

***

## Bit.29 - Rezerve

	Bit Adı : [--]

İleride belirlenebilecek kullanım alanları için ayrılmıştır.

***

## Bit.30 - Rezerve

	Bit Adı : [--]

İleride belirlenebilecek kullanım alanları için ayrılmıştır.

***

## Bit.31 - Sistem Diagnostic Durumu

	Bit Adı : STATUS_SYSTEM

Sistem bünyesinde oluşabilecek her türlü diagnostik hatasını belirten bit değeridir. I2C hatası veya SD kart durumu için gösterilir.

	High : Diagnostic hatası mevcut.
	Low : Sistem diagnostic hatası yok.

	Publish : Pasif
	Stop : Pasif

Bu bit sadece boot anında çalıştırılan sistem kontrol durumunda güncellenecektir.
