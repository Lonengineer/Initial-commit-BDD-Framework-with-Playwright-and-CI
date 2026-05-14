# 📚 SauceDemo Playwright & BDD Otomasyon Projesi - Detaylı Ders Notları

Bu doküman, projeyi sıfırdan öğrenmek, kodların mimarisini kavramak ve "neyi, neden yaptık?" sorularına cevap bulmak isteyenler için hazırlanmış kapsamlı bir rehberdir.

---

## 🎯 1. Projenin Amacı ve Test Edilen Site

**Neyi test ediyoruz?**
Projemizin hedefi, standart bir e-ticaret demo sitesi olan **[SauceDemo](https://www.saucedemo.com/)**'nun (Swag Labs) temel fonksiyonlarını otomatik olarak test etmektir. 
E-ticaret sitelerinde kullanıcıların en çok etkileşime girdiği "Giriş yapma, sepete ürün ekleme, sepeti yönetme, filtreleme ve ödeme yapma" gibi kritik senaryoların insan eli değmeden hızlıca doğrulanmasını amaçlıyoruz.

**Neden otomatik test?**
Bir site güncellendiğinde "Acaba sepet bozuldu mu?" diye manuel olarak her defasında sepete ürün eklemek saatler sürer. Yazdığımız bu proje sayesinde saniyeler içinde tüm sitenin sağlığını (Health Check) kontrol edebiliyoruz.

---

## 🛠️ 2. Kullanılan Araçlar, Teknolojiler ve Eklentiler

Projeyi inşa ederken rastgele araçlar seçmedik. Her birinin çok kritik görevleri var:

1. **Python (Programlama Dili):** Okunabilirliğinin yüksek olması ve otomasyon kütüphanelerinin genişliği sebebiyle tercih edildi.
2. **Playwright (Otomasyon Motoru):** 
   - *Neden Selenium değil?* Playwright, modern web siteleri için çok daha hızlıdır. "Auto-wait" (otomatik bekleme) özelliği sayesinde elementin sayfaya yüklenmesini kendi bekler, `time.sleep()` yazma derdinden kurtarır. Ayrıca her test için saniyeler içinde tertemiz bir gizli sekme (Browser Context) açar.
3. **Behave (BDD Framework):**
   - *Neden kullanıyoruz?* Yazdığımız Python kodlarını, yazılımcı olmayanların (Müşteri, Ürün Yöneticisi) bile anlayabileceği İngilizce (Gherkin) diline çevirir. Testleri kod blokları halinde değil, `Given, When, Then` (Verilmişken, Olduğunda, O zaman) mantığıyla hikaye gibi yazarız.
4. **Allure Reports (Raporlama):**
   - *Neden kullanıyoruz?* Konsoldaki siyah beyaz yazılar yerine, yöneticilere sunabileceğimiz interaktif, grafikli ve görsel raporlar üretir. Bir test patladığında ekran görüntüsünü (screenshot) otomatik olarak raporun içine gömer.

---

## 🏗️ 3. Mimari Yapı: Page Object Model (POM)

Projenin en önemli kurallarından biri **POM (Page Object Model)** mimarisini kullanmasıdır.

**Neden bu mimariyi kullandık?**
Eğer login sayfasındaki "Kullanıcı Adı" kutusunun konumunu (Locator) doğrudan testin içine yazsaydık ve yarın sitenin tasarımı değişseydi, 50 farklı testin içine girip o konumu tek tek değiştirmemiz gerekirdi.
**POM ile:** Sayfadaki butonların yerlerini sadece `pages/login_page.py` gibi sayfa nesnesi sınıflarının içine yazarız. Testlerimiz ise bu sınıflara "Giriş yap" der. Butonun yeri değişirse sadece 1 dosyayı güncelleriz, 50 test otomatik olarak düzelir.

Bu mimari; kodu **Bakımı Kolay**, **Okunabilir** ve **Tekrar Edilmeyen (DRY - Don't Repeat Yourself)** hale getirir.

---

## 📂 4. Klasör Yapısı ve Dosyaların Detaylı Görevleri

### ⚙️ `config/` (Ayar Merkezi)
* **`config.json`:** Projenin ayar dosyasıdır. Şifreler, kullanıcı adları, tarayıcı tipi (chrome, firefox) ve sitenin ana adresi burada tutulur. 
  * *Neden?* Testi farklı bir tarayıcıda veya başka bir sitede (örn: test ortamı yerine prod ortamı) koşmak istersek kodlara dokunmadan sadece bu JSON dosyasını değiştiririz. `slow_mode` ayarı ile testleri yavaşlatıp izleyebilir veya `headless` ile görünmez çalıştırabiliriz.

### 🧰 `utilities/` (Yardımcı Araçlar)
Bu klasör testin kendisiyle değil, sistemin çalışmasıyla ilgilenen jenerik araçları tutar.
* **`config_reader.py`:** `config.json` dosyasını okuyup Python'a aktaran köprüdür.
* **`logger.py`:** Test çalışırken konsola "Butona tıklandı", "Sayfaya gidildi" yazılarını tarih ve saat damgasıyla profesyonelce yazdıran sistemdir. 

### 📝 `features/` (Test Hikayeleri)
Burada Gherkin dilinde yazılmış düz metin dosyaları (`.feature`) vardır.
* **Neyi Test Ediyoruz? (Toplam 24 Senaryo, 110 Adım)**
  Şu an projemizde 5 farklı modüle (feature) bölünmüş toplam **24 adet test case (senaryo)** ve **110 test adımı** bulunmaktadır:
  1. `login.feature` (6 Senaryo): Geçerli bilgilerle başarılı giriş yapma ve hatalı/eksik bilgilerle giriş yapmaya çalışma (Negatif Testler).
  2. `cart.feature` (7 Senaryo): Sepete ürün ekleme/çıkarma, sepet rozetini (badge) doğrulama, boş sepetle ödemeye gitme (Negatif Test) ve aynı ürünü çift eklemeyi engelleme (Negatif Test).
  3. `sorting.feature` (4 Senaryo): Ürünleri isme göre (A-Z, Z-A) ve fiyata göre (Ucuz-Pahalı, Pahalı-Ucuz) sıralama.
  4. `checkout.feature` (5 Senaryo): Uçtan uca sipariş tamamlama ve ödeme formunu farklı zorunlu alan kombinasyonları eksik olacak şekilde gönderip hata mesajlarını doğrulama (Negatif Testler).
  5. `performance.feature` (2 Senaryo): Login ve ürünler sayfalarının kabul edilebilir sürede (< 5 sn) yüklendiğini doğrulama.

* **`features/environment.py`:** Sistemin kalbidir. Her testten önce Playwright'ı başlatır, tarayıcıyı açar. Test bitince tarayıcıyı kapatır. Eğer test **başarısız (failed)** olursa, o anki ekranın **fotoğrafını çeker** ve Allure raporuna kaydeder.

### 🔗 `features/steps/` (Köprü Kodlar)
* `login_steps.py`, `cart_steps.py` vb.: Feature dosyasındaki "Kullanıcı login sayfasına gider" cümlesini Python koduna bağlayan yerdir. Buradaki kodlar `pages` klasöründeki sayfaları çağırarak işlemi gerçekleştirir.

### 📄 `pages/` (Sayfa Modelleri - POM'un Uygulandığı Yer)
* **`base_page.py`:** Tüm sayfaların atasıdır. Tıklama (`click`), metin yazma (`type_text`) gibi ortak Playwright fonksiyonlarını barındırır.
* **`login_page.py`:** Sadece login sayfası butonlarını ve "login olma" eylemini içerir.
* **`products_page.py`:** Ürün ana sayfasındaki sepete ekle butonları ve filtreleme menüsü buradadır.
* **`cart_page.py`:** Sepet içi işlemler (Silme butonu vb.)
* **`checkout_page.py`:** Ödeme formu (İsim, soyisim, posta kodu alanları).

---

## 💡 5. Hangi Kodları Neden Yazdık? (Örneklerle Kod Mantığı)

**1. Neden `BasePage` kullanıyoruz?**
Playwright'ta bir butona tıklamak için `page.locator("#buton").click()` yazılır. Ancak biz `BasePage` içine kendi `click` metodumuzu yazdık. Neden? 
Çünkü tıklamadan önce kendi Logger'ımız ile konsola *"#buton elementine tıklandı"* yazdırmak veya hata alırsak özel bir uyarı verdirmek istedik.

**2. `slow_mode` yapısı neden eklendi?**
Playwright o kadar hızlı çalışır ki, tarayıcı açılıp kapanır ve siz ne olduğunu göremezsiniz. Testlerin nereye tıkladığını gözünüzle izlemek ve sunum yapmak için `config.json` içine `slow_mode` ekledik. Bu mod aktifken `environment.py` dosyası Playwright'a `slow_mo=2000` komutunu göndererek her eylemi 2 saniye yavaşlatır.

**3. Performans testi hatasını nasıl çözdük?**
Yakın zamanda `slow_mode: true` açık kaldığı için performans testleri sayfa yavaş yükleniyor sanıp hata verdi. `config.json` üzerinden bu ayarı kapattık, yapay gecikme ortadan kalkınca testler normal hızına döndü ve başarılı (Passed) oldu.

**4. `run_tests.bat` neden var?**
Testleri ve Allure raporunu çalıştırmak için terminale şunu yazmak gerekir: 
`python -m behave --no-capture -f allure_behave.formatter:AllureFormatter -o reports/allure-results`
Kimse bu uzun kodu ezberleyemez. O yüzden bunu bir `.bat` dosyasının içine koyduk. Kullanıcı sadece `.\run_tests.bat` yazar, arka planda tüm raporlar oluşur ve tarayıcıda grafikli sonuç ekranı otomatik açılır.

**5. Neden Negatif Testler Ekledik?**
Gerçek dünyada kullanıcılar her zaman mükemmel veriler girmez. Hatalı şifre denemeleri, form alanlarını boş bırakma veya boş sepetle ödeme yapmaya çalışma gibi sınır/hatalı durumlarında sistemin çökmeden doğru hata mesajını verdiğini doğrulamak, uygulamanın kararlılığı (robustness) için çok kritiktir. Sadece mutlu senaryoları (Happy Path) değil, olumsuz (Negative) senaryoları da test ederek test kapsamımızı (coverage) maksimize ettik.

---

## 🏁 6. Genel Sonuç

Bu proje;
* Değişime direnen (Spaghetti code) bir yapıdan **uzak**,
* Modüler (LEGO gibi parçalara ayrılmış),
* Bakımı kolay,
* Okunabilirliği maksimize edilmiş,
* Modern endüstri standartlarında (Playwright + BDD) bir **Test Otomasyon Framework'üdür.**

Yeni bir test eklenmek istendiğinde HTML yapısı `pages` klasörüne, hikayesi `features` klasörüne, aradaki bağ ise `steps` klasörüne eklenerek sistem hiç bozulmadan sonsuza kadar büyütülebilir.
