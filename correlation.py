import plotly.express as px
import pandas as pd
import csv
import numpy as np

def getSource(data_path):
    marks=[]
    days_present=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row['Marks In Percentage']))
            days_present.append(float(row['Days Present']))
        
    return{"x":marks,"y":days_present}

def getCorrelation(datasource):
    correlation=np.corrcoef(datasource['x'],datasource['y'])
    print('Correlation between Marks and Days Present is:',correlation[0,1])
def plotFigure():
    df=pd.read_csv('data1.csv')
    fig=px.scatter(df,x='Marks In Percentage',y='Days Present')
    fig.show()
def setup():
    data_path='./data1.csv'
    datasource=getSource(data_path)
    getCorrelation(datasource)
    plotFigure()

setup()