# Telit Tarafından Önerilen Tasarım Parametreleri <sup>01.00.00</sup>

**Telit design review team** tarafından bundan önce yapılmış tasarım incelemeleri içerisinde yer alan tasarım notları bu başlık altında kategorilendirilmiş şekilde yer almaktadır. Yapılan tasarımlarda karşılaşılan hatalar ise ayrıca **bugs** kısmı altında anlatılacaktır.

## Tasarım Teknik Önerileri

### Şematik tasarım notları

##### AE-33729 - Sinyal hatları tristate olması.

Yapılan tüm tasarım inceleme dokümanlarında özellikle belirtilen bir maddedir. Modemin açma kapama işlemleri sırasında sinyal hatları üzerinden güç alarak kapanmama sorunlarının olabileceği bu nedenle sinyal hatlarının tristate özellikte (istenilen durumlarda yüksek empedans modunda bırakılabilmesi) olması istenmektedir.

Bu nedenle seçilen voltaj dönüştürücülerin mutlaka tristate özellik desteklemesi gerektiği unutulmamalıdır.

***

##### AE-33764 - SIM hattı kapasitör değerleri.

Tüm SIM hatları (I/O, CLK, RST ve SIM_VCC) yüksek frekans parazitler için 33pF kapasitör ile filtre edilmelidir. Buna ek olarak SIM_VCC hattı ayrıca bir 1uF kapasitör ile (GE910 için) desteklenmelidir. 

***

##### AE-33764 - SIM hattı ESD koruması.

Tüm SIM hatları sokete insan eli değebileceği için ESD koruması yapılması gerekmektedir. Bu ESD ler zener gibi tek yönlü korumalar yerine çift yönlü olarak seçilmelidir. 

SIM pinlerinde kullanılacak olan TVS diyotları kullanırken stand-off voltajının minimum 5V olması gerektiği ve giriş kapasitanslarının 30pF dan az olması gerektiği unutulmamalıdır. 

Telitin önerdiği ESD : SP1001-04JTG

***

##### AE-33729 - LED sinyalleri filtrasyonu.

Sistem içerisinde kullanılan tüm LED komponentleri için anode ve cathode hatları üzerine 33pF kapasitör ile filtre edilmesi gerekmektedir.

***

##### AE-33729 - Filtre kapasitörleri.

Sistem içerisinde kullanılan aşağıda tanımlanmış kısımlar eğer metal kalkan ile yalıtılmaması durumunda 33pF kapasitör ile filtrelenecektir. 

* Giriş ve çıkış bağlantısı yapan güç hatları.
* Doğrudan GND bağlantısı olmayan tüm diyotlar için anode ve cathode hatları.
* Transistör base hatları, phototransistor ve opto yalıtım elemanları sinyal hatları.

Seçilen filtre kapasitörünün planlanması gerekmektedir. Genellikle 33pF SMD 0603/0402 25V/50V COG kapasitörler yaklaşık 1GHz de rezonans frekansına sahiptir. Ancak satıcıdan satıcıya farklılık göstermektedir. GSM RF i etkili şekilde filtrelemek için bu sinyal kapasitörleri yaklaşık 1GHz de kendi rezonansı (SRF) olması gerekmektedir. 

Seçilecek kapasitörün 33pF 25V ve 1GHz rezonanslı olması gerekmektedir.

***

### PCB tasarım notları

##### 00262307 - PCB yol kalınlıkları

00262307 teknik yazışması neticesinde gelen cevaba göre yüksek sıklıkla veri transferi yapılması gerekli durumlarda GE910 GSM modem için güç hattı yol kalınlığı 2mm (1oz) olarak kullanılması uygun ve hesaplamalar doğrudur.

Bunun yanı sıra çok yüksek veri transferi yapmayarak yüksek güç tüketimi olmayan durumlar için RMS akım değeri 2G de 350mA ve 4G de 700mA olarak söylenmiştir. Bu durumlar göz önüne alındığında iç katmanda yer alan güç hatları için 0.5mm (1oz) yol kalınlığı ve dış katmanlar için 0.3mm (1oz) yol kalınlığı uygun olmaktadır.

Bu belirtilen yol kalınlıkları minimum olup uygun şartlarda kalınlaştırmak her zaman daha iyi olacağı belirtilmiştir. Ayrıca 0.6mm yol yakınlaşma değeri olması gerektiği ayrıca hesaplanmıştır.

Güç hatlarının olabildiğince kısa tutulması gerektiği (kart nezdinde) ayrıca tasarım notu olarak verilmiştir. 

Tasarım önerisinde ayrıca güç yolları için ısı artışlarının ihmal edilebilir düzeyde olduğu belirtilmiştir. RMS değeri üzerinden hesaplanan değerlerde güç yolu için termal gücün 10-30 mW olduğu söylenmiş ve ayrıca modemin termal gücünün 2W olduğu göz önünde bulundurulursa bunun ihmal edilebilecek kadar az olduğu yazılmıştır.

Teknik notu yazan : Bruno Tomaz (Telit)

***

##### AE-33729 - Anten empedansı

Yapılan tüm tasarım inceleme dokümanlarında özellikle belirtilen bir maddedir. PCB tasarım sırasında anten hatlarının olabildiğince kısa tutulması gerektiği ve ayrıca bu anten hatlarının altında iç katmanların boş olması gerektiği sadece zıt katmanın GND olması gerektiği belirtilmiştir. Ayrıca anten hatlarının etrafı via lar ile çevrilmeli ve olası dış etkilenmeler minimuma indirilmelidir. 

***

##### AE-33729 - Anten ve güç hattı teması.

Anten hatlarının hiçbir güç hattı ile yakınlaşmaması mutlaktır. Anten hatları sadece GND sınırı bununmalıdır.

***

##### AE-33729 - Kart sınırları GND hattı.

Kart sınırları mutlaka tüm katmanlarda GND olarak planlanmalıdır. Ayrıca kart kenarlarında 2mm (max) aralıklı via kafes yapısı kurulmalıdır. 

***

## Bug's