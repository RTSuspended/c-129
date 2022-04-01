import csv
from wsgiref import headers
data=[]
with open("dataset2.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data.append(row)

header=data[0]
planetdata=data[1:]

for datapoint in planetdata:
    datapoint[2]=datapoint[2].lower()

planetdata.sort(key=lambda planetdata:planetdata[2])
with open("datasetsorted.csv","a+") as f:
    c=csv.writer(f)
    c.writerow(header)
    c.writerows(planetdata)