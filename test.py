import datetime

x = str(datetime.datetime.now())

stripped_name = x.replace(' ', '').replace(':','').replace('.','').replace('-','')
file_name = stripped_name[0:-6]

with open(f'{file_name}.json', 'w',) as f:
    f.write('{"a": 1, "b": 2}')

