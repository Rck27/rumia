from bs4 import BeautifulSoup
import requests

# URL of the webpage you want to scrape
url = 'https://www.postel.go.id/faq.htm'

# Send HTTP request to the specified URL and save the response from server in a response object called r
r = requests.get(url)

# Create a BeautifulSoup object and specify the parser library at the same time
soup = BeautifulSoup(r.text, 'html.parser')

# Find all the <li> tags on the webpage
li_tags = soup.find_all('li')

for li in li_tags:
    # Find the <em> tag within each <li> tag
    em_tag = li.find('em')
    if em_tag:
        question = em_tag.text
        print(f'Question: {question}')

    # Find the <p> tag within each <li> tag
    p_tag = li.find('p')
    if p_tag:
        answer = p_tag.text
        print(f'Answer: {answer}')