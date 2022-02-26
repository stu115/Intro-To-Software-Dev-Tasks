myfleet = []
print("hello this is your car rental programs")

print("(a)add a car to the fleet")
print("(r)emove a car from the fleet")
print("(f)ind a car on this rate or lower")
print("(l)ist all car")
print("(s)how available cars")
print("(g)et a car")
print("(r)eturn a car")
print("(q)uit program")


user_input = input("please select an option")

while user input != "q":

if user_input == "i":

    brand = input("Please enter the brand: ")
    mileage = input("Please enter mileage: ")
    fuel = input("Please enter fuel type: ")
    availability = input True
    rate = input ("Please enter rate")
    regnum = input("Please enter registration number")
    

    carobject = Car(brand,mileage,fuel,avail,rate,regnum)
    myfleet.append(cardobject)
    print(myfleet)

