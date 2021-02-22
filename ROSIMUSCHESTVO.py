import requests
import xml.etree.ElementTree as ET
import os
import lxml
import pandas as pd
import datetime

url = 'https://www.rosim.ru/opendata/7710723134-rfi_2_1_stock/data-20200415T0000-structure-20171115T0000.xml'
r = requests.get(url)
with open('New_xml.xml', 'wb') as stakeFile:
    stakeFile.write(r.content)

tree = ET.parse("New_xml.xml")
root = tree.getroot()
# print(root)

registry_number = []
list_entities = []
number_stake = []
for row in root:
    # print(row.tag, row.attrib)
    l = []
    for child in row.findall('ObjectName'):
        # list_entities.append(child.text)
        l.append(child.text)

    for child in row.findall('StockQuantity'):
        l.append(child.text)
        # list_entities.append(child.text)

    for child in row.findall('RegisterNumber'):
        l.append(child.text)
    list_entities.append(l)
headers = ["Company OSN", "Stock Quantity", "ID"]
# stock_array = [list_entities, number_stake]
stock_array = pd.DataFrame(list_entities, None, headers)
final_name = 'StateAssets' + str(datetime.date.today()) + '.csv'
stock_array.to_csv(final_name,encoding='UTF16', sep='\t',index=None)
