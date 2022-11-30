"""
Simple Classifying App using the Iris Dataset
"""

import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Iris Classifier App Demo

Predicts Iris **flower type** using the ***Iris*** dataset from sklearn
""")

st.sidebar.header("Use Input")

def user_input_features():
    sepal_length = st.sidebar.slider("Sepal Length", 3.0, 10.0, 5.0)
    sepal_width = st.sidebar.slider("Sepal Width", 1.0, 5.0, 3.0)
    petal_length = st.sidebar.slider("Petal Length", 1.0, 9.0, 5.0)
    petal_width = st.sidebar.slider("Petal Width", 0.0, 5.0, 3.0)
    data = {
        "Sepal Length":sepal_length,
        "Sepal Width":sepal_width,
        "Petal Length":petal_length,
        "Petal Width":petal_width,
    }
    user_input_feature_df = pd.DataFrame(data, index=[0])
    return user_input_feature_df

df = user_input_features()

st.subheader("User Input")
st.write(df)

iris = datasets.load_iris()
X = iris.data
y = iris.target

rf_classifier = RandomForestClassifier()
rf_classifier.fit(X,y)

y_pred = rf_classifier.predict(df)


st.subheader("Predicted Iris Flower Type")
st.write(iris.target_names[y_pred])

