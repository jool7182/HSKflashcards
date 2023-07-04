from bs4 import BeautifulSoup
import requests
import pprint


#gets html tags, finds <a> tags
html_text = requests.get('https://mandarinbean.com/new-hsk-6-word-list/').text
soup = BeautifulSoup(html_text)
sites = (soup.find_all('tr'))

vocab_list = []
#puts tags in a list
for words in sites:
    rows = words.find_all('td')
    for tags in rows:
        result = tags.text.strip()
        vocab_list.append(result)



final_list = []
i = 0
while i < len(vocab_list):
    final_list.append(vocab_list[i:i+4])
    i+=4


dict = {}
i = 0
while i < len(final_list):
    dict[final_list[i][1]] = [final_list[i][2],final_list[i][3]]
    i+=1

pprint.pprint(dict)













