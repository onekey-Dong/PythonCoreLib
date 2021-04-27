import pandas as pd
import xlsxwriter

def readToOtherFile(old_file, new_file):
    if old_file == None or new_file == None:
        return None
    
    allFd = pd.read_excel(old_file, sheet_name=None)
    writer = pd.ExcelWriter(new_file, engine='xlsxwriter')
    for sheet_name in list(allFd):
        allFd[sheet_name].to_excel(writer, sheet_name, index=False)
    
    return writer

def getExcelSheetsName(file):
    if old_file == None or new_file == None:
        return None
    fd = pd.read_excel(file, sheet_name=None)
    return list(fd)