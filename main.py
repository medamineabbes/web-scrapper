import requests
from bs4 import BeautifulSoup
def get_name_and_price(url):
    page=requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.select_one("span[data-name*=price]")
    price = results.text
    result = soup.select_one("h1[data-name*=adview_title]")
    name = result.text
    return (name,price);

def main():
    needed_url="https://www.tayara.tn"
    mainpageurl = "https://www.tayara.tn/sc/v%C3%A9hicules/voitures"
    r = requests.get(mainpageurl)
    aa = BeautifulSoup(r.content, 'html.parser')
    d = aa.find_all('div', 'card')
    for i in d:
        url=needed_url+i.a['href']
        (name,price)=get_name_and_price(url)
        print("(name::" + name + ") and  price:: (" + price + ")")

main()