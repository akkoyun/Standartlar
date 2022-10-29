# SBus Global Soket Yapısı <sup>03.00.00</sup>

Modüler sistem planlaması içerisinde tüm kartlar için uyumlu bir veri yolu standardı belirlemek gerekmiştir. Bu nedenle işlemci modülleri için SODIMM ve add-on modüller için PCIe-mini soket tipleri baz alınarak (sadece fiziksel olarak soket standardı alınmış pin yapıları ihtiyaçlarımıza göre optimize edilmiştir) bir bağlantı mimarisi geliştirilmiştir. Geliştirilen ve planlanan birçok cihaza hitap eden bir modül yapısı kurabilmek adına aşağıda tanımlanan ana standartlarda sistem kurgulanmıştır. 

| Standart                  | Uzun İsim   | Açıklama                                                         | Version  |
|---------------------------|-------------|------------------------------------------------------------------|----------|
| [SODIMM](/SBus/SODIMM.md) | SBus-SODIMM | Mikro işlemci içeren ana ünite modülleri için kullanılmaktaıdır. | 00.00.01 |
| [PCIe](/SBus/PCIe.md)     | SBus-PCIe   | Add-on modüller için kullanılmaktadır.                           | 01.00.00 |

Kurum içi kodlama yapısında ilgili standart açıklaması modüllerin sonuna eklenecektir. Örneğin PCIe iletişim yapısına sahip GSM modülü için **B101AA-PCIe** yada SODIMM iletişim yapısına sahip İşlemci modülü için **B001BA-SODIMM**.
