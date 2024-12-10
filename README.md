# NewmindAIFinalCase
Newmind AI Company Bootcamp Final Case study will be here.

# Yelp Yorum Analizi ve Metin Üretimi

Projede iki farklı ipynb ve 1 app.py dosyası vardır. App.py dosyası streamlit arayüzünü sağlayan metin özetleme ve metin üretimi yapan 2 farklı modeli çalıştırır. Metin Özetleme LLM Modeli 5 farklı restoranın yorumları sonucu ortaya çıkan restorant hakkındaki özetlerdir. Metin Üretme LLM Modeli ise restorantlara yazılan yorumlara karşılık gelen 1'den 5'e kadar olan yıldızlar(yorumların puanlamasını) ile eğitilmiştir. Streamlit Prompt satırına kullanıcı 1 yıldızlı yorumdan 5 yıldızlı yoruma kadar tüm yıldızları içeren yorum üretmesini isteyebilir ve model bu istek üzerine istenilen yıldız sayısına göre yorum üretir.

![image](https://github.com/user-attachments/assets/1195edfa-ae22-43aa-9863-a0444c86092b)
Data Verisi Stars, Text, Business ID kolonları

newmind-model-1-and-feature-engineering.ipynb dosyası veri analizi, veri mühendisliği, veri görselleştirme ve metin özetleme modelini içermektedir.
newmind-model-2.ipynb dosyası veri analizi ve mühendisliğini Model-1.ipynb dosyası gibi tekrardan yapar ardından da bağlamsal embedding ile sınıflandırma ve metin üretme modelini oluşturur.

---

## **Proje Özeti**
### 1. **Metin Özetleme**
- Model: **T5-large**
- Amaç: Uzun restoran yorumlarını özetleyerek anahtar bilgileri çıkarmak.
- Yaklaşım: Özetleme için önceden eğitilmiş **T5-large** modeli, yorum verileriyle ince ayar yapılarak (fine-tuning) eğitildi.

### 2. **Metin Üretimi**
- Model: **DistilGPT-2**
- Amaç: Kullanıcı tarafından belirtilen yıldız derecelerine (1–5 yıldız) dayalı yorumlar oluşturmak.
- Yaklaşım: **DistilGPT-2**, şu formatta yapılandırılmış bir veri kümesiyle ince ayar yapılarak eğitildi.

### 3. **Sınıflandırma**
- Model: **Random Forest**
- Amaç: Kullanıcı tarafından belirtilen yıldız derecelerini (1–5 yıldız) sentence transformer ile embedding yaparak random forest makine öğrenmesi sağlanmıştır.
- Sonuç: %75 oranında test sonucu çıkmıştır.

  
# Model ve veri setleri boyutlarından ötürü eklenememiştir.
Veri Seti linki: https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset
