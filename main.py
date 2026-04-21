



import streamlit as st
import numpy as np
import pandas as pd
import pickle
from keras.models import load_model

# ─── PAGE CONFIG ───
st.set_page_config(
    page_title="Delivery Time Predictor",
    page_icon="🚚",
    layout="centered"
)

# ─── CUSTOM CSS ───
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
}

.stApp {
    background: #0f0f0f;
    color: #f0f0f0;
}

/* Titles */
.main-title {
    font-size: 2.6rem;
    font-weight: 800;
}
.main-sub {
    font-family: 'Space Mono', monospace;
    font-size: 0.8rem;
    color: #888;
    letter-spacing: 2px;
    text-transform: uppercase;
}

/* Section Label */
.section-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.7rem;
    color: #ff6b35;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-top: 1.5rem;
    margin-bottom: 0.5rem;
    border-left: 3px solid #ff6b35;
    padding-left: 10px;
}

/* ─── TIME SECTION CARD FIX ─── */
.section-label + div {
    background: #1a1a1a;
    padding: 1.2rem;
    border-radius: 16px;
    border: 1px solid #2a2a2a;
    margin-bottom: 1rem;
}

/* Inputs */
.stNumberInput input, .stSelectbox div[data-baseweb="select"] {
    background: #1a1a1a !important;
    border: 1px solid #2a2a2a !important;
    border-radius: 8px !important;
    color: #f0f0f0 !important;
    font-family: 'Space Mono', monospace !important;
}
            

/* ─── SLIDER FIX ─── */
.stSlider {
    padding-top: 15px;
}

/* slider track */
.stSlider > div > div {
    height: 6px !important;
    border-radius: 10px !important;
}

/* slider handle */
.stSlider [data-baseweb="slider"] div[role="slider"] {
    width: 16px !important;
    height: 16px !important;
    background: #ff6b35 !important;
    border-radius: 50% !important;
    border: 2px solid #0f0f0f !important;
}

/* Buttons */
.stButton > button {
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)

# ─── LOAD MODELS ───
@st.cache_resource
def load_artifacts():
    scaler = pickle.load(open("scaler.pkl", "rb"))
    model = load_model("model.keras")
    cols = pickle.load(open("cols.pkl", "rb"))
    return scaler, model, cols

scaler, model, cols = load_artifacts()

# ─── TITLE ───
st.markdown('<div class="main-title">🚚 Delivery Time</div>', unsafe_allow_html=True)
st.markdown('<div class="main-sub">Porter AI · Delivery Predictor</div>', unsafe_allow_html=True)
st.markdown("---")

# ─── RESET ───
def reset_all():
    for key in list(st.session_state.keys()):
        del st.session_state[key]

# ─── CATEGORIES ───
categories = ['afghan','african','american','indian','italian','mexican','chinese','japanese','fast','pizza','burger','sushi','thai','vietnamese','other']

# ─── INPUTS ───
st.markdown('<div class="section-label">📦 Order Info</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    total_items = st.number_input("Total Items", 1, 50, 3)
    subtotal = st.number_input("Subtotal", 0.0, 10000.0, 2000.0)
with col2:
    num_distinct_items = st.number_input("Distinct Items", 1, 50, 3)
    min_item_price = st.number_input("Min Price", 0.0, 5000.0, 200.0)

max_item_price = st.number_input("Max Price", 0.0, 5000.0, 800.0)

# ─── PARTNER INFO ───
st.markdown('<div class="section-label">🛵 Partner Info</div>', unsafe_allow_html=True)

col3, col4, col5 = st.columns(3)
with col3:
    onshift = st.number_input("Onshift", 0.0, 100.0, 10.0)
with col4:
    busy = st.number_input("Busy", 0.0, 100.0, 5.0)
with col5:
    orders = st.number_input("Outstanding", 0.0, 100.0, 5.0)

# ─── TIME INFO ───
st.markdown('<div class="section-label">🕐 Time Info</div>', unsafe_allow_html=True)

col6, col7 = st.columns(2)
with col6:
    hour = st.slider("Hour", 0, 23, 12)
with col7:
    day = st.slider("Day (Mon=0)", 0, 6, 2)

# ─── RESTAURANT ───
st.markdown('<div class="section-label">🏪 Restaurant</div>', unsafe_allow_html=True)

col8, col9, col10 = st.columns(3)
with col8:
    category = st.selectbox("Category", categories)
with col9:
    market_id = st.selectbox("Market", [1,2,3,4,5,6])
with col10:
    protocol = st.selectbox("Protocol", [1,2,3,4,5,6,7])

st.markdown("---")

# ─── BUTTONS ───
col_btn1, col_btn2 = st.columns([3,1])
with col_btn1:
    predict = st.button("🔮 Predict")
with col_btn2:
    st.button("Reset", on_click=reset_all)

# ─── PREDICTION ───
if predict:
    data = {
        'total_items': total_items,
        'subtotal': subtotal,
        'num_distinct_items': num_distinct_items,
        'min_item_price': min_item_price,
        'max_item_price': max_item_price,
        'total_onshift_partners': onshift,
        'total_busy_partners': busy,
        'total_outstanding_orders': orders,
        'hour': hour,
        'day': day,
        'store_primary_category': category,
        'market_id': market_id,
        'order_protocol': protocol
    }

    df = pd.DataFrame([data])
    df = pd.get_dummies(df, columns=['store_primary_category','market_id','order_protocol'])

    for col in cols:
        if col not in df.columns:
            df[col] = 0

    df = df[cols]

    scaled = scaler.transform(df)
    pred = model.predict(scaled)

    st.markdown(f"""
    <div style="background:#1a1a1a;padding:2rem;border-radius:16px;text-align:center;border:1px solid #ff6b35;">
        <div style="font-size:3rem;color:#ff6b35;font-weight:700;">
            {pred[0][0]:.0f} min
        </div>
        <div style="color:#888;letter-spacing:3px;font-size:0.8rem;">
            ESTIMATED DELIVERY TIME
        </div>
    </div>
    """, unsafe_allow_html=True)
