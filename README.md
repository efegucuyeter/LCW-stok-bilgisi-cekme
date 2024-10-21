# LCW Ürün Stok Bilgisi Çekme Uygulaması

### Özellikler

- Web sayfasından ürün fiyat ve stok bilgilerini çeker.
- Excel dosyasına yazar.
- Ürün bulunamadığında hata kaydı ekler.
- Tarayıcı her ürün için baştan açılır ve kapatılır, bu sayede bellek sızıntılarından kaçınılır.

------------

### Kurulum

#### 1- Gerekli Bağımlılıkları Yükleyin

Aşağıdaki komutla proje bağımlılıklarını yükleyebilirsiniz:
`pip install -r requirements.txt`

#### 2- WebDriver İndirin
Bu uygulama Selenium WebDriver kullanır. Tarayıcınıza uygun WebDriver'ı indirip sistem PATH'ine eklemeniz gerekmektedir.(Kaynak dosyaların içinde ekli hali mevcuttur.)

##### Güncel ChromeDriver dosyasına [buradan](https://developer.chrome.com/docs/chromedriver/downloads "buradan") ulaşabilirsiniz.
#### 3- Kodu Başlatın

Aşağıdaki komutu kullanarak Python dosyasını çalıştırın:
`python main.py`
------------
# Nasıl çalışır
1-Kodu çalıştırın ardından görselde de gözüken **Dosya Seç** butonuna  tıklayın.

![Ekran görüntüsü 2024-10-21 154237](https://github.com/user-attachments/assets/8b40e527-921d-4985-9b27-44f676f9a17f)


2-Aşağıdaki gibi bir xlsx tablosu oluşturun ve uygulamada açılan pencereye yükleyin.(Örnek tablo kodlarda mevcuttur. )

|Link   |
| ------------ |
| https://www.lcw.com/standart-kalip-kapusonlu-erkek-yagmurluk-haki-o-3349957  |
|  https://www.lcw.com/standart-kalip-kapusonlu-erkek-yagmurluk-haki-o-3349957 |
|   https://www.lcw.com/standart-kalip-kapusonlu-erkek-yagmurluk-haki-o-3349957|


3-Dosyayı seçtikten sonra **Stok Bİlgisi Çek** butonuna tıklayın.

4- **Başlandı...**   **Veriler Excel dosyasıına kaydedildi.** yazılarından sonra  kod bulunduğu yere  **urun_stok_bilgisi.xlsx** dosyasını kayıt eder ve  dosya aşağıdaki gibi gözükür.

| Ürün Linki  | Fiyat  |  Beden | Stok  |
| ------------ | ------------ | ------------ | ------------ |
|https://www.lcw.com/standart-kalip-kapusonlu-erkek-yagmurluk-haki-o-3349957   |  899,99 TL |  S  |   0|
|  https://www.lcw.com/standart-kalip-kapusonlu-erkek-yagmurluk-haki-o-3349957 | 899,99 TL  |  M |   0|
| https://www.lcw.com/standart-kalip-kapusonlu-erkek-yagmurluk-haki-o-3349957  | 899,99 TL  |  L |     0|
|  https://www.lcw.com/standart-kalip-kapusonlu-erkek-yagmurluk-haki-o-3349957 | 899,99 TL  |  XL |   0|

------------


# Exe Formatına Çevirmek

#### 1- Gerekli Kütüphaneyi Yükleyin

Aşağıdaki komutla gerekli kütüphaneleri yükleyebilirsiniz:

`pip install pyinstaller`

### 2- Terminale Gerekli Kodu Yazın
Aşağıdaki komudu kullanabilirsiniz

`pyinstaller --onefile --noconsole --add-binary"driver-yolu;./" main.py`

##### Oluşturulan main.exe dosyası dist/ klasöründe bulunacaktır.
