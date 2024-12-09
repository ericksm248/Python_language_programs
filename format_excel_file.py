import xlrd
import os
i = 0
name_file = input("ingrese el nombre del archivo: ")
openFile = xlrd.open_workbook(name_file+".xlsx")
sheet = openFile.sheet_by_name("REPORTE")
#open("data.txt","a")
#print("Nr de filas",sheet.nrows)
#print("Nr de columnas",sheet.ncols)
for a in range(int(sheet.nrows/2)):
	if 5+i>=int(sheet.nrows):break
	buf1 = "{  %d,%d,\"%-16s\",%d,%d,%4d,{%d,0}}," %(int(sheet.cell_value(5+i,0)),0 if sheet.cell_value(5+i,2)=='A' else 1,sheet.cell_value(5+i,4),sheet.cell_value(5+i,5),sheet.cell_value(5+i,6),sheet.cell_value(5+i,7),sheet.cell_value(5+i,8))
	if 6+i>=int(sheet.nrows):
		buf2 = ""
	else: 
		buf2 = "{  %d,%d,\"%-16s\",%d,%d,%4d,{%d,0}}," %(int(sheet.cell_value(6+i,0)),0 if sheet.cell_value(6+i,2)=='A' else 1,sheet.cell_value(6+i,4),sheet.cell_value(6+i,5),sheet.cell_value(6+i,6),sheet.cell_value(6+i,7),sheet.cell_value(6+i,8))
	print(buf1 + buf2)
	i=i+2
os.system("pause")
