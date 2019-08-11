import json, os, glob, html
import pandas as pd
from pprint import pprint

dataPath = './json/'
banks = ['ABBank','ACB','Agribank','ANZB','BAB','BaoVietBank','BCEL','BID','CFV','CoopBank','CTG','DAB','DeutscheBank','DongABank','EIB','EVF','FCB','FENB','GPBank','HBB','HDB','HongLeong','HSBC','Indovinabank','JPMorgan','KLB','LaoVietBank','LPB','MBB','MDB','MHB','MSB','NamABank','NVB','OCB','Oceanbank','PGBank','PNB','PVcomBank','PVF','SCB','SeABank','SGB','SHB','Shinhan','Shinhanvina','StandardChartered','STB','TCB','TinNghiaBank','TPB','TVFC','VBSP','VCB','VCFC','VDBank','VIB','VIDBank','VietABank','Vietbank','VietCapitalBank','VietNgaBank','Vinasiam','VNCB','VPB','VVF','WEB']
finalData = {}
whiteList = ['Vốn và các quỹ']
banks = ['ACB', 'VCB']
whiteList = [
    'Tổng LNST',
    'Tổng tài sản',
    'Tổng LNTT',
    'TỔNG NỢ PHẢI TRẢ VÀ VỐN CHỦ SỞ HỮU',
    'TỔNG NỢ PHẢI TRẢ',
    'Dư nợ cho vay/Tổng tài sản Có',
    'Chi phí hoạt động',
    'Vốn chủ sở hữu/Tổng vốn huy động',
    'Dự phòng rủi ro tín dụng/Tổng dư nợ',
]
for bank in banks:
    masterKey = bank
    for filename in glob.glob(dataPath + bank + '*.json'):
        reportType = filename.split('_')[1]
        with open(filename) as jsonFile:
            data = json.load(jsonFile)
            for index in [1, 2, 3, 4]:
                try:
                    year = data[0][3 - (index - 1)]
                except IndexError:
                    break
                year = data[0][3 - (index - 1)]['YearPeriod']
                subKey = masterKey + '_' + str(year)
                if subKey not in finalData:
                    finalData[subKey] = {
                        'BANK': bank,
                        'YEAR': year,
                    }
                for key in data[1]:
                    values = data[1][key]
                    for row in values:
                        if row['NameMobile'] in whiteList:
                            # dataKey = reportType + '_' + row['NameMobile']
                            dataKey = row['NameMobile']
                            finalData[subKey][dataKey] = row['Value' + str(index)]
jsonData = []
for _key, _value in finalData.items():
    jsonData.append(_value)
pd.read_json(json.dumps(jsonData)).to_csv('pandas.csv', index=False)
