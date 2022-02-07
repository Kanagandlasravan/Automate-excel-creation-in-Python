import xlsxwriter

data = [
    {
        'name': "Sravan Kanagandla",
        'phone': "9989102133",
        'email' : "kanagandlasravan@gmail.com",
        'address': "Borivali West, Mumbai, Maharastra - 400103",
        'country': "India"
    },
    {
        'name': "Ronak Duari",
        'phone': "8551941547",
        'email' : "ronakduarik@gmail.com",
        'address': "Nalasopara, Mumbai, Maharastra - 400019",
        'country': "India"
    },
    {
        'name': "Ravali Kanagandla",
        'phone': "7506847295",
        'email' : "ravalikanagandla@gmail.com",
        'address': "Borivali West, Mumbai, Maharastra - 400103",
        'country': "India"
    },
    {
        'name': "Sravan Kanagandla",
        'phone': "9989102133",
        'email' : "kanagandlasravan@gmail.com",
        'address': "Borivali West, Mumbai, Maharastra - 400103",
        'country': "India"
    }
        ]

workbook = xlsxwriter.Workbook("excelfile.xlsx")
worksheet = workbook.add_worksheet("fistsheet")

worksheet.write(0,0,"#")
worksheet.write(0,1,"Name")
worksheet.write(0,2,"Phone")
worksheet.write(0,3,"Email")
worksheet.write(0,4,"Address")
worksheet.write(0,5,"Country")

for index, entry in enumerate(data):
    worksheet.write(index+1,0,str(index))
    worksheet.write(index+1,1,entry["name"])
    worksheet.write(index+1,2,entry["phone"])
    worksheet.write(index+1,3,entry["email"])
    worksheet.write(index+1,4,entry["address"])
    worksheet.write(index+1,5,entry["country"])

workbook.close()

