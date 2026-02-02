# Yelp Review Intelligence Suite
A compact NLP project that turns raw Yelp reviews into **actionable business summaries**, **rating-aware synthetic reviews**, and **star rating predictions** — packaged with an interactive **Streamlit** demo app.

> Note: Trained model artifacts and the full dataset are not included in this repository due to size limitations.

---

## ✨ What this project does

This repository covers three practical NLP tasks on Yelp restaurant reviews:

1. **Abstractive Summarization (LLM fine-tuning)**  
   - Model: **T5-large**  
   - Goal: Generate a concise “business-level” summary from multiple customer reviews (e.g., aggregating feedback into a short overview).

2. **Rating-Conditioned Review Generation (LLM fine-tuning)**  
   - Model: **DistilGPT-2**  
   - Goal: Generate realistic restaurant review text conditioned on a requested star rating (1–5).

3. **Star Rating Classification (Traditional ML)**  
   - Approach: Sentence embeddings + **Random Forest** classifier  
   - Reported result: ~**75%** test accuracy (as documented in the original work).

---

## 🧱 Repository structure

- `app.py`  
  Streamlit application that runs:
  - Review summarization
  - Rating-conditioned review generation

- `newmind-model-1-and-feature-engineering.ipynb`  
  Data analysis + feature engineering + summarization pipeline (T5 fine-tuning).

- `newmind-model-2.ipynb`  
  Data preparation + embeddings + rating classification + review generation pipeline.

- `Restorant yorum.pdf`  
  Project report/documentation.

---

## 📦 Dataset

- Source: **Yelp Dataset** (via Kaggle)  
- Expected columns used in the notebooks:  
  `stars`, `text`, `business_id`

Dataset link (as referenced in the original README):  
https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset

---

## 🚀 Quickstart (Demo App)

> If you already have the required model checkpoints locally (not stored in this repo), you can run the Streamlit app.

```bash
pip install -r requirements.txt
streamlit run app.py
