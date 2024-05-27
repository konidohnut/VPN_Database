import requests
import csv

from bs4 import BeautifulSoup

url = 'https://ipapi.is/vpn-exit-nodes.html'

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


def find_row(soup):
    data_item = []
    all_name_fields = soup.select('table.is-striped > tbody > tr')
    for data in all_name_fields:
        cells = data.select('td')
        texts = [cell.get_text().strip() for cell in cells]
        data_item.append(texts)
    return data_item


data = find_row(soup)

with open('output.csv', 'w', newline='', encoding='utf-8') as file:
    header = ["VPN Service", "IP Address", "Organization", "City", "Country"]
    writer = csv.writer(file)
    writer.writerow(header)
    for row in data:
        writer.writerow(row)
