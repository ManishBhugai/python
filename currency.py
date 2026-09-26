dict={}
with open("hello.txt","r",encoding="utf-8") as f:
    lines=f.readlines()
    for line in lines:
            value = line.strip()
            for value in line.split():
                currency, rate=value.split("=")
                dict[currency]=int(rate)
                
print("Welcome to our currency converter")
print("Available currencies are:" )
for currency in dict.keys():
    print(currency)
current=int(input("Enter the amount you want to convert:"))
for_currency=input("Enter the currency you want to convert from:")
converted=current*dict.get(for_currency)
print(f"{current} {for_currency} is equal to {converted}")