# Movie Recommender System

A content-based recommendation engine that suggests movies to users based on their search history by analyzing genres, keywords, cast, and crew information using the TMDB 5000 Movies Dataset.

---

## 🛠️ Tech Stack

*   **Language:** Python
*   **Machine Learning & Analytics:** NumPy, Pandas, Scikit-learn, NLTK (for stemming)
*   **Frontend & Deployment:** Streamlit, Heroku
*   **Data Source:** TMDB Movie Metadata

---

## 🚀 Key Features

*   **Data Preprocessing:** Cleaned, structured, and transformed movie metadata to combine features into meaningful textual tags.
*   **Vectorization:** Applied `CountVectorizer` (Bag of Words technique) to convert textual movie tags into a multi-dimensional numerical format.
*   **Similarity Metric:** Implemented **Cosine Similarity** to measure the angular distance between movie vectors and identify closest matches.
*   **Recommendation Engine:** Built an optimized function to instantly fetch and display the top 5 most similar movie titles.

---

## 💻 How to Run Locally

Follow these steps to replicate the setup and run the application on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com
cd Movie-Recommendation-System
```

### 2. Install Dependencies
Make sure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

### 3. Run the Application
Launch the Streamlit web server:
```bash
streamlit run app.py
```

---
*Developed as a portfolio project to showcase End-to-End Machine Learning workflows, data engineering, and interactive web application deployment.*

