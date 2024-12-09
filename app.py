import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import re

# Eğitilen modeli yükle
model_path = "./dilstilgpt2_model"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

# Yıldız derecesini prompt'tan çıkarma
def extract_star_rating(user_input):
    match = re.search(r'\b[1-5]\b', user_input)
    return int(match.group()) if match else None

# Yorum üretme
def generate_review(user_input, max_length=50):
    star_rating = extract_star_rating(user_input)
    if not star_rating:
        return "Geçerli bir yıldız derecesi girin (1-5)."
    prompt = f"Star Rating: {star_rating}\nReview:"
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs.input_ids, max_length=max_length, do_sample=True, temperature=0.7)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Streamlit uygulaması
st.title("Yelp Review Generator")
st.write("Eğitilen DistilGPT-2 modeli ile yıldız derecesine göre yorum oluşturun.")

# Kullanıcıdan giriş al
user_input = st.text_input("Yorum isteğinizi yazın (örnek: '5 yıldızlı yorum yap'):")

if st.button("Yorum Oluştur"):
    review = generate_review(user_input)
    st.write("Oluşturulan Yorum:")
    st.write(review)

import streamlit as st

# Restoran isimleri ve yorumları
restaurants = {
    "Luke": "The raw bar was amazing with fantastic Alaskan crab legs and excellent bread and butter.",
    "Peppermill Reno": "Peppermill is known for its loose slot machines, clean rooms, and diverse on-site dining options.",
    "Santa Barbara": "The shellfish company serves large, delicious rock crab with fresh salad and soup, offering great value.",
    "Mr B's Bistro": "The burger was overcooked, seafood jumbalaya was decent, and the bread pudding was a bit dry.",
    "Surrey's Cafe": "Shrimp and grits were exceptional, and the crab omelette was perfect for a rainy morning."
}

# Sayfa başlığı
st.title("Restoran ve Yorum Analizi")
st.write("Beş farklı restoran arasından bir seçim yapın ve yorumları görün.")

# Restoran seçimi için seçim çubuğu
selected_restaurant = st.selectbox(
    "Bir restoran seçin:",
    options=list(restaurants.keys())
)

# Seçilen restoranın yorumu
if selected_restaurant:
    st.write(f"Seçilen restoran: **{selected_restaurant}**")
    st.write(f"Yorum: *{restaurants[selected_restaurant]}*")
