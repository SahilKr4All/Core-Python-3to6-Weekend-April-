data = {"id":[101,102,103,104,105],
        "Name":["Ananta","rahul","rishi","anjali","faisal"],
        "class":[9,12,11,10,9],"physics":[78,59,68,85,81],
        "chemistry":[65,55,86,72,70],"maths":[60,68,65,75,85]}

avglist=[]
for i in range(len(data["id"])):
    avg = (data["physics"][i]+data["chemistry"][i]+data["maths"][i])/3
    avglist.append(avg)

data["Average"] = avglist

for i in range(len(data["id"])):
    print(f'{data["id"][i]} {data["Name"][i]} {data["class"][i]} {data["Average"][i]}')
