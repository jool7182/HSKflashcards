import json
import datetime


results = '''
{
    "words": [
        {   
            "vocab": "中国", 
            "answer": "Correct"
        },
        {
            "vocab": "爱好",
            "answer": "Correct"
        }
    ]
}
'''

data = json.loads(results)
json_string = json.dumps(data)

initial = str(datetime.datetime.now())

stripped_name = initial.replace(' ', '').replace(':','').replace('.','').replace('-','')
file_name = stripped_name[0:-6]

with open(f'{file_name}.json', 'w',) as f:
    f.write(json_string)

print(data)