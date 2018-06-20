#https://medium.com/mai-piu-senza/connect-a-python-script-to-ifttt-8ee0240bb3aa
#https://anthscomputercave.com/tutorials/ifttt/using_ifttt_web_request_email.html
import requests
from bs4 import BeautifulSoup

def notify_ifttt(message, keyurl):
    report = {}
    report["value1"] = message
    requests.post(keyurl, data=report)


last_availability_file = open("cancellation_text.txt", "r")
last_availability_text = last_availability_file.read()
key_url = open("settings.txt", "r")
key_url = key_url.read()
cancellations_page = "https://www.pc.gc.ca/apps/tcond/cond_e.asp?oPark=100438"
page = requests.get(cancellations_page)
soup = BeautifulSoup(page.text, 'html.parser')

cancellations_text = soup.find_all('p')

for p_tag in cancellations_text:
    if "available" in p_tag.text.lower():
        if last_availability_text.lower() != p_tag.text.lower():
            notify_ifttt(p_tag.text, key_url)
            last_availability_file = open("cancellation_text.txt", "w")
            last_availability_file.write(p_tag.text)


