import requests
from bs4 import BeautifulSoup
facts = []
def soup():
    res = requests.get("https://www.boldtuesday.com/blogs/travel/facts-about-the-world-that-will-blow-your-mind")
    soup = BeautifulSoup(res.text, "lxml")
    sections = soup.find_all("p")
    short = sections[1:] 
    for section in short:
        facts.append(section.get_text(strip=True))
    return facts


ffacts = soup()

with open('facts.txt', 'w') as f:
    for fact in ffacts:
        f.write(fact + "\n")
