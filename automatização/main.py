import csv
import openpyxl

wb = openpyxl.load_workbook('output.xlsx')

ws = wb.active if wb.active else wb.create_sheet('Sheet1')

with open('input.')