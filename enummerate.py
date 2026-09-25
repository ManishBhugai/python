print("first welcome to our grocery store")
print("Please enter your name ")
name=input("enter your name:")
print(f"Welcome, {name}!")
print("Enter the name of the item and its price below ")
sum=0
list1={}
while True:
    item_name=input("enter the name of the item:")
    item=input("enter the price of the item:")
    if (item !='q'):
        sum+=int(item)
        list1[item_name]=item
        
        
    else:
        print(f"total prie of the items is:{sum}")
        print("Please visit again")
        break
    
print(f"List of items purchused by {name} ")
for i,list in enumerate(list1):
     print(f"{i+1}. {list} : {list1[list]}")
     

