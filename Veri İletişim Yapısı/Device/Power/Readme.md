# 2. Power

Geliştirilen donanımların tamamı batarya destekli sistemler olarak tasarlanmaktadır. Herhangi bir güç kaynağına bağlı olarak çalışsa bile güç kesilmesi durumunda sunuculara veri gönderebilmek için yeterli enerjiye sahip olmaları gerekmektedir. Bu nedenle tüm ürünler üzerinde Li-Ion batarya (ürün cinsine göre adedi ve gücü değişmektedir bu bilgi donanım versiyonu içerisinde yer alacaktır) kullanılmaktadır.

Li-Ion bataryalar yapı gereği 3V8 nominal voltaj, 4V2 max voltaj ve 3V0 min voltaj olarak karakterize edilmektedir. Bu değerler teorik değerler olup ortam sıcaklığına göre değişmektedir. Düşük sıcaklıklar bir sorun değil bir avantajdır ve pil yaşlanmasını azaltır. Bununla beraber bataryaların 3V0 değerine düşmesi istenmeyen bir durumdur genellikle 3V2-3V4 aralığına düşmüş bataryalar boş olarak değerlendirilir.

Bu kapsamda donanımlar üzerinde batarya şarj ve batarya ölçümleme sistemleri bulunmaktadır. Bu sistemler üzerinden alınan veriler hem anlık hem de ileri vade sürdürülebilirlik analizleri için kaydedilmelidir.

Bu segment içerisinde cihaza ait güç parametreleri yer alamaktadır. Batarya durumu şarj bilgileri gibi parametreler bu alan içerisinde yer almaktadır. 

```json
"Power": {
	"Battery": {
		"AC": -0.15,
		"FB": 2000,
		"IB": 1300,
		"IV": 4.17,
		"SOC": 92.13,
		"T": 23.12,
		"Charge": 3
	}
}
```

## Tiny Paket İçeriği

İlgili komutun içeriğinde tanımlandığı şekilde gerek veri paketini küçültmek gerekse backend işlemlerini aza indirmek amacı ile bazı durumlarda aşağıdaki tabloda belirtildiği üzere bazı parametreler sunucuya gönderilmeyecektir.

| Değişlen Adı  | Normal Paket      | Tiny Paket        | 
|---------------|:-----------------:|:-----------------:|
| AC			|:white_check_mark:	|:white_check_mark:	|
| FB			|:white_check_mark:	|:x:				|
| IB			|:white_check_mark:	|:x:				|
| IV			|:white_check_mark:	|:white_check_mark:	|
| SOC			|:white_check_mark:	|:white_check_mark:	|
| T				|:white_check_mark:	|:x:				|
| Charge		|:white_check_mark:	|:white_check_mark:	|

***

## Battery

Sistem içerisinde kullanılmakta olan bataryaların anlık olarak takip edilmesi hem güvenlik hemde sürdürülebilirlik açısından önem teşkil etmektedir. Bu nedenle sistem içerisine MAX17055 batarya ölçüm sistematiği kurgulanmıştır. Bu sayede birçok batarya parametresini ölçümleyebilmekteyiz. Bu veri paketi içersinde analiz için gerekli önemli parametreler gönderilmektedir.

***

### "AC" : Ortalama Akım Tüketimi

Sistem güç katmanı üzerinde bulunan MAX17055 batarya ölçümleme çipi üzerinden ölçülen ortalama akım bilgisidir. Batarya ölçüm çipinin kullanılmasında ki birincil öncelik bu veridir (IV ile birlikte). Çip bataryaya bağlı kaldığı süre boyunca ölçümleme yapar ve bu verilerin ortalamalarını iç registerlarında tutar. Bu verinin negatif değer olması tüketim olduğunu (bataryadan güç çekimi), pozitif olması ise şarj olduğunu belirtmektedir (bataryaya doğru güç). Sonraki versiyonlarda akım değeri üzerinden güç analizleri ve batarya sağlığı konusunda analizler yapılabilecektir.

|                 | Açıklama                                        |
|-----------------|-------------------------------------------------|
| Değişken Adı    | AC                                              |
| Değişken Tanımı | **A**verage **C**urrent (Ortalama Akım)         |
| Değişken Tipi   | Float                                           |
| Değişlen Birimi | mA                                              |
| Örnek Veri      | -51.72                                          |

***

### "FB" : Tam Dolu Batarya Kapasitesi

Sistem güç katmanı üzerinde bulunan MAX17055 batarya ölçümleme çipi üzerinden ölçülen batarya tam dolu kapasite bilgisidir. Bu kapasite bilgisi mAh birimi üzerinden batarya döngüsüne göre anlık olarak hesaplanmaktadır. Herhangi bir harici kaynaktan set edilmemektedir. SOC değeri üzerinden bu veri değeri çarpılarak toplam kapasite bilgisine ulaşılabilmektedir bu nedenle FB değeri gönderilmemiştir.

|                 | Açıklama                                        |
|-----------------|-------------------------------------------------|
| Değişken Adı    | FB                                              |
| Değişken Tanımı | **F**ull **B**attery (Tam Dolu Kapasite)        |
| Değişken Tipi   | int                                             |
| Değişlen Birimi | mAh                                             |
| Örnek Veri      | 718                                             |

	# Bu veri "tiny" paketlerinde gönderilemyecektir.

