from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
import os

amazon_url = "https://www.amazon.co.uk/PBN-Whey-Protein-Powder-Strawberry/dp/B07ZV1973J/ref=sr_1_1_ffob_" \
             "sspa?keywords=whey%2Bprotein%2Bpowder&qid=1690292636&rdc=1&sprefix=whey%2B%2Caps%2C106&sr=8-1-" \
             "spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
                  "(KHTML, like Gecko) Version/15.6.1 Safari/605.1.15",
    "Accept-Language": "en-GB,en;q=0.9"
}

response = requests.get(url=amazon_url, headers=headers)
product = response.text

soup = BeautifulSoup(product, "lxml")
product_span = soup.find(name="span", class_="a-offscreen")
product_string = product_span.getText().split("£")[1]
product_price = float(product_string)
print(product_price)

my_email = "pythontest401@gmail.com"
password = os.environ.get("PYTHON401PASSWORD")
recipient = 'george_jb94@hotmail.com'

if product_price < 48:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient,
            msg=f"Subject:Whey protein {product_price}\n\nIt's time to buy some whey! Current price: {product_price}"
    )
