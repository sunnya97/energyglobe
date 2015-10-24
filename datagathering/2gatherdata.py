import requests
import json
import csv


with open('5letter.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('coors_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        fiveletters = {rows[0]:rows[1] for rows in reader}

with open('3letter.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('coors_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        threeletters = {rows[0]:rows[1] for rows in reader}


output_list = []


country = "RUSSIAN FEDERATION"

exporter = threeletters[country]
print(exporter)

url = 'http://atlas.media.mit.edu/hs92/export/2010/' +exporter+ '/show/2709/'

r = requests.get(url)
parsed_json = r.json()["data"]


for i in parsed_json:
    if "export_val" in i.keys() and i["dest_id"] in fiveletters.keys():
        output_list += [{"i": fiveletters[i["dest_id"]], "wc": "cru", "e": country, "v": int(i["export_val"])}]

print(output_list)


final_json = '[{"data": ' + str(output_list) + ', "t": 2010}'

print(final_json)

text_file = open("Output.txt", "w")

text_file.write(final_json)

text_file.close()