***

### "IB" : Anlık Batarya Kapasitesi

Sistem güç katmanı üzerinde bulunan MAX17055 batarya ölçümleme çipi üzerinden ölçülen batarya anlık kapasite bilgisidir. Bu kapasite bilgisi mAh birimi üzerinden batarya döngüsüne göre anlık olarak hesaplanmaktadır. Herhangi bir harici kaynaktan set edilmemektedir. SOC değeri üzerinden bu veri değeri çarpılarak toplam kapasite bilgisine ulaşılabilmektedir bu nedenle FB değeri gönderilmemiştir.

|                 | Açıklama                                        |
|-----------------|-------------------------------------------------|
| Değişken Adı    | IB                                              |
| Değişken Tanımı | **I**nstant **B**attery (Anlık Kapasite)        |
| Değişken Tipi   | int                                             |
| Değişlen Birimi | mAh                                             |
| Örnek Veri      | 718                                             |

	# Bu veri "tiny" paketlerinde gönderilemyecektir.

***

### "IV" : Anlık Batarya Voltajı

Sistem kurulu bataryasına ait anlık voltaj bilgilerini vermektedir. Sonraki versiyonlarda voltaj değeri üzerinden güç analizleri ve batarya sağlığı konusunda analizler yapılabilecektir. Kullanılan batarya voltaj alt ve üst limitleri kayıt sırasında kontrol edilebilir.

|                 | Açıklama                                        |
|-----------------|-------------------------------------------------|
| Değişken Adı    | IV                                              |
| Değişken Tanımı | **I**nstant **V**oltage (Anlık batarya voltajı) |
| Değişken Tipi   | Float                                           |
| Değişlen Birimi | Volt                                            |
| Örnek Veri      | 3.89                                            |

***

### "SOC" : Anlık Batarya Doluluk Oranı

Sistem güç katmanı üzerinde bulunan MAX17055 batarya ölçümleme çipi üzerinden ölçülen batarya doluluk oranı bilgisidir. Batarya paketinin firmware üzerinde ayarlanmış kapasitesi ile anlık olarak ölçümlenen batarya kapasite oranı olarak hesaplanmaktadı. Bu hesap için batarya karakteristik eğrileri kullanılmakta ve lineer olmayan bir hesap ölçüm çipi tarafından anlık olarak yapılmaktadır.

Bu değer UI tasarımlar içerisinde batarya durum bilgisi olarak direkt paylaşılabilir yapıdadır.

|                 | Açıklama                                        |
|-----------------|-------------------------------------------------|
| Değişken Adı    | SOC                                             |
| Değişken Tanımı | **S**tate **o**f **C**harge (Kapasite yüzdesi)  |
| Değişken Tipi   | Float                                           |
| Değişlen Birimi | %                                               |
| Örnek Veri      | 17.97                                           |

	Batarya SOC verisinin tam doğru parametreyi gösterebilmesi için en az bir defa tam deşarj-şarj döngüsü
	tamamlamış olması gerekmektedir. Bu nedenle ilk gelen veriler hatalı olabilir.

***

### "T" : Çip Sıcaklığı

Sistem güç katmanı üzerinde bulunan MAX17055 batarya ölçümleme çipi üzerinden ölçülen kart sıcaklığıdır. Sonraki versiyonlarda sıcaklık değeri üzerinden güç analizleri ve batarya sağlığı konusunda analizler yapılabilecektir.

|                 | Açıklama                                        |
|-----------------|-------------------------------------------------|
| Değişken Adı    | T                                               |
| Değişken Tanımı | **T**emperature (Anlık Çip Sıcaklığı)           |
| Değişken Tipi   | Float                                           |
| Değişlen Birimi | Santigrat                                       |
| Örnek Veri      | 25.43                                           |

	# Bu veri "tiny" paketlerinde gönderilemyecektir.

***

### "Charge" : Şarj Durumu

BQ24298 şarj entegresi şarj durumlarını tanımlayan register değerine sahiptir. Bu register değeri işlemci tafaından okunarak veri paketi ile birlikte sunuculara kaydedilmektedir. Bu sayede şarj durumu ile güç kaynaklı arıza durumları tesbit edilebilir hale getirilmiştir. Bu register değerlerinin neleri ifade ettiği aşağıdaki tabloda belirtilmiştir.

|                 | Açıklama                                        |
|-----------------|-------------------------------------------------|
| Değişken Adı    | Charge                                          |
| Değişken Tanımı | **Charge**r Status (Şarj durumu)                |
| Değişken Tipi   | int                                             |
| Değişlen Birimi | -                                               |
| Örnek Veri      | 2 (0-3)                                         |

Şarj kodu değer açıklamaları.

| Status ID | Durum           | Açıklama                                  |
|-----------|-----------------|-------------------------------------------|
| 0         | Not Charging    | Şarj olmuyor                              |
| 1         | Precharge       | Ön şarj oluyor                            |
| 2         | Fast Charge     | Hızlı şarj oluyor                         |
| 3         | Charge Done     | Şarj tamamlandı                           |

Bu veri alanı gerekli durumlarda UI üzerinde direkt olarak gösterilebilecektir (örneğin şarj oluyor ikonu).

***