import requests
from bs4 import BeautifulSoup
import smtplib


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('sameeranpandey@gmail.com', 'xgdbkuruivyjfaoi')

    subject = 'The price is down'
    body = 'Link:', URL
    msg = f"Subject : {subject} \n \n {body}"
    

    server.sendmail('Your_Email_Id@gmail.com', 'Secondary_email@gmail.com', msg)
    print("email sent")
    server.quit()


URL = "https://www.amazon.in/Pantene-Silky-Smooth-Care-Shampoo/dp/B0764M9QVT/ref=sr_1_7?keywords=pantene&qid=1566390239&s=gateway&sr=8-7" //URL of the price section of product

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

page = requests.get(URL , headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id = "productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()

cprice = float(price[2:5])

print(title.strip())
print(cprice)
if(cprice < 470.0):
    send_mail()


