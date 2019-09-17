import pandas as pd
path = "/home/dark_matter/MAIN/Projects/Project_X/Project_X/organisedData/d.csv"
data1 = pd.read_csv(path)
notneeded = pd.read_csv("/home/dark_matter/MAIN/Projects/Project_X/Project_X/organisedData/tsp.csv")
l = [['','','','']]
c = 0
for i in range(len(data1)):
    if(data1["info"][i] in notneeded["info"]):
        data1["PresentInTSP"][i] = True
        l.append(list(data1.iloc[[i]]))
        c += 1

df = pd.DataFrame(l)
df.columns = ["name","url","PresentInTSP","info"]
df.to_csv("/home/dark_matter/MAIN/Projects/Project_X/Project_X/organisedData/filteredData.csv")