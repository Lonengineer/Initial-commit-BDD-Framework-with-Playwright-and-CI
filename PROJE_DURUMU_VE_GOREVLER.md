# SauceDemo Otomasyon Projesi - Durum Özeti ve Görev Dağılımı


## 🚀 Projenin Şu Anki Durumu (Neler Yapıldı?)
Şu ana kadar projenin tüm çekirdek mimarisi ve temel senaryoları kodlanmış, stabil ve modern bir altyapı oturtulmuştur.

### 1. Kullanılan Teknolojiler ve Mimari
* **Framework:** Selenium'dan çok daha modern, hızlı ve stabil olan **Playwright**'a geçiş yapıldı.
* **Dil ve Yaklaşım:** Python ve **Behave (BDD - Behavior Driven Development)** kullanılarak Gherkin dilinde (`Given, When, Then`) testler yazıldı.
* **Tasarım Deseni:** **Page Object Model (POM)** mimarisi kusursuz şekilde uygulandı. Kod tekrarı önlendi, okunabilirlik artırıldı. (`base_page.py`, `login_page.py`, `cart_page.py` vb.)
* **Raporlama:** **Allure Reports** entegrasyonu yapıldı. Hata alan testlerde anında tam sayfa ekran görüntüsü alınıp rapora ekleniyor.
* **Konfigürasyon:** `config.json` ile dinamik yönetim sağlandı. (Headless mod, tarayıcı seçimi ve görsel takip için "slow_mo" gecikme modu tek dosyadan yönetiliyor.)
* **Çalıştırıcı:** Takımın kolayca testleri koşup raporları görebilmesi için `run_tests.bat` dosyası hazırlandı.

### 2. Tamamlanan Test Senaryoları (Feature'lar)
* `login.feature`: Başarılı giriş testleri.
* `cart.feature`: Sepete ürün ekleme, çıkarma, sepet rozeti (badge) sayı kontrolleri.
* `checkout.feature`: Başarılı sipariş verme (End-to-End) süreci ve boş form gönderildiğinde hata mesajı doğrulaması.
* `sorting.feature`: Ürün sayfasındaki A-Z, Z-A, Ucuz-Pahal, Pahalı-Ucuz filtreleme testleri.
* `performance.feature`: Sayfaların 5 saniyenin altında yüklendiğini doğrulayan hız/performans testleri.

---

## 📋 Takım Arkadaşlarına Görev Dağılımı (Bundan Sonra Ne Yapılacak?)

Ana altyapıyı, mimariyi ve pozitif testlerin çoğunu tamamladım. Projeyi daha profesyonel bir seviyeye çıkarmak için geri kalan işleri 3 parçaya böldüm. Lütfen herkes kendi sorumluluğunu alıp geliştirmelere başlasın.

### 🧑‍💻 Takım Arkadaşı 1: CI/CD Pipeline ve Bulut Entegrasyonu (DevOps Odaklı)
**Görevler:**
1. Projeyi GitHub/GitLab'a taşıdıktan sonra bir **GitHub Actions** veya **Jenkins Pipeline** dosyası oluşturmak.
2. Her `push` veya `Pull Request` işleminde Playwright testlerinin otomatik (headless) olarak uzak sunucuda çalışmasını sağlamak.
3. Çalışan testlerin Allure Raporlarını otomatik olarak oluşturup **GitHub Pages**, AWS S3 veya benzeri bir bulut servisine "Test Sonuçları Sayfası" olarak deploy etmek.
4. (Opsiyonel) Başarısız testlerde Slack veya Discord kanalına otomatik bildirim atılmasını sağlamak.

### 🧑‍💻 Takım Arkadaşı 2: Negatif Testler ve Edge Case (Sınır Durum) Senaryoları
**Görevler:**
1. Mevcut `login.feature` dosyasına "Locked Out User" (Kilitli kullanıcı), hatalı şifre, boş kullanıcı adı girişleri gibi negatif senaryoları eklemek ve `login_steps.py` içerisine bağlamak.
2. `cart.feature` içerisine, rastgele/farklı sıradaki ürünlerin eklenip çıkarılması gibi karmaşık (complex) sepet operasyonları yazmak.
3. Glitchy User (Sistemi yavaşlatan kullanıcı) profili ile giriş yapıldığında uygulamanın nasıl tepki verdiğini test eden ek performans sınır durumları yazmak.

