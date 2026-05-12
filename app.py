# ============================================================
# HDFC BANK AI LOAN APPROVAL SYSTEM
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(

    page_title="HDFC AI Loan Approval System",

    page_icon="🏦",

    layout="wide"

)

# ============================================================
# LOAD MODEL
# ============================================================

model = joblib.load("loan_approval_model.pkl")

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""

<style>

/* ============================================================
BACKGROUND
============================================================ */

.stApp {

    background: linear-gradient(
        to right,
        #0f172a,
        #1e293b
    );

    color: white;
}

/* ============================================================
REMOVE HEADER
============================================================ */

header {

    visibility: hidden;
}

/* ============================================================
TITLE
============================================================ */

.main-title {

    font-size: 50px;

    font-weight: bold;

    text-align: center;

    color: #38bdf8;

    margin-top: 10px;
}

/* ============================================================
SUBTITLE
============================================================ */

.sub-title {

    font-size: 20px;

    text-align: center;

    color: #cbd5e1;

    margin-bottom: 40px;
}

/* ============================================================
SECTION TITLES
============================================================ */

.section-title {

    font-size: 24px;

    font-weight: bold;

    color: #38bdf8;

    margin-bottom: 20px;
}

/* ============================================================
LABELS
============================================================ */

label {

    color: white !important;

    font-size: 16px !important;

    font-weight: bold !important;
}

/* ============================================================
INPUTS
============================================================ */

.stNumberInput input {

    background-color: #334155 !important;

    color: white !important;

    border-radius: 10px !important;

    border: 1px solid #38bdf8 !important;
}

/* ============================================================
SELECT BOX
============================================================ */

div[data-baseweb="select"] {

    background-color: #334155 !important;

    color: white !important;

    border-radius: 10px !important;
}

/* ============================================================
SELECTED VALUE
============================================================ */

div[data-baseweb="select"] > div {

    color: white !important;

    background-color: #334155 !important;
}

/* ============================================================
OPTIONS
============================================================ */

li {

    background-color: #1e293b !important;

    color: white !important;
}

/* ============================================================
OPTION HOVER
============================================================ */

li:hover {

    background-color: #2563eb !important;

    color: white !important;
}

/* ============================================================
BUTTON
============================================================ */

.stButton>button {

    background: linear-gradient(
        to right,
        #06b6d4,
        #2563eb
    );

    color: white !important;

    height: 65px;

    width: 100%;

    border-radius: 12px;

    font-size: 22px;

    font-weight: bold;

    border: none;

    margin-top: 20px;
}

/* ============================================================
BUTTON HOVER
============================================================ */

.stButton>button:hover {

    background: linear-gradient(
        to right,
        #0284c7,
        #1d4ed8
    );

    transform: scale(1.02);
}

/* ============================================================
SUCCESS BOX
============================================================ */

.success-box {

    padding: 25px;

    border-radius: 15px;

    background-color: #064e3b;

    color: #d1fae5;

    font-size: 28px;

    font-weight: bold;

    text-align: center;

    margin-top: 30px;
}

/* ============================================================
WARNING BOX
============================================================ */

.warning-box {

    padding: 25px;

    border-radius: 15px;

    background-color: #78350f;

    color: #fef3c7;

    font-size: 28px;

    font-weight: bold;

    text-align: center;

    margin-top: 30px;
}

/* ============================================================
DANGER BOX
============================================================ */

.danger-box {

    padding: 25px;

    border-radius: 15px;

    background-color: #7f1d1d;

    color: #fecaca;

    font-size: 28px;

    font-weight: bold;

    text-align: center;

    margin-top: 30px;
}

/* ============================================================
INFO CARD
============================================================ */

.info-card {

    background-color: #1e293b;

    padding: 20px;

    border-radius: 15px;

    margin-top: 20px;

    border: 1px solid #38bdf8;
}

/* ============================================================
SCROLLBAR
============================================================ */

::-webkit-scrollbar {

    width: 10px;
}

::-webkit-scrollbar-track {

    background: #1e293b;
}

