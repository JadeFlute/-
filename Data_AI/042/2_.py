import pandas as pd
from pandas import DataFrame
import xlrd


wb = xlrd.open_workbook('meal_order_detail.xlsx')
sheets = wb.sheet_names()
print(sheets)

total = DataFrame()
for i in range(len(sheets)):
    df = pd.read_excel('meal_order_detail.xlsx',sheet_name=i,skiprows=0,encoding='utf8')
    total = total.append(df)

print(total.shape)

writer = pd.ExcelWriter('output.xlsx')
total.to_excel(writer,sheet_name='Sheet1')
writer.save()












