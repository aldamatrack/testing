from bs4 import BeautifulSoup
import requests as r

title = []

with open("titlebody.txt", "w") as testo:
    html_site = r.get("https://www.nytimes.com/").text
    soup = BeautifulSoup(html_site, "html.parser")
    for body in soup.find_all("section", class_="story-wrapper"):

        try:
            if body.a.h3:
                testo.write((str(body.a.h3.text)))
                testo.write("\n")
        except:
                print("***")
                continue

testo.close()
