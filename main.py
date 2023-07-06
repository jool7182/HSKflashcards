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
with open(f'C:\\Users\\Joshua\\Desktop\\pyscripts\\flash_cards\\results\\{hsk_choice}_accuracy.json', 'r') as f1:
    data1 = f1.read()

#Creating variables
accuracy_data = json.loads(data1)
accuray_term_list = list(accuracy_data.keys())
accuracy_score_list = []


#Creating % value and Avoiding divide by zero
for i in accuracy_data:
    if accuracy_data[i][1] > 0:
        pct = accuracy_data[i][0] / accuracy_data[i][1]
        accuracy_score_list.append(pct)
    else:
        pct = 0.0
        accuracy_score_list.append(pct)
         
#Creating term:accuracy% dictionary        
terms_dict = {}
i = 0
while i < len(accuray_term_list):
    terms_dict[accuray_term_list[i]] = accuracy_score_list[i]
    i+=1

#Sorting dictionary + Sorted lists
new_accuracy_dict = dict(sorted(terms_dict.items(), key=lambda item: item[1]))
sorted_term_list = list(new_accuracy_dict.keys())
sorted_score_list = []

#Inverting % score into weight value
for i in new_accuracy_dict:
    x = new_accuracy_dict[i]
    if x < 0.1:
        x = 0.1
    new_value = 1 / x
    sorted_score_list.append(new_value)

#Preparing variables
results = {"terms": [], "score": ''}
word_list = []
answer_list = []



#Main Loop
while True:
    #Choosing/Displaying English Term
    current_term = random.choices(sorted_term_list, weights=sorted_score_list)[0]
    print(current_term)
    English_answer = input('''Press enter to show answer:
     ''')
    if English_answer == 'quit':
        break
    print('Answer:', selected_data[current_term][1], '  |||  Pinyin:', selected_data[current_term][0])
    
    while True:
        correct_or_incorrect = input('Correct? (y/n) >')
        if correct_or_incorrect == 'y' or correct_or_incorrect == 'n':
            #we're happy with the value given.
            #we're ready to exit the loop.
            break
        else:
            print("Please enter a valid response.")
            continue
            

    
    if correct_or_incorrect == 'y':
        word_list.append(current_term)
        answer_list.append(True)
        accuracy_data[current_term][0] = accuracy_data[current_term][0] + 1       
    elif correct_or_incorrect == 'n':
        word_list.append(current_term)
        answer_list.append(False)
    else:
        print("Unknown Error")
 
    accuracy_data[current_term][1] = accuracy_data[current_term][1] + 1    
    print('------------------------------------')


#Creating saved results
for i in range(len(word_list)):
    y= word_list[i]
    z= answer_list[i]
    x={y: z}
    results["terms"].append(x)

#Creating End of Test list
print('------------------------------------')
print('Test Results:')
end_test_list = []
end_test_correct_answers = 0
i = 0
while i < len(word_list):
    if answer_list[i] == True:
        end_test_list.append(f'{word_list[i]},  :  Correct' )
        end_test_correct_answers +=1
    elif answer_list[i] == False:
        end_test_list.append(f'{word_list[i]},  :  Incorrect' )
    else:
        print('Error')
    i+=1
  

#Displaying End of test list
i=0
while i < len(end_test_list):
    print(end_test_list[i])
    i+=1 
print(f'Total score: {end_test_correct_answers} / {len(end_test_list)}')
results['score'] = f'Total score: {end_test_correct_answers} / {len(end_test_list)}'
print('------------------------------------')
print('Test complete. Saving results...')

#Updating accuracy report
finished_data = json.dumps(accuracy_data, indent=2)
with open(f'C:\\Users\\Joshua\\Desktop\\pyscripts\\flash_cards\\results\\{hsk_choice}_accuracy.json', 'w') as f2:
    f2.write(finished_data)

#Creating File name
x = str(datetime.datetime.now())
stripped_name = x.replace(' ', '').replace(':','').replace('.','').replace('-','')
file_name = stripped_name[0:-6]

#Storing results
json_string = json.dumps(results, indent=2)
with open(f'C:\\Users\\Joshua\\Desktop\\pyscripts\\flash_cards\\results\\{hsk_choice}_results\\{file_name}{hsk_choice}.json', 'w') as f:
    f.write(json_string)
 
