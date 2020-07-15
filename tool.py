import urllib3 as lib
from bs4 import BeautifulSoup

http = lib.PoolManager()
url = input("Enter URL: ")
r = http.request('GET', url)

lst = []
if r.status == 200:
    soup = BeautifulSoup(r.data, 'html.parser')
    a = soup.find_all(class_ = 'comments')

    for number in a:
        lst.append(int(number.text))
    print(sum(lst))
    
else:
    print("Didn't Work :(")