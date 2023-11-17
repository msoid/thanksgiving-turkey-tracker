from sys import breakpointhook


print("Welcome to your Turkey Tracker! We can help you track how long it will take for your turkey to cook!")

useropt = str(input("Do you want to track your turkey? (yes/no): "))

while useropt == "yes":
    turkeysu = str(input("Is your turkey stuffed or not stuffed? (stuffed/not stuffed): "))
    twe = int(input("What is the weight of your turkey in pounds?: "))
    if turkeysu == "not stuffed":
        turkeytimeus = str(twe*13)
        print("You should cook your turkey at 350 degrees farenheit for " + turkeytimeus + " " + "minutes.")
        useropt = str(input("Do you want to track your turkey? (yes/no): "))
        if useropt != "no":
            print("Thank you for using Turkey Tracker!")
            break
    elif turkeysu == "stuffed":
        turkeytimeus = str(twe*28)
        print("You should cook your turkey at 350 degrees farenheit for " + turkeytimeus + " " + "minutes.")
        useropt = str(input("Do you want to track your turkey? (yes/no): "))
        if useropt != "no":
            print("Thank you for using Turkey Tracker! We hope to see you again next year!")
            break
    else: 
            print("Try again.")

while useropt == "no":
        print("Come here to track your turkeys when you need to!")
        break