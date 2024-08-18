import requests
import mail
from bs4 import BeautifulSoup


amazon_url = 'https://www.amazon.com/dp/B01NBKTPTS?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1'
amazon_headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    "Accept-Language": "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,pl;q=0.6",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}

get_result = requests.get(amazon_url, headers=amazon_headers)
soup = BeautifulSoup(get_result.text, "lxml")
# print(soup)
price_text = soup.find(name="span", class_="a-offscreen").get_text()
# print(price_text)
price = float(price_text[1:])
print(price)

TARGET_PRICE = 130
NOTIFICATION_EMAIL = "petermoloch@mail.ru"
if price < TARGET_PRICE:
    message = f"Current price for targeting product is pretty nice today - only {price}$ Time to do some shopping!"
    mail.send_email(NOTIFICATION_EMAIL, message)
