import os
import datetime

file = "products.csv"

#讀取檔案
def read_file(filename, products):
	with open(filename, "r", encoding="utf-8") as f:
		for line in f:
			data = line.strip().split(",")
			products.append(data)
			if "商品" not in line:
				print(data)
	products[1][1] = str(datetime.datetime.now()).split(" ")[0]

	return products

#使用者輸入
def user_input(products):
	while True:
		name = input("請輸入商品: ")
		if name == "q":
			break
		price = int(input("請輸入價格: "))
		products.append([name, price])
		products[2][1] = int(products[2][1]) - price
	print(products)

	return products

#寫入檔案
def write_file(filename, products):
	with open(filename, "w", encoding="utf-8") as f:
		for i in products:
			f.write(i[0] + "," + str(i[1]) + "\n")

#主程式
def main(file):
	products = []
	if os.path.isfile(file):
		products = read_file(file, products)
	else:
		start = str(datetime.datetime.now()).split(" ")[0]
		now = str(datetime.datetime.now()).split(" ")[0]
		print("尚未有購買紀錄")
		money = int(input("請輸入預算: "))
		products.append(["計算日", start])
		products.append(["現在日期", now])
		products.append(["剩餘預算", money])
		products.append(["商品", "價格"])

	products = user_input(products)
	write_file(file, products)

main(file)