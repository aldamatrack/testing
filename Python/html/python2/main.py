import requests as r
from bs4 import BeautifulSoup

with open("prove.txt", "a+") as test:
    html_request = r.get(" http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture").text
    soup = BeautifulSoup(html_request, "lxml")
    maintext = soup.find_all("p", class_="paywall")

#working
    for i in maintext:
            try:
                test.write(str(i.text))
            except:
                print("**")
                continue
