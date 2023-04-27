## General
Like react it has build process
Like react composable UI; each UI is one function e.g. st.label()
Run this app using : streamlit run app.py
*each* statement will render the component one by one like markdown

## Beginning Code
```python
import streamlit as st
import seaborn as sns
df=sns.load_dataset('diamonds')
```

st.write is omnibus. It can take a text, df, keras, etc.

```python
    st.title('This is the title')
    st.header('This is a header')
    st.write(df)
```
## Widgets are user input controls : buttons, text, sliders
st.checkbox()
st.radio()
st.multiselect()
st.select_slider()
st.slider()

```python
st.title('This is the title')
agree = st.checkbox('I agree')
if agree:
    st.write('Great!')
```
some widget allow context manager
with st.spinner('Wait for it ....'):
    time.sleep(10)

