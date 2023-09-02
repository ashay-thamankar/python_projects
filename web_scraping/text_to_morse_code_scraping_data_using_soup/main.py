# Programme to get the data from Morse code world website and convert user text to morse code

from bs4 import BeautifulSoup
import requests

url_link = 'https://morsecode.world/international/morse2.html'
response = requests.get(url_link).text

soup = BeautifulSoup(response, "html.parser")

all_tables = soup.select('.small-12 table')
letter = []
code = []
for tabel in all_tables[:5]:
    all_inside = (tabel.select('tbody tr')[1:])
    for inside in all_inside:
        letter.append(inside.find(class_='tile').text)
        code.append(inside.select('td')[1].text)

user_text = input('Enter the text (can use letter, digit, punctuation mark, accented letter): ')

final_result = []
for text in user_text.upper():
    try:
        in_index = letter.index(text)
        final_result.append(code[in_index])
    except ValueError:
        print(f'{text} was not in the list and it is skipped')
print(f'the user input is : {user_text}')
print(f'the morse code is : {final_result}')
