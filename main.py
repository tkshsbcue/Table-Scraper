import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://ninjatables.com/examples-of-data-table-design-on-website/"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")
#cc = input("Enter the Class Name ->")
table = soup.find("table", class_= "foo-table ninja_footable foo_table_17874 ninja_table_unique_id_669291762_17874 ui table nt_type_legacy_table selectable striped vertical_centered footable-paging-right ninja_table_pro footable footable-1 footable-filtering footable-filtering-right footable-paging breakpoint-xs")

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
