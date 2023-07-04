import random
import datetime
import json


with open('C:\\Users\\Joshua\\Desktop\\pyscripts\\flash_cards\\word_lists\\jsonvocab.json', 'r') as f:
    data = f.read()
read_data = json.loads(data)

hsk_choice = input('which test would you like to study? >')
selected_data = read_data[hsk_choice][0]

with open('test.json', 'r') as f1:
    data1 = f1.read()
read_data1 = json.loads(data1)

print(read_data1)

for i in read_data1:
    read_data1[i][1] = read_data1[i][1] + 1

finished_data = json.dumps(read_data1, indent=2)

with open('test.json', 'w') as f2:
    f2.write(finished_data)
""" 
results = {"terms": []}
word_list = []
answer_list = []
vocab = list(selected_data.keys())

while True:
    n = random.randrange(0,len(selected_data)) 

    current_term = vocab[n]
    print(current_term)


    English_answer = input('''Press enter to show answer:
     ''')
    if English_answer == 'quit':
        break
    print('Answer:', selected_data[current_term][1], '  |||  Pinyin:', selected_data[current_term][0])
    correct_or_incorrect = input('Correct? (y/n) >')
    if correct_or_incorrect == 'y':
        word_list.append(current_term)
        answer_list.append(True)       
    elif correct_or_incorrect == 'n':
        word_list.append(current_term)
        answer_list.append(False)
    else:
        print("I don't understand")
 
        

    print('----------------------------')
 """