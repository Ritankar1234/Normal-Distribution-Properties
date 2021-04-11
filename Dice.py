import random
import statistics
import plotly.graph_objects as go
diceResult=[]
count=[]
for i in range(0, 1000):
  dice1=random.randint(1, 6)
  dice2=random.randint(1, 6)
  diceResult.append(dice1+dice2)
  count.append(i)
import plotly.express as px
#fig=px.bar(x=diceResult, y=count)
#fig.show()
import plotly.figure_factory as ff 
#fig=ff.create_distplot([diceResult],["result"], show_hist=False)
#fig.show()
mean=statistics.mean(diceResult)
median=statistics.median(diceResult)
mode=statistics.mode(diceResult)
standardDeviation=statistics.stdev(diceResult)
print(mean, median, mode, standardDeviation)
fsds, fsde=mean-standardDeviation, mean+standardDeviation
ssds, ssde=mean-(2*standardDeviation), mean+(2*standardDeviation)
tsds, tsde=mean-(3*standardDeviation), mean+(3*standardDeviation)
fig=ff.create_distplot([diceResult],["result"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.17], mode="lines", name="mean"))
fig.add_trace(go.Scatter(x=[fsds, fsds], y=[0,0.17], mode="lines", name="firstStandardDeviationStart"))
fig.add_trace(go.Scatter(x=[fsde, fsde], y=[0,0.17], mode="lines", name="firstStandardDeviationEnd"))
fig.add_trace(go.Scatter(x=[ssds, ssds], y=[0,0.17], mode="lines", name="secondStandardDeviationStart"))
fig.add_trace(go.Scatter(x=[ssde, ssde], y=[0,0.17], mode="lines", name="secondStandardDeviationEnd"))
fig.add_trace(go.Scatter(x=[tsds, tsds], y=[0,0.17], mode="lines", name="thirdStandardDeviationStart"))
fig.add_trace(go.Scatter(x=[tsde, tsde], y=[0,0.17], mode="lines", name="thirdStandardDeviationEnd"))
fig.show()
listOfDataWithinStandardDeviation1=[result for result in diceResult if result>fsds and result<fsde]
listOfDataWithinStandardDeviation2=[result for result in diceResult if result>ssds and result<ssde]
listOfDataWithinStandardDeviation3=[result for result in diceResult if result>tsds and result<tsde]
print("{}".format(len(listOfDataWithinStandardDeviation1)*100/len(diceResult)))
print("{}".format(len(listOfDataWithinStandardDeviation2)*100/len(diceResult)))
print("{}".format(len(listOfDataWithinStandardDeviation3)*100/len(diceResult)))
