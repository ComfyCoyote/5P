# This program was coded by Muzzammil Adamjee and completed on 10/22/2021.
# It simulates a vending machine by displaying products and prices to the user
# through the command shell. It allows the user to select an item
# then proceeds to asks the user to pay for it.
# Upon a sufficient monetary deposit it then dispenses the appropriate
# change to them.
#


shopping = True
while shopping:
    print("Vending Machine")
    x = True
    while x:
        items = ["a bottle of water - $1.99", "a bottle of orange juice - $2.15", "a bottle of ice tea - $2.49"]
        
        
        print(f"Please enter what product you want to buy[1-3] or select quit[4]:\n1.{items[0]}\n2.{items[1]}\n3.{items[2]}\n4.Quit")
   
        choice = input()
        if choice == "1" or choice == "2" or choice == "3":
            x = False
        elif choice == "4":
            x = False
        else:
            print("You made a wrong choice!")



           

    if choice == '1':
        money = 0
        while money < 199:
            money += int(input("please deposit money (in cents): "))

        if money >= 199:
            print("you bought a bottle of water")
          
    elif choice == '2':
        money = 0
        while money < 215:
            money += int(input("please deposit money in cents: "))
       
        if money >= 215:
            print("you bought a bottle of orange juice")
            
    elif choice == '3':
        money = 0
        while money < 249:
            money += int(input("Enter amount in cents: "))
      
        if money >= 249:
            print("you bought a bottle of ice tea")
            
    elif choice == '4':
        print("Goodbye!")
        shopping = False
        break
       
  
    product_price = [199, 215, 249]
    change = money - product_price[int(choice)-1]
    dollars = change // 100   
    change = change % 100     
    quarters = change // 25 
    change = change % 25
    dimes = change // 10
    change = change % 10
    nickels = change // 5
    change = change % 5
    cents = change   
    print("your change is: ")
    if dollars != 0:
        print(f"Dollars - {dollars}")
    if quarters != 0:
        print(f"Quarters - {quarters}")
    if dimes != 0:
        print(f"Dimes - {dimes}")
    if nickels != 0:
        print(f"Nickels - {nickels}")
    if cents != 0:
        print(f"Cents - {cents}")
          

        

        

            
        

        


        
        
