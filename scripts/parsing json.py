import io
import requests
response = requests.get("https://feeds.citibikenyc.com/stations/stations.json")
# print(response)  # if the response is 200, means it is working

data = response.json()
#print(set(data)) # shows the unique key

# print(len(data["stationBeanList"])) # length of the list

# print((data["stationBeanList"]))
with io.open("stationList.csv","w", encoding="utf-8") as f1:
    f1.write("ID"+","+"NAME"+","+"latitude"+"\n")
    for i in range (len(data["stationBeanList"])):
        id = data["stationBeanList"][i]["id"]
        stationName = data["stationBeanList"][i]["stationName"]
        latitude = data["stationBeanList"][i]["latitude"]
        data_row = str(id) + "," + stationName + "," + str(latitude) + "\n"
        f1.write(data_row)
    f1.close()
