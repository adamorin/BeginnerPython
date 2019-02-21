import pandas as pd
import matplotlib.pyplot as mp
import numpy

def makeNewSeries(ID, times, volts, kwh):
    dic = {"Time": times, "Voltage": volts, "KWH": kwh}
    df = pd.DataFrame(data = dic)
    print("New dataframe for ID" + str(prevId))
    return df

data = pd.read_csv("Fake Voltage Data - Sheet2.csv")

#print(data)

#data.plot()

prevId = -1

frames = []
times = []
volts = []
kwh = []
for index, row in data.iterrows():
    currId = row["ID"]
    if currId != prevId:
        if len(times) > 0:
            df = makeNewSeries(prevId, times, volts, kwh)
            frames.append(df)
        times = [row["Time"]]
        volts = [row["Voltage"]]
        kwh = [row["KWH"]]
        prevId = currId
    else:
        times.append(row["Time"])
        volts.append(row["Voltage"])
        kwh.append(row["KWH"])
        
df = makeNewSeries(prevId, times, volts, kwh)
frames.append(df) 

for f in frames:
    mp.plot(f["Time"], f["Voltage"] ) 
mp.show()     
        
