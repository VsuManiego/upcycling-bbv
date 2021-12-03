# Title: Upcycling Innovation Management System
# Batister, Jhonel 
# Visabella, Goerge
# Belonio, Jo Franz

print ("This is a list of Upcycled Products with their description and procedure")
print ("------------------------------------------------------------------------------------")

upcycledproduct = {" Coin Purse - Coin purses keep loose currency separate from the rest of the purse or pocket's contents. This is especially helpful when traveling to other countries which use a number of metal coins for standard currency": 
"Find 2 plastic bottles to use as a coin purse. Cut the bottom portion off of each bottle, then discard the top and trim the cut edge further to clean up any jaggedness. Punch holes along the cut edges with a thick needle. Find a zipper that is long enough to wrap around the bottle then place the zipper inside the bottle, along the cut edge. Overlap the ends of the zipper if the zipper is too long. Thread your needle with strong thread. Sew the zipper to the bottle using a running stitch. Open the zipper and sew it to the other half of the bottle. Lastly,zip the bottle shut." , "Repurposed Tin Can - It can be used as a planters which ornamental plants are grown": "Make a hole to the bottom and sides of the can, clean the can through washing it and let it dry, apply some excess paint to make it colorful, and look a tire wire and attach it to the can as its holder." , " Plastic Straw Cable Organizer - It helps to organize the disarranged cables which it can be used to hold the cables into one together": 

"Slice the plastic straw by inserting and twisting it into the pencil sharpener" , "Plastic Toothbrush Holder Bottle - It is used as a container for the tooth brush": 

"Remove the cap of the plastic bottle but don’t throw it, slice the plastic bottle vertically into two equal parts but not fully sliced. Then, close it together and used the cap as the locker." , "Plastic bottle stool - It is used as a seat":
    "Gather at least 7 big plastic bottles with same sizes, then stick it together by using a strong paste and tie. Cover the bottom to half with brochures up to 3 to 5 layers and let it dry at least two (2) days. After that, paint it as what you like to design and let it dry" , "Candle Glass planter - It used as a planter especially for succulent plants":
        "Clean the old candle Glass by pouring a boiling water. Put some pebbles in the glass about half of it, and then put soil for the rest of space and then it is ready to be planted" , "Plastic rope - It can be used in different ways. It can be hanged by clothes or used for decoration":
            "Place the plastic bag in a flat surface and remove the wrinkles. Next is, fold the plastic bag vertically at least two times, and cut horizontally into four parts and then braid it" , "Plastic coaster - It is used to be placed anything that can damage the surface":
                "Place the plastic bag in a flat surface and remove the wrinkles. Next is, fold the plastic bag vertically at least two times, and cut horizontally into four parts and then braid it. Roll the braided plastic and use stick glue to stick it together. After that, it is ready to be used" , "Upcycled pillow shirt - It used as pillow for bed or in sofa":
                    "Place the old shirt in flat surface and cut the center part as what shape you like. Cut a little in all around then, place a cotton or a pillow in between the cutted shirt, and tie the cutted parts"}  

print("Upcycledproduct:")

for item, data in upcycledproduct.items():
    print(f"\n{item}. \nProcedure of items of this product in upcycledproduct: {data}")  
while True:
    add = input("\nAdd a product in the inventory? (Yes/No): ")  # if want to add
    add = add.title( )
    
    if add == "Yes":  
        add_new_product = input("Please add the name of the product: ")  # what to be add
        capitalize_add_new_product = add_new_product.capitalize() 
        add_product_description = input("Please add the description of the product): ")  # what be the description   
        good = False
  
        while not False:  
            try:
                add_new_product_procedure = str(input("Please input the procedure of items of this product you want to add in the upcycledproduct: "))  #what  
                good = True
                break  
                
            except NameError:
                print("Please input a procedure only.") 

        upcycledproduct[f"{capitalize_add_new_product} - {add_product_description}"] = f"{add_new_product_procedure}"  # adds product, description, and procedure to the upcycledproduct
        print(f"\nThe upcycledproduct has been updated.") 
            
    elif add == "No":  # does not want to add
        break 
        
    else:  
        print("The answer you entered is not in the choices. Please repeat")  #user be inform and repeat

print("\n\nUpcycledproduct:")

for item, data in upcycledproduct.items():       
    print(f"\n{item}. \nProcedure of items of this product in upcycledproduct: {data}") 