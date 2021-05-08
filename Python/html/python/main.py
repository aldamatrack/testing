from bs4 import BeautifulSoup
import requests as r

title = []

with open("titlebody.txt", "w") as testo:
    html_site = r.get("https://www.nytimes.com/").text
    soup = BeautifulSoup(html_site, "html.parser")
    for body in soup.find_all("section", class_="story-wrapper"):
        #testobody.write(str(body))
        #testobody.write("\n\n")

        #print(body.a)
        try:
            if body.a.h3:
                print("i \n")
                testo.write((str(body.a.h3.text)))
                testo.write("\n")

            elif body.a.h3.span:
                print("ii \n")
                #print(body.h3.text)
                #print("\n\n")

                testo.write((str(body.a.h3.span.text)))
                testo.write("\n")
            else:
                print("iii \n")
                #print(body.h3.span.text)
                #print("\n\n")
                testo.write((str(body.h2.text)))
                testo.write("\n")


        except:
                print("***")
                continue

testo.close()


#"section", class_="story-wrapper",
#"2.h3.span.text"
