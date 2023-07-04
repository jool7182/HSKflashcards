#option for vocabulary/pinyin
#Option to select multiple groups of flash cards
#Keep track of most missed words
#Track the accuracy percentage of each word
#Fix the I don't understand to re=ask y/n


import random
import datetime
import json

#Getting the list of all words
with open('C:\\Users\\Joshua\\Desktop\\pyscripts\\flash_cards\\word_lists\\jsonvocab.json', 'r') as f:
    data = f.read()
read_data = json.loads(data)

#Choosing an HSK Level
hsk_choice = input('which test would you like to study? >')
selected_data = read_data[hsk_choice][0]

#Opening the accuracy file
with open('C:\\Users\\Joshua\\Desktop\\pyscripts\\flash_cards\\results\\hsk1_accuracy.json', 'r') as f1:
    data1 = f1.read()
accuracy_data = json.loads(data1)

#Preparing variables
results = {"terms": []}
word_list = []
answer_list = []
vocab = list(selected_data.keys())

#Main Loop
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
        accuracy_data[current_term][0] = accuracy_data[current_term][0] + 1       
    elif correct_or_incorrect == 'n':
        word_list.append(current_term)
        answer_list.append(False)
    else:
        print("I don't understand")
 
    accuracy_data[current_term][1] = accuracy_data[current_term][1] + 1    
    print('----------------------------')


#Creating results
print('Test complete. Saving results...')
for i in range(len(word_list)):
    y= word_list[i]
    z= answer_list[i]
    x={y: z}
    results["terms"].append(x)

#Updating accuracy report
finished_data = json.dumps(accuracy_data, indent=2)
with open('C:\\Users\\Joshua\\Desktop\\pyscripts\\flash_cards\\results\\hsk1_accuracy.json', 'w') as f2:
    f2.write(finished_data)

#Creating File name
x = str(datetime.datetime.now())
stripped_name = x.replace(' ', '').replace(':','').replace('.','').replace('-','')
file_name = stripped_name[0:-6]

#Storing results
json_string = json.dumps(results, indent=2)
if hsk_choice == 'hsk1':
    with open(f'C:\\Users\\Joshua\\Desktop\\pyscripts\\flash_cards\\results\\hsk1_results\\{file_name}{hsk_choice}.json', 'w') as f:
        f.write(json_string)
elif hsk_choice == 'hsk2':
    with open(f'C:\\Users\\Joshua\\Desktop\\pyscripts\\flash_cards\\results\\hsk2_results\\{file_name}{hsk_choice}.json', 'w') as f:
        f.write(json_string)
elif hsk_choice == 'hsk3':
    with open(f'C:\\Users\\Joshua\\Desktop\\pyscripts\\flash_cards\\results\\hsk3_results\\{file_name}{hsk_choice}.json', 'w') as f:
        f.write(json_string)
elif hsk_choice == 'hsk4':
    with open(f'C:\\Users\\Joshua\\Desktop\\pyscripts\\flash_cards\\results\\hsk4_results\\{file_name}{hsk_choice}.json', 'w') as f:
        f.write(json_string)
elif hsk_choice == 'hsk5':
    with open(f'C:\\Users\\Joshua\\Desktop\\pyscripts\\flash_cards\\results\\hsk5_results\\{file_name}{hsk_choice}.json', 'w') as f:
        f.write(json_string)
elif hsk_choice == 'hsk6':
    with open(f'C:\\Users\\Joshua\\Desktop\\pyscripts\\flash_cards\\results\\hsk6_results\\{file_name}{hsk_choice}.json', 'w') as f:
        f.write(json_string)
elif hsk_choice == 'hsk789':
    with open(f'C:\\Users\\Joshua\\Desktop\\pyscripts\\flash_cards\\results\\hsk789_results\\{file_name}{hsk_choice}.json', 'w') as f:
        f.write(json_string)

