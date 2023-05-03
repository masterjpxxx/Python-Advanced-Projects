import requests, sys, webbrowser, bs4

from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q='

print('Opening Google....')
response = requests.get(url+ ' '.join(sys.argv[1:]))
print(response.url)

soup = BeautifulSoup(response.text, "html.parser")

print(soup)

search_results = soup.find_all("div", class_="egMi0 kCrYT")
urls = [result.a["href"] for result in search_results]

print(f'the URLS are {urls}')


for url in urls[:5]:
    new_url = url.strip('/url?q=')
    webbrowser.open_new_tab(new_url)