import requests
import pandas as pd
from bs4 import BeautifulSoup
#URL goes here
url = ""
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")
#you manually need to find the class name of that table using inspect element
table = soup.find("table", class_= "")

header = table.find_all("th")

titles = []

for i in header:
    titles.append(i.text.strip())

df = pd.DataFrame(columns=titles)

rows = table.find_all("tr")

for i in rows[1:]:
    data = i.find_all("td")
    row = [tr.text.strip() for tr in data]
    df.loc[len(df)] = row


df.to_csv('financial_data.csv', index=False)

print("Data saved to financial_data.csv")
