print("USD and NGN converter ")

Amount = int(input("Amount "))
unit = input("NGN or USD ")

if unit.upper() == "USD":
	converted = Amount * 1515
	print("Amount: " + str(converted))
else:
	converted = Amount / 1515
	print("Amount: "+ str(converted))
print("Done ")
