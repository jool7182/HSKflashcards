import json
mydict = {
    "values": [
        {
            "name": "Bob",
            "profession": "slave"
        }
    ]
}



names = ['mike', 'jason', 'alex']
professions = ['worker', 'king', 'servant']



for i in range(3):
    y= names[i]
    z= professions[i]
    x={y: z}
    mydict["values"].append(x)
print(mydict)

json_string = json.dumps(mydict)
with open('yoma.json', 'w',) as f:
    f.write(json_string)
