# NewmindAIFinalCase
Newmind AI Company Bootcamp Final Case study will be here.

# Yelp Yorum Analizi ve Metin Üretimi

Projede iki farklı ipynb ve 1 app.py dosyası vardır. App.py dosyası streamlit arayüzünü sağlayan metin özetleme ve metin üretimi yapan 2 farklı modeli çalıştırır. Metin Özeti 5 farklı restoranın yorumları sonucu ortaya çıkan özetlerdir. Metin Üretimi ise kullanıcının yazdığı 1'den 5'e kadar yıldızlardan yorum üretmesini ister ve model otomatik üretir. 

Model 1 ipynb dosyası veri analizi, veri mühendisliği, veri görselleştirme ve metin özetleme modelini içermektedir.
Model 2 ipynb dosyası veri analizi ve mühendisliğinin tekrar yapıldığı ardından da bağlamsal embedding ile sınıflandırma ve metin üretme modelini içermektedir.

---

## **Proje Özeti**
### 1. **Metin Özetleme**
- Model: **T5-large**
- Amaç: Uzun restoran yorumlarını özetleyerek anahtar bilgileri çıkarmak.
- Yaklaşım: Özetleme için önceden eğitilmiş **T5-large** modeli, yorum verileriyle ince ayar yapılarak (fine-tuning) eğitildi.

### 2. **Metin Üretimi**
- Model: **DistilGPT-2**
- Amaç: Kullanıcı tarafından belirtilen yıldız derecelerine (1–5 yıldız) dayalı yorumlar oluşturmak.
- Yaklaşım: **DistilGPT-2**, şu formatta yapılandırılmış bir veri kümesiyle ince ayar yapılarak eğitildi:

### 3. **Sınıflandırma**
- Model: **Random Forest**
- Amaç: Kullanıcı tarafından belirtilen yıldız derecelerini (1–5 yıldız) sentence transformer ile embedding yaparak random forest makine öğrenmesi sağlanmıştır.
- Sonuç: %75 oranında test sonucu çıkmıştır.
