# NewmindAIFinalCase
Newmind AI Company Bootcamp Final Case study will be here.

# Yelp Yorum Analizi ve Metin Üretimi

Bu proje, Yelp restoran yorumlarını analiz etmeyi ve yıldız derecelerine dayalı yorumlar üretmeyi amaçlamaktadır. Proje iki ana görevi içerir: **T5-large** ile özetleme ve **DistilGPT-2** ile metin üretimi.

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
