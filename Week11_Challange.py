import mobile as CL

manufac = input("Enter Manufacture Here: ")
model = input("Enter Model Here: ")
retailPrice = float(input("Enter Retail Price Here: "))
retailPrice = str(retailPrice)

phone = CL.mobile(manufac, model, retailPrice)

print("Manufacture is " + phone.get_manufact())
print("Model is " + phone.get_model())
print("Retail Price is $" + phone.get_retail_price())