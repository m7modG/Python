fruts_prices={"apple": 10,"watermelon":12,"mango":15,"graips":12}

frut = input("Enter the frut name\n")

if frut in fruts_prices :
    print(frut," : ",fruts_prices[frut])
    
else :
    print("Sorry, this fruit is not available")
    