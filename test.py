#Creat a list
candy = []
smarties = 100

'''print(candy)
print(candy[0])#Access first element
print(candy[3])#access fourth element
print(len(candy)-1)#access the last element'''

candy = ["Chocalate", "bubble gum", "skittles", "starburst", "smarties"]
candy.append("Almond joy")#add elements at the end of the list
candy.append("Baby Ruth")#add elements at the end of the list
candy.insert(3, "Kit Kat")
candy.insert(2, "Jelly Belly")
candy.pop(4)
for i in range (0, len(candy), 1):
    print(candy[i], end=" ")








#Display an inventory. Using three list.
#list 1: items name
#list 2L Quantity
#list 3: cost
print("\n")
print("items \t\t\t", "quantity")