### 🧑‍💻 Takım Arkadaşı 3: Cross-Browser & Mobil Test Genişletmesi
**Görevler:**
1. Şu an testler sadece Chromium'da (Chrome) koşuyor. `features/environment.py` ve `config.json` yapısı Firefox ve WebKit (Safari) için uygun altyapıya sahip. Bu tarayıcılarda da testlerin stabil çalıştığından emin olmak.
2. Playwright'ın "Mobil Emülasyon" (Mobile Viewport) özelliğini `environment.py` dosyasına entegre etmek. (Örn: Bir testin iPhone 13 ekran boyutlarında çalıştırılmasını sağlamak).
3. Mobil boyutta hamburger menünün (sol üstteki 3 çizgi) düzgün açılıp kapandığını test eden yepyeni bir `navigation.feature` dosyası ve step'leri yazmak.

---

> **Not:** Lütfen geliştirmelerinizi yaparken projenin kod standartlarına (Page Object Model kurallarına) ve `base_page.py` içerisindeki Playwright metotlarına sadık kalın. Yeni bir fonksiyon yazmadan önce BasePage içinde benzerini yazıp yazmadığıma mutlaka bakın. Kolay gelsin! 🚀

---

## 📖 Kapsamlı Teknik Kod İncelemesi ve Dokümantasyon

Bu bölüm, projede yer alan **tüm dosyaların**, **klasör yapısının** ve **kod bloklarının** ne işe yaradığını, neden böyle yazıldığını tek tek, satır satır ve eksiksiz bir biçimde açıklamaktadır. Takım arkadaşlarınızın projeyi tam olarak anlaması için bir "Kullanım Kılavuzu ve Mimari Kılavuzu" niteliğindedir.

### 🏗️ 1. Mimari Tasarım Kararları

Proje üç temel teknoloji üzerine inşa edilmiştir:
1. **Python:** Projenin ana programlama dili.
2. **Playwright:** Tarayıcıları yöneten, tıklama ve yazma işlemlerini gerçekleştiren modern otomasyon motoru. (Eski Selenium yapısının yerini aldı).
3. **Behave (BDD):** Davranış Odaklı Geliştirme (Behavior Driven Development) aracı. Testleri yazılımcı olmayanların da okuyabileceği İngilizce (Gherkin) dilinde yazar.

Proje **Page Object Model (POM)** tasarım desenini kullanır. Bu desenin amacı; web sayfalarındaki "Locator"ları (HTML element bulucuları) ve "Action"ları (Tıklama, yazma işlemleri) test senaryolarından ayırarak, kod tekrarını önlemek ve bakımı kolaylaştırmaktır.

### 📂 2. `config` Klasörü (Konfigürasyon)

