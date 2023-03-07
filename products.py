import os

products = []

if os.path.isfile("products.csv"):
	with open("products.csv", "r", encoding="utf-8") as f:
		for line in f:
			data = line.strip().split(",")
			products.append(data)
			if "商品" not in line:
				print(data)

else:
	print("尚未有購買紀錄")
	money = int(input("請輸入預算: "))
	products.append(["剩餘預算", money])
	products.append(["商品", "價格"])


while True:
	name = input("請輸入商品: ")
	if name == "q":
		break
	price = int(input("請輸入價格: "))
	products.append([name, price])
	products[0][1] = int(products[0][1]) - price
print(products)

with open("products.csv", "w", encoding="utf-8") as f:
	for i in products:
		f.write(i[0] + "," + str(i[1]) + "\n")