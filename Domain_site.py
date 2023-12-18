import requests

from bs4 import BeautifulSoup

requests.get('https://www.domain.com/')

response = requests.get('https://www.domain.com/')

html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

title = ' '.join (title.text for title in soup.find('title'))

div = ' '.join (div.text for div in soup.find('div', class_='responsivecolumns'))

span = ' '.join (span.text for span in soup.find_all('span'))

body = ' '.join (body.text for body in soup.find_all('body', class_='page basicpage'))

header2 = ' '.join (header2.text for header2 in soup.find('span', class_='rte__48px--900'))

h2 = ' '.join (h2.text for h2 in soup.find('span', class_='rte__26px--300'))

div2 = ' '.join (div.text for div in soup.find_all('div', class_='itl teaser section'))

div3 = ' '.join (div3.text for div3 in soup.find('div', class_='accordion panelcontainer'))

div4 = ' '.join (div4.text for div4 in soup.find_all('div', class_='rte text section'))

div5 = ' '.join (div5.text for div5 in soup.find('span', class_='rte__14px--900'))

footer = ' '.join (footer.text for footer in soup.find('div', class_='footer__colGroup--2'))

with open("Domain_data.txt", 'w') as file:
  file.write(title + "\n" + div + "\n" + header2 + "\n" + h2 + "\n" + div2 + "\n" + div3 + "\n" + div4 + "\n" + div5 + "\n" + footer)
