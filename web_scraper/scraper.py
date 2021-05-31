import requests
from bs4 import BeautifulSoup

url='https://en.wikipedia.org/wiki/History_of_Mexico'

def get_citations_needed_count(url):
    page = requests.get(url)
    # print(page.content)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    return (len(results))


def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    results_parghraphs=[]
    result_one = soup.find('div', class_="mw-parser-output")
    parghraphs = result_one.find_all('p')
    for i in parghraphs:
        j = i.find('span',string = lambda text: 'citation needed' in text)
        if j :
            results_parghraphs.append(i.text.strip())
    return results_parghraphs

if __name__ == "__main__":
    
    