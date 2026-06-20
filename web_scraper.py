import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://books.toscrape.com"

response = requests.get(url)

print(response.status_code)
soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)
books = soup.find_all("article", class_="product_pod")

data = []
for book in books:

    title = book.h3.a["title"]

    price = book.find("p", class_="price_color").text

    rating = book.find("p")["class"][1]

    data.append([title, price, rating])
df = pd.DataFrame(
    data,
    columns=["Title", "Price", "Rating"]
)

print(df)
df.to_csv("books_data.csv", index=False)

print("Data saved successfully!")