



# import streamlit as st
# import numpy as np
# import pandas as pd
# import pickle
# from tensorflow.keras.models import load_model

# # Page Config 
# st.set_page_config(
#     page_title="Delivery Time Predictor",
#     page_icon="🚚",
#     layout="centered"
# )

# # Custom CSS 
# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;700;800&display=swap');

# html, body, [class*="css"] {
#     font-family: 'Syne', sans-serif;
# }

# .stApp {
#     background: #0f0f0f;
#     color: #f0f0f0;
# }

# h1, h2, h3 {
#     font-family: 'Syne', sans-serif !important;
#     font-weight: 800 !important;
# }

# .stApp > header { background: transparent !important; }

# .main-title {
#     font-family: 'Syne', sans-serif;
#     font-size: 2.6rem;
#     font-weight: 800;
#     color: #f0f0f0;
#     letter-spacing: -1px;
#     margin-bottom: 0rem;
# }
# .main-sub {
#     font-family: 'Space Mono', monospace;
#     font-size: 0.8rem;
#     color: #888;
#     margin-bottom: 2rem;
#     letter-spacing: 2px;
#     text-transform: uppercase;
# }

# .section-label {
#     font-family: 'Space Mono', monospace;
#     font-size: 0.7rem;
#     color: #ff6b35;
#     letter-spacing: 3px;
#     text-transform: uppercase;
#     margin-top: 1.5rem;
#     margin-bottom: 0.5rem;
#     border-left: 3px solid #ff6b35;
#     padding-left: 10px;
# }

# .stNumberInput input, .stSelectbox div[data-baseweb="select"] {
#     background: #1a1a1a !important;
#     border: 1px solid #2a2a2a !important;
#     border-radius: 8px !important;
#     color: #f0f0f0 !important;
#     font-family: 'Space Mono', monospace !important;
# }

# .stSlider > div > div { background: #2a2a2a !important; }
# .stSlider > div > div > div { background: #ff6b35 !important; }

# /* Predict Button */
# div[data-testid="column"]:nth-child(1) .stButton > button {
#     width: 100%;
#     background: #ff6b35 !important;
#     color: #0f0f0f !important;
#     font-family: 'Syne', sans-serif !important;
#     font-weight: 700 !important;
#     font-size: 1rem !important;
#     border: none !important;
#     border-radius: 10px !important;
#     padding: 0.75rem 1.5rem !important;
#     letter-spacing: 1px !important;
#     transition: all 0.2s ease !important;
# }
# div[data-testid="column"]:nth-child(1) .stButton > button:hover {
#     background: #ff8c5a !important;
#     transform: translateY(-2px) !important;
#     box-shadow: 0 8px 25px rgba(255, 107, 53, 0.35) !important;
# }

# /* Reset Button */
# div[data-testid="column"]:nth-child(2) .stButton > button {
#     width: 100%;
#     background: transparent !important;
#     color: #888 !important;
#     border: 1px solid #2a2a2a !important;
#     border-radius: 10px !important;
#     font-family: 'Syne', sans-serif !important;
#     font-size: 0.85rem !important;
#     padding: 0.75rem !important;
#     transition: all 0.2s ease !important;
# }
# div[data-testid="column"]:nth-child(2) .stButton > button:hover {
#     border-color: #555 !important;
#     color: #f0f0f0 !important;
#     background: #1a1a1a !important;
# }

# hr { border-color: #1a1a1a !important; }

# .result-box {
#     background: linear-gradient(135deg, #1a1a1a, #222);
#     border: 1px solid #ff6b35;
#     border-radius: 16px;
#     padding: 2rem;
#     text-align: center;
#     margin-top: 1.5rem;
# }
# .result-time {
#     font-family: 'Space Mono', monospace;
#     font-size: 3.5rem;
#     font-weight: 700;
#     color: #ff6b35;
#     line-height: 1;
# }
# .result-label {
#     font-family: 'Space Mono', monospace;
#     font-size: 0.7rem;
#     color: #888;
#     letter-spacing: 3px;
#     text-transform: uppercase;
#     margin-top: 0.5rem;
# }
# </style>
# """, unsafe_allow_html=True)

# #Load Files  
# @st.cache_resource
# def load_artifacts():
#     scaler = pickle.load(open("scaler.pkl", "rb"))
#     model = load_model("model.h5")
#     cols = pickle.load(open("cols.pkl", "rb"))
#     return scaler, model, cols

# scaler, model, cols = load_artifacts()

# # Title 
# st.markdown('<div class="main-title">🚚 Delivery Time</div>', unsafe_allow_html=True)
# st.markdown('<div class="main-sub">Porter AI · Delivery Predictor</div>', unsafe_allow_html=True)
# st.markdown("---")

# # Reset Function 
# def reset_all():
#     for key in list(st.session_state.keys()):
#         del st.session_state[key]

