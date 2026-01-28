# 🎬 Movie Recommendation System

This is a **content-based movie recommendation system** that recommends similar movies based on user selection.  
The system uses **cosine similarity** on movie feature vectors and displays movie posters using the **TMDB API**.

---

## 🚀 Features
- Recommend similar movies
- Content-based filtering
- Movie poster fetching using TMDB API
- Simple and interactive UI built with Streamlit

---

## 🧠 How It Works
1. Movie metadata is vectorized
2. Cosine similarity is calculated between movies
3. When a user selects a movie, the most similar movies are recommended
4. Posters are fetched dynamically using the TMDB API

---

## 📦 About `.pkl` Files

This project uses serialized `.pkl` files (such as `similarity.pkl`) to store precomputed similarity matrices.

These files are **intentionally excluded** from the repository because:
- They are large in size and exceed GitHub's file size limits
- They can be easily regenerated from the source code
- Version-controlling generated artifacts is not a recommended practice

To recreate the file locally, run the similarity computation code provided in the project.

This approach keeps the repository lightweight, reproducible, and aligned with best practices in machine learning engineering.

---
## 🛠 Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- TMDB API

---

## ▶️ How to Run Locally

1. Clone the repository
```bash
git clone https://github.com/irfan-pathan-09/movie-recommendation-system.git
