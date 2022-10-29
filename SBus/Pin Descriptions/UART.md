# Seri Haberleşme Kanalları [2xUART]

Modüller anakart ile ilgili iletişim kanalları üzerinden haberleşmektedir. Seri haberleşme (UART) bunların en çok kullanılanlarından birisidir. Bu nedenle modül bağlantısı içerisinde 2 kanal UART haberleşme giriş ve çıkışı bulunmaktadır.

GSM, WiFi veya BlueTooth gibi IoT modülleri için gerekli durumlarda (test vb) kullanılmak üzere 2 kanal olarak konumlandırılmıştır.

UART0 ve UART1 olarak gruplanan iletişi hatları için ana iletişim hattı UART0 olarak sabitlenmiştir. Bu ana iletişim hattı **[COMMUNICATION_ENABLE]** sinyali ile kontrol edilmektedir (aktif veya pasif). İletişim hattı sinyal voltaj seviyesi 3V3 olarak tanımlanmıştır (UART1 farklı voltaj seviyelerinde çalışabilmektedir).

| Açıklama          | Değer                              |
|-------------------|------------------------------------|
| Uzun Adı          | **3V3_UART0_TX**, **3V3_UART0_RX** |
| Kısa Adı          | **UART0_TX**, **UART0_RX**         |
| Voltaj Seviyesi   | 3V3                                |
| Sinyal            | Girişi ve Çıkış (modüle Göre)      |

| Açıklama          | Değer                              |
|-------------------|------------------------------------|
| Uzun Adı          | **UART1_TX**, **UART1_RX**         |
| Kısa Adı          | **UART0_TX**, **UART0_RX**         |
| Voltaj Seviyesi   | Değişken                           |
| Sinyal            | Girişi ve Çıkış (modüle Göre)      |
