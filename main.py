#%%

from bs4 import BeautifulSoup
import requests
from pathlib import Path


#%%
asin = 'B00S3NPKKG'
url = f'https://www.amazon.pl/dp/{asin}'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')


#%%

model_class = soup.find_all(class_='a-size-base prodDetAttrValue')
for elem in model_class:
    if '/' in elem:
        model = elem

#%%

url = f'https://www.philips.pl/c-p/{model}/'
page = requests.get(url)
page = requests.get(str(page.url)+'/pomoc')


#%%

soup = BeautifulSoup(page.text, 'html.parser')


#%%

link_class = soup.find_all('a', href=True, class_=False, target="_blank")


#%%

link_temp = link_class[0]
link_str = str(link_temp).split()[1][6:-1]

#%%

r = requests.get(url, stream=True)


#%%

filename = Path(f'files/{model}.pdf')
response = requests.get(link_str)
filename.write_bytes(response.content)

#%%



