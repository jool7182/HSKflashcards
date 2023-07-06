import json
import random

#Opening File
with open ('C:\\Users\\Joshua\\Desktop\\pyscripts\\flash_cards\\results\\hsk2_accuracy.json', 'r') as f:
    read_file = f.read()
data = json.loads(read_file)


term_list = list(data.keys())
score_list = []


#Creating % value and Avoiding divide by zero
for i in data:
    if data[i][1] > 0:
        pct = data[i][0] / data[i][1]
        score_list.append(pct)
    else:
        pct = 0.0
        score_list.append(pct)
         
#Creating term:accuracy% dictionary        
terms_dict = {}
i = 0
while i < len(term_list):
    terms_dict[term_list[i]] = score_list[i]
    i+=1

#Sorting dictionary + Sorted lists
new = dict(sorted(terms_dict.items(), key=lambda item: item[1]))
sorted_term_list = list(new.keys())
sorted_score_list = []

#Inverting % score into weight value
for i in new:
    x = new[i]
    if x < 0.1:
        x = 0.1
    new_value = 1 / x
    sorted_score_list.append(new_value)


print(random.choices(sorted_term_list, weights=sorted_score_list, k=15))



