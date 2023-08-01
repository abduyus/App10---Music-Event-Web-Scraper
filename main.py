import requests
import selectorlib
import smtplib, ssl
import os
import time

"INSERT INTO events VALUES ('Tigers', 'Tiger city', '2088.10.15')"
"SELECT * FROM events WHERE date='2088.11.15'"
"DELETE FROM events WHERE band='ismail'"

URL = "http://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "yusufabdurrasheed539@gmail.com"
    password = "oybomsonfjawmknk"

    receiver = "yusufabdurrasheed539@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
    print("Email was sent")



def store(extracted):
    with open("data.txt", 'a') as file:
        file.write(extracted + "\n")
    

def read():
    with open("data.txt", 'r') as file:
        return file.read()

if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        content = read()
        if extracted != "No upcoming tours":
            if extracted not in content:
                store(extracted)
                send_email(message="Hey, New event was found!")
        time.sleep(2)

