import requests
from bs4 import BeautifulSoup
url = "https://www.brainyquote.com/topics/motivational-quotes"
r = requests.get(url)
# print(r.content)

soap = BeautifulSoup(r.content, 'html5lib')
# table = soap.find('div', attrs={'id': 'quotesList'})
# print(table.prettify())

# now im creating one html file which will contain all html code of given site link
f = open("motivational.html", "w")
f.write(soap.prettify())
f.close()

