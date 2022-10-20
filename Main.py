from unicodedata import name
from cv2 import mean, trace
import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv
import plotly.graph_objects as go

df=pd.read_csv("Data.csv")
data=df["temp"].tolist()
population_mean=statistics.mean(data)
SD=statistics.stdev(data)
print("population mean :" ,population_mean,"Standard devitation :",SD)


def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    fig=ff.create_distplot([data],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
    fig.show()

def random_set_of_mean(counter):
    dataset=[]
    for i in range (0,counter):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    SD=statistics.stdev(dataset)

    return mean

def setup():
    mean_list=[]
    for i in range (0,1000):
        set_of_mean=random_set_of_mean(100)
        mean_list.append(set_of_mean)
    show_fig(mean_list)

setup()

def StandardDeviation():
    mean_list=[]
    for i in range(0,100):
        set_of_mean=random_set_of_mean(50)
        mean_list.append(set_of_mean)
    SD=statistics.stdev(mean_list)
    print("SD of Sampling distrubution",SD)
StandardDeviation()






