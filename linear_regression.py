from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error
from sklearn import linear_model, tree, neighbors
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go


#Main function starts here!
def doML(DataFrame,a,b):
    #This function gets the right columns based on the input
    def select(DataFrame,a):
        count=0
        col=a
        for i in DataFrame.columns:
            if(i==col):
                count+=1
            if(count==0):
                print("Column Doesn't exist ")
            else:
                return DataFrame[col]


    #This sets up the inputs for train_test_split
    df = DataFrame
    c=select(df,a)
    d=select(df,b)
    x = c.values[:, None]
    x_train, x_test, y_train, y_test = train_test_split(
        x, d, random_state=42)

    #Type of models we'll offer
    models = {'Regression': linear_model.LinearRegression,
            'Decision Tree': tree.DecisionTreeRegressor,
            'k-NN': neighbors.KNeighborsRegressor}

    def train_and_display(name):
        model = models[name]()
        model.fit(x_train, y_train)

        #Determines Range
        x_range = np.linspace(x.min(), x.max(), 100)
        y_range = model.predict(x_range.reshape(-1, 1))

        #Creates Figure
        fig = go.Figure([
            go.Scatter(x=x_train.squeeze(), y=y_train, 
                    name='train', mode='markers'),
            go.Scatter(x=x_test.squeeze(), y=y_test, 
                    name='test', mode='markers'),
            go.Scatter(x=x_range, y=y_range, 
                    name='prediction')
        ])
        fig.write_html("/Users/teerathamvitchutripop/Documents/teerathamprojects/sutayjee/test-download")
        print(name)
        return fig

#Testing Area
a="ST"
b="rho"
df=pd.read_csv('Semiconductor T and rho values.csv')
doML(df,a,b)