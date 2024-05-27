import os
import logging
import requests
import csv

from bs4 import BeautifulSoup

level = logging.DEBUG
format_log = "%(asctime)s - %(levelname)s - %(message)s"

if not os.path.exists("./logs/"):
    os.mkdir("./logs/")
logfile = "./logs/verify_mailbox.log"
logging.basicConfig(format=format_log, level=level, filename=logfile)
logger = logging.getLogger(__name__)

url = 'https://ipapi.is/vpn-exit-nodes.html'
logging.info('Starting the script.')

try:
    response = requests.get(url)
    response.raise_for_status()
    logging.info('Successfully fetched the webpage.')
except requests.exceptions.RequestException as e:
    logging.error(f'Error fetching the webpage: {e}')
    raise

soup = BeautifulSoup(response.text, "html.parser")


def find_row(soup):
    data_item = []
    all_name_fields = soup.select('table.is-striped > tbody > tr')
    for data in all_name_fields:
        cells = data.select('td')
        texts = [cell.get_text().strip() for cell in cells]
        data_item.append(texts)
    return data_item


try:
    data = find_row(soup)
    logging.info('Successfully parsed the webpage.')
except Exception as e:
    logging.error(f'Error parsing the webpage: {e}')
    raise

try:
    with open('output.csv', 'w', newline='', encoding='utf-8') as file:
        header = ["VPN_Service", "IP_Address", "Organization", "City", "Country"]
        writer = csv.writer(file)
        writer.writerow(header)
        for row in data:
            writer.writerow(row)
    logging.info('Successfully wrote data to output.csv.')
except Exception as e:
    logging.error(f'Error writing data to CSV file: {e}')
    raise

logging.info('Script finished successfully.')