#### `config/config.json`
Projenin beyni burasıdır. Tüm sabit ve ayarlanabilir değişkenler burada tutulur. Kod içine (hardcode) şifre veya link yazmak yerine buradan çekilir.
* `"base_url"`: Testlerin başlayacağı ana URL (https://www.saucedemo.com/).
* `"browser"`: Testlerin koşulacağı tarayıcı (chrome, firefox, webkit).
* `"username"` & `"password"`: Siteye giriş yapılacak standart test kullanıcısı.
* `"headless"`: `true` ise tarayıcı arkaplanda görünmez çalışır (CI/CD için). `false` ise tarayıcı ekranda açılır (gözle izlemek için).
* `"slow_mode"` & `"step_delay"`: Görsel izlemeyi kolaylaştırmak için Playwright'ın `slow_mo` özelliğine kaç saniye (veya milisaniye) bekleme ekleneceğini belirler.

### 🛠️ 3. `utilities` Klasörü (Yardımcı Araçlar)

Bu klasör, doğrudan testle ilgili olmayan ama sisteme yardımcı olan jenerik kodları barındırır.

#### `utilities/config_reader.py`
* **Amacı:** `config.json` dosyasını okuyan ve içindeki verileri Python nesnesi olarak (`dict`) kodun diğer yerlerine dağıtan sınıftır.
* **Nasıl Çalışır?** `@staticmethod` olarak tanımlanmış metotlar kullanır. `ConfigReader.get_base_url()` çağrıldığında, JSON dosyasını okur ve ilgili değeri döndürür.

#### `utilities/logger.py`
* **Amacı:** Testler çalışırken terminale "Giriş yapıldı", "Sepete tıklandı" gibi loglar basılmasını sağlar. Sadece `print()` kullanmak yerine profesyonel Python `logging` kütüphanesini kullanır. 
* **Nasıl Çalışır?** Zaman damgası (`2026-05-10 23:00 | INFO | ...`) formatıyla çıktı verir.

#### `utilities/screenshot_helper.py`
* **Amacı:** Testler başarısız olduğunda Allure raporu için o anki ekranın resmini `.png` olarak kaydeder. Playwright'a geçişle birlikte ekran görüntüsü alma işlemi `environment.py` içine daha temiz entegre edilmiş olsa da, yardımcı sınıf olarak durmaktadır.

### ⚓ 4. `features` Klasörü (Testlerin Kalbi)

#### `features/environment.py`
* **Amacı:** Testlerin **Öncesinde** ve **Sonrasında** ne olacağını (Hooks) belirler. Projenin en kritik altyapı dosyasıdır.
* **`before_all(context)`:** Tüm test süreci başlamadan 1 kere çalışır. Logger'ı başlatır ve Playwright motorunu (`sync_playwright()`) ayağa kaldırır.
* **`before_scenario(context, scenario)`:** Her bir test senaryosundan (örn: sepete ekleme testi) önce çalışır. Tarayıcıyı açar (`context.browser`), yepyeni ve temiz bir çerez/cache barındıran gizli pencere (context) oluşturur ve sayfayı açar (`context.page`). `slow_mode` ayarı açıksa, tarayıcıyı yavaşlatılmış modda başlatır.
* **`after_scenario(context, scenario)`:** Her test bittiğinde çalışır. Eğer senaryo başarısız (`failed`) olduysa, Playwright üzerinden `context.page.screenshot()` ile fotoğraf çeker ve bunu Allure raporuna gömer (`allure.attach`). Ardından tarayıcıyı tertemiz şekilde kapatır.
* **`after_all(context)`:** Tüm testler bitince Playwright motorunu kapatır.

### 📝 5. `features/*.feature` Dosyaları (Gherkin Senaryoları)

Bu dosyalar, teknik kod değil İngilizce cümlelerdir. Müşteri veya ürün yöneticisi bile okuyabilir.
* **`login.feature`:** Sisteme giriş yapılabilmesini kontrol eder.
* **`cart.feature`:** Ürün ekleme, çoklu ürün ekleme, sepet rozetindeki (badge) sayıların doğruluğunu ve ürün çıkarma işlemlerini doğrular.
* **`checkout.feature`:** End-to-end (Uçtan uca) alışveriş denemesi yapar. Ayrıca kullanıcı adını boş bırakıp ilerlemeye çalışınca hata mesajı (Negative Testing) çıkıp çıkmadığını kontrol eder.
* **`sorting.feature`:** Ürünlerin A'dan Z'ye veya fiyata göre doğru sıralanıp sıralanmadığını test eder.
* **`performance.feature`:** "Sayfa yüklendiği zaman kaydedilsin, yükleme 5 saniyeyi geçiyorsa test fail olsun" diyerek basit yük testleri yapar.

### 🧠 6. `features/steps/*.py` Klasörü (Step Definitions)

Feature dosyalarındaki düz metin İngilizce cümlelerin (`Given`, `When`, `Then`) Python kodundaki karşılıklarıdır.
* **`cart_steps.py`, `checkout_steps.py`, `login_steps.py`, vb.:** 
Buradaki her bir fonksiyonun üzerinde `@when('the user clicks the checkout button')` gibi bağlayıcı bir kelime (decorator) vardır.
* Bu dosyalar asla doğrudan HTML sayfasına müdahale etmez (Locator barındırmaz). Görevleri şudur: Page Object sınıflarını (örneğin `CartPage`) çağırır ve içlerindeki işlemleri tetikler.
* **Assertion (Doğrulama):** `Then` adımlarında `assert` kelimesi kullanılarak, beklenen sonuç ile gerçek sonuç kıyaslanır. Eşit değillerse test patlar ve rapor tutulur.

### 🧱 7. `pages` Klasörü (Page Object Model - POM)

Burası sayfalardaki butonların, kutuların yerlerinin ve onlarla yapılan işlemlerin tanımlandığı yerdir.

#### `pages/base_page.py` (Ana Sınıf)
* **Amacı:** Diğer tüm sayfaların kalıtım (inheritance) alacağı atasıdır. Playwright `page` objesini içine alır.
* **`navigate(url)`:** Verilen linke gider.
* **`click(selector)`:** Verilen CSS stringini (örneğin `"#login-button"`) Playwright ile bulur ve tıklar.
* **`type_text(selector, text)`:** Verilen CSS stringindeki kutuyu bulur ve içine yazıyı `fill()` metoduyla doldurur.
* **`is_element_displayed(selector)`:** Element sayfada görünür mü görünmez mi diye bakar (try-catch bloğu içinde).

#### `pages/login_page.py`
* Sadece Login sayfasıyla ilgilenir. Username kutusu (`#user-name`), password kutusu ve login butonunun konumlarını tutar.
* `login(username, password)` metodu: Sadece bu çağrılarak tüm formu tek kalemde doldurup girmesi sağlanır.

#### `pages/products_page.py`
* Ürünlerin sıralandığı ana sayfa. 
* CSS Locatorları `[data-test='...']` attributelarına göre tanımlanmıştır (Çünkü SauceDemo bu id'leri otomasyon testleri için özel bırakmıştır, değişmezler).
* Sepete ürün ekler, sepet badge'indeki sayıyı okur (`get_cart_badge_count`), filtreleri değiştirir (`select_sort_option`).

#### `pages/cart_page.py`
* Sepet içerisine tıklandığında açılan sayfadır.
* `get_cart_item_count()`: Sepetteki mevcut "öğe" (item) sayısını Playwright'ın `.count()` metoduyla milisaniyeler içinde anında hesaplar.
* Sepetteki silme (`remove`) butonlarına sırayla tıklayarak sepeti boşaltma görevlerini yapar.

#### `pages/checkout_page.py`
* Ödeme adımlarıdır. Form doldurma işlemleri yapar.
* Önceki Selenium versiyonunda React formlarına dışarıdan yazabilmek için Javascript kodları kullanmıştık. Ancak Playwright'a geçince, `self.type_text()` komutu React event'lerini tetiklediği için tüm o karmaşık Javascript hileleri silinmiş ve kod çok sadeleşmiştir.

### 🏃‍♂️ 8. `run_tests.bat` (Çalıştırıcı)

* **Amacı:** Terminalden upuzun Python/Behave komutları girmek yerine tek tıkla testleri çalıştırmaktır.
* İçerisinde `python -m behave --no-capture -f allure_behave.formatter:AllureFormatter -o reports/allure-results` kodu gizlidir.
* İsterseniz yanına klasör/dosya adı girerek filtreleme yapmanızı sağlar (`.\run_tests.bat cart` derseniz sadece Cart testlerini çalıştırır).
* Test bittikten sonra Allure komutunu kullanarak raporları derler ve tarayıcıyı açarak karşınıza rapor görselini getirir.

---

### Sonuç Özeti

Takım arkadaşlarınız `pages` klasörüne baktıklarında hiçbir test kodu görmemelidir (sadece Locatorlar ve sayfa aksiyonları). 
`features` klasörüne baktıklarında sadece insan dilinde cümleler görmelidirler.
`features/steps` klasörüne baktıklarında ise bu cümleleri POM'daki fonksiyonlara bağlayan kısa ve öz köprü kodlar görmelidirler. 

Bu sayede mimari 3 katmana ayrılmış olur ve çok uzun yıllar boyunca kod kalitesi bozulmadan yeni özellikler kolayca eklenebilir.
