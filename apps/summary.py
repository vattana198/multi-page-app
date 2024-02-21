import streamlit as st
import pandas as pd
from sklearn import datasets

def app():
    st.title('Iris Dataset Summary')
    iris = datasets.load_iris()

    X = pd.DataFrame(iris.data, columns = iris.feature_names)
    Y = pd.Series(iris.target, name = 'class')

    df = pd.concat([X,Y], axis=1)
    df['class'] = df['class'].map({0:"setosa", 1:"versicolor", 2:"virginica"})

    summary = df.describe(include='all')
    st.write(summary)

# Call the app function
if __name__ == "__main__":
    app()