::-webkit-scrollbar-thumb {

    background: #38bdf8;

    border-radius: 10px;
}

</style>

""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================

st.markdown(

    """
    <div class="main-title">
    🏦 HDFC BANK AI LOAN APPROVAL SYSTEM
    </div>
    """,

    unsafe_allow_html=True

)

st.markdown(

    """
    <div class="sub-title">
    AI Powered Banking Risk Assessment & Smart Loan Decision Engine
    </div>
    """,

    unsafe_allow_html=True

)

# ============================================================
# LAYOUT
# ============================================================

col1, col2, col3 = st.columns(3)

# ============================================================
# PERSONAL DETAILS
# ============================================================

with col1:

    st.markdown(

        '<div class="section-title">👤 Personal Details</div>',

        unsafe_allow_html=True

    )

    age = st.slider(

        "Age",

        18,
        70,
        30

    )

    gender = st.selectbox(

        "Gender",

        ['Male', 'Female']

    )

    marital_status = st.selectbox(

        "Marital Status",

        ['Single', 'Married', 'Divorced']

    )

    employment_type = st.selectbox(

        "Employment Type",

        ['Government', 'Private', 'Self Employed', 'Business']

    )

# ============================================================
# FINANCIAL DETAILS
# ============================================================

with col2:

    st.markdown(

        '<div class="section-title">💰 Financial Details</div>',

        unsafe_allow_html=True

    )

    monthly_salary = st.number_input(

        "Monthly Salary",

        10000,
        500000,
        50000

    )

    existing_emi = st.number_input(

        "Existing EMI",

        0,
        200000,
        10000

    )

    savings_balance = st.number_input(

        "Savings Balance",

        0,
        10000000,
        100000

    )

    existing_loan_count = st.slider(

        "Existing Loan Count",

        0,
        10,
        1

    )

# ============================================================
# CREDIT DETAILS
# ============================================================

with col3:

    st.markdown(

        '<div class="section-title">📊 Credit Details</div>',

        unsafe_allow_html=True

    )

    credit_score = st.slider(

        "Credit Score",

        300,
        900,
        700

    )

    cibil_score = st.slider(

        "CIBIL Score",

        300,
        900,
        720

    )

    repayment_history = st.selectbox(

        "Repayment History",

        ['Poor', 'Average', 'Good', 'Excellent']

    )

# ============================================================
# ENCODING MAPS
# ============================================================

gender_map = {

    'Male': 1,
    'Female': 0

}

marital_map = {

    'Single': 2,
    'Married': 1,
    'Divorced': 0

}

employment_map = {

    'Government': 0,
    'Private': 1,
    'Self Employed': 2,
    'Business': 3

}

repayment_map = {

    'Poor': 0,
    'Average': 1,
    'Good': 2,
    'Excellent': 3

}

# ============================================================
# PREDICT BUTTON
# ============================================================

