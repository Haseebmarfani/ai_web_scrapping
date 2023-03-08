from bs4 import BeautifulSoup
import requests
import openai
requests.get('https://www.w3.org/MarkUp/Guide/')
url = requests.get('https://www.w3.org/MarkUp/Guide/').text
soup = BeautifulSoup(url, 'html.parser')
import json

# Load JSON data from config file
with open('config.json', 'r') as f:
    config = json.load(f)

def open_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as infile:
        return infile.read()

def save_file(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as outfile:
        outfile.write(data)
        
#div = soup.find('div', attrs={'class':'hh hi hj hk hl'})

text = soup.find_all('p')[3].text   
print(text)

        
    
docs = open('data.txt', 'a', encoding='utf-8')
docs.write(text)
docs.close()

openai.api_key = config['api_key']

feed = open_file('data.txt')
prompt = open_file('prompt.txt').replace('<<FEED>>', feed)

response = openai.Completion.create(
    model = 'text-davinci-002',
    prompt = prompt,
    temperature = 1.0,
    max_tokens = 100,
    top_p = 1,
    frequency_penalty = 0.0,
    presence_penalty = 0.0
)

text = response['choices'][0]['text'].strip()
print(prompt)
print(text)

save_file('output.txt', text)
prompt1 = open_file('output.txt')

response = openai.Image.create(
    prompt = prompt1 + ('digital illustration, 8k, sharp foucs'),
    n=1,
    size = "1024x1024"
)

image_url = response['data'][0]['url']

URL = image_url
response = requests.get(URL)
open('image.png', 'wb').write(response.content)


