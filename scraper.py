import requests 

from bs4 import BeautifulSoup

import csv
requests.get('https://developer.mozilla.org/en-US/docs/Glossary/Python')

response = requests.get('https://developer.mozilla.org/en-US/docs/Glossary/Python')

html_content = response.text

# print(html_content)

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Get all the text elements (paragraphs, headings,....) you want to scrape.
text_elements = soup.find_all(['p', 'title', 'h2', 'footer', 'urls', 'span'])
# results  = soup.find_all('div', class_='page-wrapper')

# # print(results)

scraped_text = ' '.join(element.get_text() for element in text_elements)


# print(scraped_text)

title = ' '.join (title.text for title in soup.find('title'))
# print('Title: ', title)
# print('Title: ', title.get_text())

h2 = soup.find_all('h2')


urls = []

# for link in soup.find_all('a'):
#     urls.append(link.get('href'))
    
# print(urls)

span = ' '.join (span.text for span in soup.find('span'))
# print(span)


footer = ' '.join (footer.text for footer in soup.find('div', class_='page-footer-grid'))
# print(footer)
 

# content  = [content.text for content in soup.find_all('div', class_='section-content')]
content = ' '.join (content.text for content in soup.find_all('p'))
# print(content)


file = open("Parsed_data.txt", "w", encoding='UTF-8')
file.write (title + "\n" + content + "\n" + span + "\n" + footer + "\n")

for link in soup.find_all('a'):
   urls.append(link.get_text('href'))

  
file.write(str(urls))



      
file.close()