import plotly.express as px
import pandas as pd
import csv
import numpy as np

def getSource(data_path):
    coffee=[]
    sleep=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for f in csv_reader:
            coffee.append(float(f['Coffee in ml']))
            sleep.append(float(f['sleep in hours']))
        
    return{"x":coffee,"y":sleep}

def getCorrelation(datasource):
    correlation=np.corrcoef(datasource['x'],datasource['y'])
    print('Correlation between Amount of Sleep and Amount of Coffee drank is:',correlation[0,1])
def plotFigure():
    df=pd.read_csv('data2.csv')
    fig=px.scatter(df,x='Coffee in ml',y='sleep in hours')
    fig.show()
def setup():
    data_path='./data2.csv'
    datasource=getSource(data_path)
    getCorrelation(datasource)
    plotFigure()
setup()