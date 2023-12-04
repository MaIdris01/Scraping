import requests 

from bs4 import BeautifulSoup


# gets the URL
requests.get('https://developer.mozilla.org/en-US/docs/Glossary/Python')

response = requests.get('https://developer.mozilla.org/en-US/docs/Glossary/Python')

html_content = response.text


# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")



urls = []

# Get all the text elements (title, content,....) you want to scrape.

title = ' '.join (title.text for title in soup.find('title'))

span = ' '.join (span.text for span in soup.find('span'))

footer = ' '.join (footer.text for footer in soup.find('div', class_='page-footer-grid'))

content = ' '.join (content.text for content in soup.find_all('p'))


file = open("Parsed_data.txt", "w", encoding='UTF-8')
file.write (title + "\n" + content + "\n" + span + "\n" + footer + "\n")

for link in soup.find_all('a'):
   urls.append(link.get_text('href'))

  
file.write(str(urls))


file.close()