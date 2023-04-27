import streamlit as st
import seaborn as sns
import time
df=sns.load_dataset('diamonds')


st.title('This is the title')
agree = st.checkbox(label='I agree')
if agree:
    st.write('Great!')

st.radio('Pick your gender',['Male','Female'])

st.progress(100)

with st.spinner('Wait for it ....'):
    time.sleep(10)