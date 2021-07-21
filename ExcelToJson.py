import os,sys

from openpyxl import Workbook, load_workbook
import json

xlsx_path = "."

def LoadExcel(file_path,file_name):
    path = os.path.join(xlsx_path,file_path,file_name)
    wb = load_workbook(path)
    return wb

def ReadLines(work_book):
    ws = work_book.worksheets[0]
    rows = ws.rows
    desc_row = next(rows)
    name_row = next(rows)
    
    output_all = {}
    for row in rows:
        output_row = {}
        for j in range(len(desc_row)):
            desc = desc_row[j].value
            col_name = name_row[j].value
            if col_name == None or len(col_name.strip()) == 0:
                continue
            col_name = col_name.strip()

            data = row[j].value

            if desc == "int":
                if data == None:
                    output_row[col_name] = 0
                else:
                    output_row[col_name] = int(data)
            elif desc == "string":
                if data == None:
                    output_row[col_name] = ""
                else:
                    output_row[col_name] = data
        _id = output_row["id"]
        output_all[_id] = output_row
    return output_all

work_book = LoadExcel(".",sys.argv[1])
output_all = ReadLines(work_book)
json_text = json.dumps(output_all,indent=4,ensure_ascii=False)
print(json_text)

