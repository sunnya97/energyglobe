import json
import csv


newdata = {"timeBins":[]}
with open('3letter.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)



#dict = {'a' :0,'b' :0,'c' :0 ,'d':0}

#json_data = {'data': [{'i': 'b', 'e': 'a', 'v': 3}, {'i': 'c', 'e': 'b', 'v': 3}, {'i': 'c', 'e': 'a', 'v': 5},{'i':'d','e':'c','v':3},{'i':'d','e':'a','v':7},{'i':'d','e':'b','v':5}]}

with open('All.json') as data_file:
    json_data=json.load(data_file)
    bigdata = json_data["timeBins"]


for k in bigdata:
    data=k["data"]
    dict={}
    for j in your_list:
        dict[j[0]]=0

    print(len(data))
    for i in data:   
        dict[i['i']] += i['v']
        dict[i['e']] -=i['v']

    posbalance=[]
    negbalance=[]

    for l,v in dict.items():
        if(v>0):
            posbalance.append([l,v])
        elif(v<0):
            negbalance.append([l,-v])


    done = False;

    transactions=[];

    while not done:
        if posbalance[0][1]>negbalance[0][1]:
            transactions.append({'wc':'civ','i':posbalance[0][0],'e':negbalance[0][0],'v':negbalance[0][1]})
            posbalance[0][1]-=negbalance[0][1]
            negbalance[0][1]=0
        
        elif negbalance[0][1]>posbalance[0][1]:
            transactions.append({'wc':'civ','i':posbalance[0][0],'e':negbalance[0][0],'v':posbalance[0][1]})
            negbalance[0][1]-=posbalance[0][1]
            posbalance[0][1]=0
        
        else:
            transactions.append({'wc':'civ','i':posbalance[0][0],'e':negbalance[0][0],'v':negbalance[0][1]})
            posbalance[0][1]=0
            negbalance[0][1]=0
        

        if posbalance[0][1]==0:
            del posbalance[0]
        if negbalance[0][1]==0:
            del negbalance[0]
        if(len(posbalance)==0):
            done=True
    print(len(transactions))
    
    k["data"].extend(transactions)

    
    
newdata["timeBins"]=bigdata
json_str = json.dumps(newdata)
textfile=open("simplifieddata.txt","w")
textfile.write(json_str)
textfile.close()
print(json_str)

    



  

        











    
