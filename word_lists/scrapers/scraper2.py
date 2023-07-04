from bs4 import BeautifulSoup
import requests
import pprint


#gets html tags, finds <a> tags
html_text = requests.get('https://www.omgchinese.com/new-hsk/band7/words').text
soup = BeautifulSoup(html_text)
sites = (soup.find_all('tr'))

vocab_list = []
#puts tags in a list
for words in sites:
    rows = words.find_all('td')
    for tags in rows:
        result = tags.text.strip()
        vocab_list.append(result)


second_list = []
i = 0
while i < len(vocab_list):
    second_list.append(vocab_list[i:i+4])
    i+=4

i =0
while i < len(second_list):
    second_list[i].pop()
    line_split = second_list[i][1].splitlines()
    second_list[i].pop(1)
    second_list[i].insert(1, line_split[0])
    second_list[i].insert(2, line_split[1])
    i+=1


dict = {}
i = 0
while i < len(second_list):
    dict[second_list[i][1]] = [second_list[i][2],second_list[i][3]]
    i+=1

print(dict)
