# Please note that for every time you execute this codes it appends to the files created(data.csv and the data.txt file)

import xlrd
import json
import csv

def extractData():

    name = input("Name of Excel file = ")
    sheetName = input("Name of the sheet you want to extract = ")
    workbook = xlrd.open_workbook(name+'.xlsx')
    worksheet = workbook.sheet_by_name(sheetName)

    worksheet.cell_value(0,0)

    for line in range(worksheet.nrows):
        payment = worksheet.cell_value(line,0)
        payer = worksheet.cell_value(line,1)
        ORGANIZATION_NAME = worksheet.cell_value(line,2)
        Beneficiary_Name  = worksheet.cell_value(line,3)
        Amount = worksheet.cell_value(line,4)
        Description = worksheet.cell_value(line,5)
        Date = worksheet.cell_value(line,6)

        data = {
            worksheet.cell_value(0,0): payment,
            worksheet.cell_value(0,1): payer,
            worksheet.cell_value(0,2): ORGANIZATION_NAME,
            worksheet.cell_value(0,3) : Beneficiary_Name,
            worksheet.cell_value(0,4) : Amount,
            worksheet.cell_value(0,5) : Description,
            worksheet.cell_value(0,6): Date
        }

        # writing into a txt file in json format.
        with open('data.txt', 'a') as outfile:
            json.dump(data, outfile)


        data =  [payment,payer,ORGANIZATION_NAME,Beneficiary_Name,Amount,Description,Date]

        # Writing into a csv file
        with open('data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)

extractData()