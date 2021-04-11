import pandas as pd 
import statistics 
import csv 
import plotly.graph_objects as go
import random
import plotly.figure_factory as ff
import plotly.express as px
df=pd.read_csv("height-weight.csv")
heightList=df["Height(Inches)"].tolist()
weightList=df["Weight(Pounds)"].tolist()
heightMean = statistics.mean(heightList)
heightMedian = statistics.median(heightList)
heightMode = statistics.mode(heightList)
standardDeviation = statistics.stdev(heightList)
print(heightMean, heightMedian, heightMode, standardDeviation)
weightMean = statistics.mean(weightList)
weightMedian = statistics.median(weightList)
weightMode = statistics.mode(weightList)
standardDeviationWeight = statistics.stdev(weightList)
print(weightMean, weightMedian, weightMode, standardDeviationWeight)
hfsds, hfsde=heightMean-standardDeviation, heightMean+standardDeviation
hssds, hssde=heightMean-(2*standardDeviation), heightMean+(2*standardDeviation)
htsds, htsde=heightMean-(3*standardDeviation), heightMean+(3*standardDeviation)
wfsds, wfsde=weightMean-standardDeviationWeight, weightMean+standardDeviationWeight
wssds, wssde=weightMean-(2*standardDeviationWeight), weightMean+(2*standardDeviationWeight)
wtsds, wtsde=weightMean-(3*standardDeviationWeight), weightMean+(3*standardDeviationWeight)
hlistOfDataWithinStandardDeviation1=[result for result in heightList if result>hfsds and result<hfsde]
hlistOfDataWithinStandardDeviation2=[result for result in heightList if result>hssds and result<hssde]
hlistOfDataWithinStandardDeviation3=[result for result in heightList if result>htsds and result<htsde]
print("{}".format(len(hlistOfDataWithinStandardDeviation1)*100/len(heightList)))
print("{}".format(len(hlistOfDataWithinStandardDeviation2)*100/len(heightList)))
print("{}".format(len(hlistOfDataWithinStandardDeviation3)*100/len(heightList)))
wlistOfDataWithinStandardDeviation1=[result for result in weightList if result>wfsds and result<wfsde]
wlistOfDataWithinStandardDeviation2=[result for result in weightList if result>wssds and result<wssde]
wlistOfDataWithinStandardDeviation3=[result for result in weightList if result>wtsds and result<wtsde]
print("{}".format(len(wlistOfDataWithinStandardDeviation1)*100/len(weightList)))
print("{}".format(len(wlistOfDataWithinStandardDeviation2)*100/len(weightList)))
print("{}".format(len(wlistOfDataWithinStandardDeviation3)*100/len(weightList)))




