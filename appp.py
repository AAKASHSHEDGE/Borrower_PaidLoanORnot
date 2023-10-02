import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Prediction on borrower will paid there loan or not")

# brand
credit_policy = st.selectbox('credit.policy  (the given person is eligiable for loan or not 1 means yes and 0 means NO)',df['credit.policy'].unique())

# type of laptop
Interset_rate = st.slider('The interest rate of the loan, as a proportion (a rate of 11% would be stored as 0.11).',0.1,0.05,0.20)

# Ram
instalment = st.slider('The monthly installments owed by the borrower if the loan is funded in hundred',0,50,1000)

# weight
log_annual_inc = st.slider('Annual income in __ Lakh',0,1,30)

# Touchscreen
dti = st.slider('The debt-to-income ratio of the borrower (amount of debt divided by annual income)',0,0,20)

# IPS
fico = st.slider('credit score',0,300,900)

days_with_cr_line = st.slider('The number of days the borrower has had a credit line.',0,1000,20000)


revol_bal = st.slider('The borrowers revolving balance',0,0,50000)

revolutil = st.slider('The borrowers revolving line utilization rate ',0,0,100)

inq_last_6mths	 = st.slider('The borrowers number of inquiries by creditors in the last 6 months',0,0,10)

delinq_2yrs = st.slider('The number of times the borrower had been 30+ days past due on a payment in the past 2 years',0,0,10)

pub_rec = st.selectbox('The borrowers number of derogatory public records (bankruptcy filings, tax liens, or judgments)',df['credit.policy'].unique())

purpose_credit_card = st.selectbox('purpose_credit_card',df['credit.policy'].unique())

purpose_debt_consolidation = st.selectbox('purpose_debt_consolidation',df['credit.policy'].unique())

purpose_educational = st.selectbox('purpose_educational',df['credit.policy'].unique())

purpose_home_improvement = st.selectbox('purpose_home_improvement',df['credit.policy'].unique())

purpose_major_purchase = st.selectbox('purpose_major_purchasel',df['credit.policy'].unique())

purpose_small_business = st.selectbox('purpose_small_business',df['credit.policy'].unique())

#p = int((math.exp(sum([0.00233296*-0.00981062672*2 - 0.000191703064*2- 0.0000256662466*1+0.0182*2+0.0028315-0.0033546-0.0000156+0.01235+0.0002364+0.002564-0.00200+0.002536-0.00251+0.0002558-0.002465+0.001315-0.002565-0.002465])))/(1+math.exp(sum([0.00233296*-0.00981062672*2 - 0.000191703064*2- 0.0000256662466*1+0.0182*2+0.0028315-0.0033546-0.0000156+0.01235+0.0002364+0.002564-0.00200+0.002536-0.00251+0.0002558-0.002465+0.001315-0.002565-0.002465]))))





if st.button('Predict Performance'):


    query = np.array([credit_policy,Interset_rate,instalment,log_annual_inc,dti,fico,days_with_cr_line,revol_bal,revolutil,
    inq_last_6mths,delinq_2yrs,pub_rec,purpose_credit_card,purpose_debt_consolidation,purpose_educational,purpose_home_improvement,
    purpose_major_purchase,purpose_small_business])

    query = query.reshape(1,18)
    st.subheader("1 : Borrower will not paid the loan")
    st.subheader("0 : Borrower will paid the loan")
    st.title("Borrower will :" + str(int((pipe.predict(query)[0]))))