from bs4 import BeautifulSoup
import requests
from twilio.rest import Client
import smtplib

# INFO TO SEND MESSAGE VIA EMAIL
MY_EMAIL = "geaa00643@gmail.com"
PASSWORD = "stshwbcqwctxdyco"

# INFO TO SEND A MESSAGE VIA TEXT
ACCOUNT_SID = "AC1f8ae4df7a706685d9211e91744eb6d9"
AUTH_TOKEN = "[729096d8613b7f0803143d2da0ebaf84]"

PRICE_LIMIT = 1800

my_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,sq;q=0.8,fr;q=0.7"
}
product_url = "https://www.amazon.com/Apple-MacBook-Laptop-10%E2%80%91core-16%E2%80%91core/dp/B0BSHDVBXZ/ref=sr_1_3?adgrpid=149992944904&dib=eyJ2IjoiMSJ9.oEc7tV9s79835nDbWXQ2diagSejSgZzbX_p1TdAB4QYhN4PSEgSMVGrDujlkxEigrSk5EwQSOeOp8Rcyg748BfFLRKSt7nxSoiNDexLU3_EYRuXHGBPIYqujPrjUmqBrDVMihgLjTtuH9pm0fh6lJZbxQYrFSXU5Nyw-FiRMwYWFFoEDwCrSUMBNoqyDZLUneFfNY7_EX-bwyhJw9orTn5SdsCSd7DBw1Ym_q5TW624.LwXa4e1GCiRd-lGbBYx8y4YrCW2udPiHMj3K3gBjqKU&dib_tag=se&hvadid=673600130071&hvdev=c&hvlocphy=9069992&hvnetw=g&hvqmt=b&hvrand=1679501478520822901&hvtargid=kwd-1960211462085&hydadcr=21218_13502031&keywords=macbook+2023+m2+laptop&qid=1718988120&sr=8-3"
response = requests.get(product_url, headers=my_headers)
product_website = response.text

soup = BeautifulSoup(product_website, "html.parser")

product_name_tag = soup.find(name="span", id="productTitle")
product_name = product_name_tag.getText().strip()

whole_price_tag = soup.find(name="span", class_="a-price-whole")
whole_price = whole_price_tag.getText().replace(",", "")
fraction_price_tag = soup.find(name="span", class_="a-price-fraction")
price_fraction = fraction_price_tag.getText().replace(".", "")
product_price = float(whole_price + price_fraction)

if product_price < PRICE_LIMIT:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="obrikoci2@gmail.com",
            msg=f"Subject:‼️Low Price Alert on Amazon️ ‼️\n\n{product_name} is now ${product_price}!\nCheck it out now:{product_url}".encode("utf-8")
        )