if st.button("🔍 Analyze Loan Eligibility"):

    # ========================================================
    # AUTO FEATURE ENGINEERING
    # ========================================================

    annual_income = monthly_salary * 12

    emi_income_ratio = existing_emi / monthly_salary

    loan_amount = monthly_salary * 20

    savings_balance_log = np.log1p(savings_balance)

    # ========================================================
    # INPUT DATAFRAME
    # ========================================================

    input_data = pd.DataFrame([{

        'Age': age,

        'Gender': gender_map[gender],

        'Marital_Status': marital_map[marital_status],

        'Education': 1,

        'Employment_Type': employment_map[employment_type],

        'Occupation': 0,

        'Monthly_Salary': monthly_salary,

        'Annual_Income': annual_income,

        'Area_Type': 0,

        'Credit_Score': credit_score,

        'Existing_Loan_Count': existing_loan_count,

        'Existing_EMI': existing_emi,

        'Bank_Account_Type': 0,

        'Years_With_Bank': 5,

        'Loan_Type': 0,

        'Property_Ownership': 0,

        'Vehicle_Ownership': 1,

        'CIBIL_Score': cibil_score,

        'Savings_Balance': savings_balance,

        'Transaction_History_Score': 75,

        'Repayment_History': repayment_map[repayment_history],

        'EMI_to_Income_Ratio': emi_income_ratio,

        'Processing_Time_Days': 5,

        'Savings_Balance_Log': savings_balance_log,

        'Loan_Amount': loan_amount,

        'Interest_Rate': 10,

        'Loan_Tenure_Years': 10

    }])

    # ========================================================
    # MATCH TRAINING COLUMN ORDER
    # ========================================================

    input_data = input_data.reindex(

        columns=model.feature_names_in_

    )

    # ========================================================
    # PREDICTION
    # ========================================================

    prediction = model.predict(input_data)[0]

    probability = np.max(

        model.predict_proba(input_data)

    ) * 100

    # ========================================================
    # ELIGIBLE LOAN AMOUNT
    # ========================================================

    full_amount = monthly_salary * 40

    partial_amount = monthly_salary * 20

    # ========================================================
    # OUTPUT LOGIC
    # ========================================================

    # ========================================================
    # FULL APPROVAL
    # ========================================================

    if prediction == 2 and probability >= 90:

        st.markdown(

            f"""
            <div class="success-box">

            ✅ LOAN APPROVED <br><br>

            Confidence Score: {probability:.2f}% <br><br>

            Eligible Loan Amount: ₹{full_amount:,.0f} <br><br>

            Interest Rate: 8.5% <br><br>

            Risk Category: Low Risk

            </div>
            """,

            unsafe_allow_html=True

        )

    # ========================================================
    # PARTIAL APPROVAL
    # ========================================================

    elif prediction == 2 and probability >= 75:

        st.markdown(

            f"""
            <div class="warning-box">

            🟡 PARTIAL APPROVAL <br><br>

            Confidence Score: {probability:.2f}% <br><br>

            Approved Amount: ₹{partial_amount:,.0f} <br><br>

            Reduced Loan Eligibility Applied <br><br>

            Risk Category: Medium Risk

            </div>
            """,

            unsafe_allow_html=True

        )

    # ========================================================
    # CONDITIONAL APPROVAL
    # ========================================================

    elif prediction == 1:

        st.markdown(

            f"""
            <div class="warning-box">

            ⚠️ CONDITIONAL APPROVAL <br><br>

            Confidence Score: {probability:.2f}% <br><br>

            Suggested Loan Amount: ₹{partial_amount:,.0f} <br><br>

            Additional Verification Required <br><br>

            Guarantor / Extra Documents May Be Needed

            </div>
            """,

            unsafe_allow_html=True

        )

    # ========================================================
    # REJECTED
    # ========================================================

    else:

        st.markdown(

            f"""
            <div class="danger-box">

            ❌ LOAN REJECTED <br><br>

            Confidence Score: {probability:.2f}% <br><br>

            Possible Reasons: <br><br>

            • High EMI Burden <br>
            • Low Credit Score <br>
            • Weak Repayment History <br>
            • Financial Risk Detected

            </div>
            """,

            unsafe_allow_html=True

        )

    # ========================================================
    # CUSTOMER SUMMARY
    # ========================================================

    st.markdown(

        f"""
        <div class="info-card">

        <h3 style="color:#38bdf8;">
        📋 Customer Financial Summary
        </h3>

        <hr>

        <b>Monthly Salary:</b> ₹{monthly_salary:,.0f} <br><br>

        <b>Annual Income:</b> ₹{annual_income:,.0f} <br><br>

        <b>Existing EMI:</b> ₹{existing_emi:,.0f} <br><br>

        <b>EMI Ratio:</b> {emi_income_ratio:.2f} <br><br>

        <b>Credit Score:</b> {credit_score} <br><br>

        <b>CIBIL Score:</b> {cibil_score} <br><br>

        <b>Repayment History:</b> {repayment_history}

        </div>
        """,

        unsafe_allow_html=True

    )

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.markdown(

    """
    <center>

    <h4 style='color:#94a3b8;'>

    Developed Using Machine Learning, Random Forest Classifier & Streamlit

    </h4>

    </center>
    """,

    unsafe_allow_html=True

)