import requests
import json
import html
from pprint import pprint
import pandas
import logging

reportType = ['BCTQ', 'CDKT', 'CSTC', 'KQKD', 'LC']
API = 'https://finance.vietstock.vn/data/financeinfo'
data = {
    'Code': '',
    'Page': '1',
    'PageSize': '4',
    'ReportTermType': '1',
    'ReportType': 'BCTQ',
    'Unit': '1000000',
}

def getReport(bank):
    for report in reportType:
        for page in [1,2,3,4]:
            data['Code'] = bank
            data['Page'] = page
            data['ReportType'] = report
            response = requests.post(API, data)
            logging.info('Get data ' + bank + ' - ' + report + ' - ' + str(page))
            with open('./json/' + bank + '_' + report + '_' + str(page) + '.json', 'w') as outfile:
                outfile.write(response.text)


banks = ['ABBank', 'ACB', 'Agribank', 'ANZB', 'BAB', 'BaoVietBank', 'BCEL', 'BID', 'CFV', 'CoopBank', 'CTG', 'DAB', 'DeutscheBank', 'DongABank', 'EIB', 'EVF', 'FCB', 'FENB', 'GPBank', 'HBB', 'HDB', 'HongLeong', 'HSBC', 'Indovinabank', 'JPMorgan', 'KLB', 'LaoVietBank', 'LPB', 'MBB', 'MDB', 'MHB', 'MSB', 'NamABank', 'NVB', 'OCB', 'Oceanbank', 'PGBank', 'PNB', 'PVcomBank', 'PVF', 'SCB', 'SeABank', 'SGB', 'SHB', 'Shinhan', 'Shinhanvina', 'StandardChartered', 'STB', 'TCB', 'TinNghiaBank', 'TPB', 'TVFC', 'VBSP', 'VCB', 'VCFC', 'VDBank', 'VIB', 'VIDBank', 'VietABank', 'Vietbank', 'VietCapitalBank', 'VietNgaBank', 'Vinasiam', 'VNCB', 'VPB', 'VVF', 'WEB']
for bank in banks:
    getReport(bank)
