import requests
import pandas as pd
from bs4 import BeautifulSoup
import discord
from discord.ext import commands


def scrape_table_to_csv(url, class_name, output_filename='financial_data.csv'):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    table = soup.find("table", class_=class_name)

    if table is None:
        print(f"No table found with class name '{class_name}'.")
        return

    header = table.find_all("th")
    titles = [i.text.strip() for i in header]

    df = pd.DataFrame(columns=titles)
    rows = table.find_all("tr")

    for i in rows[1:]:
        data = i.find_all("td")
        row = [tr.text.strip() for tr in data]
        df.loc[len(df)] = row

    df.to_csv(output_filename, index=False)
    print(f"Data saved to {output_filename}")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def scrape(ctx, url, class_name):

    scrape_table_to_csv(url,class_name)
    await ctx.send(file=discord.File(r'./financial_data.csv'))

# or:
#Put the Token here
bot.run("")
  
