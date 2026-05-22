# 🎓 Student Math Score Prediction App

## 📌 What This Project Solves
Students' academic performance is affected by many factors — not just how hard they study,
but also their background, lunch type, and test preparation. This project predicts a
**student's math score** based on their:
- Reading and writing scores
- Gender and race/ethnicity
- Parental level of education
- Lunch type
- Test preparation course completion

A **Streamlit web app** makes it easy for anyone to enter student details and instantly
get a predicted math score — no coding needed.

---

## 📂 Dataset
- **Features used:**

| Feature | Type | Example |
|---------|------|---------|
| `reading score` | Number | 72.0 |
| `writing score` | Number | 68.0 |
| `gender` | Category | male / female |
| `race/ethnicity` | Category | group A / B / C / D / E |
| `parental level of education` | Category | bachelor's degree |
| `lunch` | Category | standard / free/reduced |
| `test preparation course` | Category | none / completed |

- **Target Column:** `math score` (predicted value out of 100)

---

## 🔄 How the Pipeline Works (Step by Step)

| Step | What Happens |
|------|-------------|
| 1️⃣ Load Data | Reads student performance dataset |
| 2️⃣ Explore Data | Checks shape, columns, missing values |
| 3️⃣ Preprocess | Encodes categorical columns, scales numerical features |
| 4️⃣ Train Model | Trains a regression model to predict math score |
| 5️⃣ Evaluate | Checks accuracy using MAE, RMSE, R² score |
| 6️⃣ Save Model | Saves trained model as `my_trained_model.pkl` using joblib |
| 7️⃣ API | FastAPI endpoint accepts student data and returns prediction |
| 8️⃣ Deploy | Streamlit app lets anyone predict scores interactively |

---

## 🤖 Model Details
- **Type:** Regression (predicts a continuous score 0–100)
- **Input:** 7 features (mix of numbers and categories)
- **Output:** Predicted math score
- **Saved as:** `my_trained_model.pkl`

---

## 🌐 Streamlit Web App

The app has a clean two-column layout where you can:
- Enter **reading score** and **writing score** using number inputs
- Select **gender**, **race/ethnicity**, **parental education**, **lunch**, and **test prep** from dropdowns
- Click **Predict Math Score** to get an instant result
- See a **grade label** (A / B / C / D / F) based on the predicted score
- View an **input summary table** to confirm what was entered

### Example Output:
```
Predicted Math Score: 76.00 / 100
Grade: B — Good!
```

---

## ⚡ FastAPI Endpoint

The project also includes a FastAPI backend for programmatic predictions.

### Run the API:
```bash
uvicorn main:app --reload
```

### Test it at:
```
http://localhost:8000/docs
```

### Example Request:
```json
POST /predict
{
  "reading_score": 72.0,
  "writing_score": 68.0,
  "gender": "male",
  "race_ethnicity": "group C",
  "parental_level_of_education": "bachelor's degree",
  "lunch": "standard",
  "test_preparation_course": "none"
}
```

### Example Response:
```json
{
  "predicted_math_score": 76.00
}
```

---

## 🗂️ Project Files

| File | Purpose |
|------|---------|
| `app.py` | ⭐ Streamlit web app for interactive prediction |
| `main.py` | FastAPI backend with /predict endpoint |
| `my_trained_model.pkl` | Saved trained ML model |
| `requirements.txt` | All required Python libraries |
| `README.md` | Project documentation |

---

## ⚙️ How to Run

### 1. Install Requirements
```bash
pip install -r requirements.txt
```

### 2. Run the Streamlit App
```bash
streamlit run app.py
```
Open browser at: **http://localhost:8501**

### 3. Run the FastAPI Backend
```bash
uvicorn main:app --reload
```
Open browser at: **http://localhost:8000/docs**

---

## 📦 Libraries Used

```
pandas
numpy
scikit-learn
streamlit
fastapi
uvicorn
joblib
pydantic
```

---

## 📊 Grade Scale Used in App

| Score Range | Grade | Label |
|------------|-------|-------|
| 90 – 100 | A | Excellent |
| 75 – 89 | B | Good |
| 60 – 74 | C | Average |
| 40 – 59 | D | Needs Improvement |
| 0 – 39 | F | Poor |

---

## 📝 Key Notes
- Model is trained on student performance data with both numerical and categorical features
- Categorical features are encoded during preprocessing inside the pipeline
- The saved `.pkl` file includes the full pipeline — no separate scaler needed
- FastAPI and Streamlit both load the same `my_trained_model.pkl` file

---

## 👤 Author
Name: Ranjit Damase  Contact Info :9864583081