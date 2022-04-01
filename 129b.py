import csv
data1=[]
data2=[]

with open("final.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data1.append(row)

header1=data1[0]
planetdata1=data1[1:]

with open("datasetsorted.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data2.append(row)

header2=data2[0]
planetdata2=data2[1:]
headers=header1+header2
planetdata=[]
for index,datarow in enumerate(planetdata1):
    planetdata.append(planetdata1[index]+planetdata2[index])

with open("totallyfinal.csv","a+") as f:
    c=csv.writer(f)
    c.writerow(headers)
    c.writerows(planetdata)