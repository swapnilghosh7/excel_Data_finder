import xlrd

path = 'statscounter_data.xlsx'
count = 0
check = 100;
wb = xlrd.open_workbook(path)
print(len(wb.sheet_names()))
for l in range(len(wb.sheet_names())):
	sh = wb.sheet_by_index(l)
		# sh = wb.sheet_names()
		# print(sh)
		# sheet = wb.sheet_by_index(1)

	for i in range(sh.nrows):
		str = sh.cell_value(i,2)
		res = [int(j) for j in str.split() if j.isdigit()]
		time = 0
		if res:
			for x in range(len(res)):
				if (len(res)> 1) and x < (len(res)-1):
					timeSix = res[x] * 60 ** (len(res) -(x+1))
					time = time + timeSix
				else:
					time = time + res[x]

			if(time == check):
				count = count + 1
print(count)