# 🚚 Porter Delivery Time Predictor

A deep learning project that predicts the **estimated delivery time (in minutes)** of a food order, built as a case study on Porter, India's largest marketplace for intra-city logistics. The trained neural network is served through an interactive **Streamlit** web app.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-Neural%20Network-D00000?logo=keras&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Preprocessing-F7931E?logo=scikit-learn&logoColor=white)

---

## 📌 Problem Statement

Porter works with a wide range of restaurants and has many delivery partners available to deliver food to customers. To give customers a reliable ETA, Porter wants to estimate the delivery time based on:

- **What** is being ordered (items, prices, subtotal)
- **Where** it is ordered from (restaurant category, market)
- **Who** can deliver it (partner availability and current load)

This project builds a **regression model using a neural network** to predict the delivery time from these factors.

---

## ✨ Features

- 📊 Full EDA: data shape, data types, missing values, outliers and visualisations
- 🛠️ Feature engineering: delivery time (in minutes) derived from `created_at` and `actual_delivery_time`
- 🔡 Categorical encoding (one-hot) and feature scaling
- 🧠 Neural network regression model with hyperparameter tuning
- 📈 Evaluation on train, validation and test data
- 🌐 Interactive Streamlit app with a dark, modern UI
- 🔮 Instant delivery time prediction from user inputs

---

## 🗂️ Dataset

The data lives in `porter.csv`.

| Column | Description |
|---|---|
| `market_id` | Integer id of the market where the restaurant lies |
| `created_at` | Timestamp when the order was placed |
| `actual_delivery_time` | Timestamp when the order was delivered |
| `store_primary_category` | Category of the restaurant |
| `order_protocol` | Integer code for how the order was placed (via Porter, call to restaurant, pre-booked, third party, etc.) |
| `total_items` | Total number of items in the order |
| `subtotal` | Final price of the order |
| `num_distinct_items` | Number of distinct items in the order |
| `min_item_price` | Price of the cheapest item |
| `max_item_price` | Price of the costliest item |
| `total_onshift_partners` | Delivery partners on duty when the order was placed |
| `total_busy_partners` | Delivery partners busy with other tasks |
| `total_outstanding_orders` | Total orders waiting to be fulfilled at that moment |

**Target:** delivery time in minutes = `actual_delivery_time − created_at`

---

## 🔬 Project Workflow

1. **Problem definition and EDA**
   - Shape and data types of all attributes
   - Missing value detection
   - Outlier detection
   - Data visualisation
2. **Preprocessing and feature engineering**
   - Create the target column (delivery time in minutes)
   - Missing value and outlier treatment
   - Encode categorical columns
   - Feature scaling
3. **Model building (Keras / TensorFlow)**
   - Neural network regression model
   - Architecture design
   - Trying different hyperparameter combinations
   - Model training
4. **Evaluation**
   - Compare performance on train, validation and test sets
   - Insights and recommendations

The full analysis is available in [`main.ipynb`](main.ipynb).

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Data handling | NumPy, Pandas |
| Preprocessing | scikit-learn (scaler) |
| Deep learning | Keras / TensorFlow |
| Web app | Streamlit |
| Notebook | Jupyter |

---

## 📁 Project Structure

```
Porter-Case-Study/
├── main.ipynb         # EDA, preprocessing, model building and evaluation
├── main.py            # Streamlit app for live predictions
├── porter.csv         # Dataset
├── model.keras        # Trained neural network
├── scaler.pkl         # Fitted feature scaler
├── cols.pkl           # Column order used during training
├── requirements.txt   # Python dependencies
├── tasks.txt          # Case study problem statement and tasks
└── README.md
```

---

## ⚙️ Installation

**1. Clone the repository**

```bash
git clone https://github.com/muzzammil03/Porter-Case-Study.git
cd Porter-Case-Study
```

**2. (Optional) Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

> 💡 If Keras complains about a missing backend, also run `pip install tensorflow`.

---

## 🚀 Usage

### Run the web app

```bash
streamlit run main.py
```

The app opens at `http://localhost:8501`.

### Using the app

Fill in the order details and click **🔮 Predict** to get the estimated delivery time. Use **Reset** to clear all inputs.

| Section | Inputs |
|---|---|
| 📦 Order Info | Total items, subtotal, distinct items, min and max item price |
| 🛵 Partner Info | Onshift partners, busy partners, outstanding orders |
| 🕐 Time Info | Hour of day (0–23), day of week (Mon = 0 … Sun = 6) |
| 🏪 Restaurant | Category, market id, order protocol |

### Explore the analysis

```bash
jupyter notebook main.ipynb
```

---

## 🧠 How the Prediction Works

1. User inputs are collected into a single-row DataFrame.
2. `store_primary_category`, `market_id` and `order_protocol` are one-hot encoded.
3. Any missing dummy columns are added with value `0`, and columns are reordered to match `cols.pkl`.
4. Features are scaled using the saved `scaler.pkl`.
5. `model.keras` predicts the delivery time, shown in minutes.

---

## 📊 Results

> Add your final metrics here after running the notebook.

| Dataset | MAE | RMSE | R² |
|---|---|---|---|
| Train | – | – | – |
| Validation | – | – | – |
| Test | – | – | – |

---

## 🔭 Future Improvements

- Add distance and weather features
- Try other models (XGBoost, LightGBM) for comparison
- Deploy the app on Streamlit Community Cloud
- Add model monitoring and automatic retraining

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 👤 Author

**Muzzammil**
GitHub: [@muzzammil03](https://github.com/muzzammil03)

---

⭐ If you found this project useful, please give it a star!
