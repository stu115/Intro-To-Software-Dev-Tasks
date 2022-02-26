myadds.append(add)

print(myadds)



if user_input =="d":

    pcode_to_delete = input("Enter postcode to delete: ")

    for add in myadds:

        if pcode_to_delete == add[2]:    # postcode is always stored

             print("Found an address with the postcode: ", add)




elif user_input =="f":

     pcode_to_find = input("Enter postcode to find: ")

     for add in myadds:

         if pcode_to_find == add(12):

             print("Found an address wih the postcode: ", add)




elif user_input == "1":

      print(myadds)



      print("Sorry I didn't get that")
