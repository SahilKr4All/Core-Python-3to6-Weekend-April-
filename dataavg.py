data = {"id":[101,102,103,104],"Name":["ashish","Arpit","nikhil","gourav"],
        "physics":[75,85,95,86],"maths":[70,80,90,95]}

avglist=[]
for i in range(len(data["id"])):
    avg = (data["physics"][i]+data["maths"][i])/2
    avglist.append(avg)
    
data["Average"] = avglist

for i in range(len(data["id"])):
    print(f'{data["id"][i]} {data["Name"][i]} {data["Average"][i]}')

import pandas as pd
df = pd.DataFrame(data)
print(df)