# # Categories  
# categories = [
#     'afghan', 'african', 'alcohol', 'alcohol-plus-food', 'american',
#     'argentine', 'asian', 'barbecue', 'belgian', 'brazilian', 'breakfast',
#     'british', 'bubble-tea', 'burger', 'burmese', 'cafe', 'cajun',
#     'caribbean', 'catering', 'cheese', 'chinese', 'chocolate', 'comfort-food',
#     'convenience-store', 'dessert', 'dim-sum', 'ethiopian', 'european',
#     'fast', 'filipino', 'french', 'gastropub', 'german', 'gluten-free',
#     'greek', 'hawaiian', 'indian', 'indonesian', 'irish', 'italian',
#     'japanese', 'korean', 'kosher', 'latin-american', 'lebanese', 'malaysian',
#     'mediterranean', 'mexican', 'middle-eastern', 'moroccan', 'nepalese',
#     'other', 'pakistani', 'pasta', 'persian', 'peruvian', 'pizza', 'russian',
#     'salad', 'sandwich', 'seafood', 'singaporean', 'smoothie', 'soup',
#     'southern', 'spanish', 'steak', 'sushi', 'tapas', 'thai', 'turkish',
#     'vegan', 'vegetarian', 'vietnamese'
# ]

# #Inputs 
# st.markdown('<div class="section-label">📦 Order Info</div>', unsafe_allow_html=True)
# col1, col2 = st.columns(2)
# with col1:
#     total_items       = st.number_input("Total Items", min_value=1, max_value=50, value=3, key="total_items")
#     subtotal          = st.number_input("Subtotal (Rs)", min_value=0.0, max_value=10000.0, value=2000.0, key="subtotal")
# with col2:
#     num_distinct_items = st.number_input("Distinct Items", min_value=1, max_value=50, value=3, key="num_distinct_items")
#     min_item_price    = st.number_input("Min Item Price", min_value=0.0, max_value=5000.0, value=200.0, key="min_item_price")

# max_item_price = st.number_input("Max Item Price", min_value=0.0, max_value=5000.0, value=800.0, key="max_item_price")

# st.markdown('<div class="section-label">🛵 Partner Info</div>', unsafe_allow_html=True)
# col3, col4, col5 = st.columns(3)
# with col3:
#     total_onshift_partners   = st.number_input("Onshift Partners", min_value=0.0, max_value=100.0, value=10.0, key="total_onshift_partners")
# with col4:
#     total_busy_partners      = st.number_input("Busy Partners", min_value=0.0, max_value=100.0, value=5.0, key="total_busy_partners")
# with col5:
#     total_outstanding_orders = st.number_input("Outstanding Orders", min_value=0.0, max_value=100.0, value=5.0, key="total_outstanding_orders")

# st.markdown('<div class="section-label">🕐 Time Info</div>', unsafe_allow_html=True)
# col6, col7 = st.columns(2)
# with col6:
#     hour = st.slider("Order Hour (0–23)", 0, 23, 12, key="hour")
# with col7:
#     day  = st.slider("Day of Week (Mon=0)", 0, 6, 2, key="day")

# st.markdown('<div class="section-label">🏪 Restaurant Info</div>', unsafe_allow_html=True)
# col8, col9, col10 = st.columns(3)
# with col8:
#     store_primary_category = st.selectbox("Category", categories, key="store_primary_category")
# with col9:
#     market_id      = st.selectbox("Market ID", [1.0, 2.0, 3.0, 4.0, 5.0, 6.0], key="market_id")
# with col10:
#     order_protocol = st.selectbox("Order Protocol", [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0], key="order_protocol")

# st.markdown("---")

# # ─── Buttons  ───
# col_btn1, col_btn2 = st.columns([3, 1])
# with col_btn1:
#     predict_clicked = st.button("🔮 Predict Delivery Time")
# with col_btn2:
#     st.button("↺  Reset", on_click=reset_all)

# # ─── Prediction Logic 
# if predict_clicked:
#     input_dict = {
#         'total_items': total_items,
#         'subtotal': subtotal,
#         'num_distinct_items': num_distinct_items,
#         'min_item_price': min_item_price,
#         'max_item_price': max_item_price,
#         'total_onshift_partners': total_onshift_partners,
#         'total_busy_partners': total_busy_partners,
#         'total_outstanding_orders': total_outstanding_orders,
#         'hour': hour,
#         'day': day,
#         'store_primary_category': store_primary_category,
#         'market_id': market_id,
#         'order_protocol': order_protocol,
#     }

#     input_df = pd.DataFrame([input_dict])
#     input_df = pd.get_dummies(input_df, columns=[
#         'store_primary_category', 'order_protocol', 'market_id'
#     ])

#     for col in cols:
#         if col not in input_df.columns:
#             input_df[col] = 0

#     input_df    = input_df[cols]
#     input_scaled = scaler.transform(input_df)
#     pred         = model.predict(input_scaled)
#     minutes      = pred[0][0]

#     st.markdown(f"""
#     <div class="result-box">
#         <div class="result-time">{minutes:.0f} min</div>
#         <div class="result-label">Estimated Delivery Time</div>
#     </div>
#     """, unsafe_allow_html=True)












import streamlit as st
import numpy as np
import pandas as pd
import pickle
from tensorflow.keras.models import load_model

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
    model = load_model("model.h5")
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
