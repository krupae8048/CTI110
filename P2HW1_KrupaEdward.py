#This program determines budget for an upcoming vacation
#20JUNE2023
#CTI-110 P2HW2-Travel 
#Edward Krupa
#
print("This program determines budget for an upcoming vacation")
print()
budget= int(input("Enter budget:"))
print()
travel= input("Enter your travel destination: ")
print()
gas=int(input("How much do you think you will spend on gas? "))
print()
hotel=int(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food=int(input("Last, how much do you need for food? "))
print()
print("-"*12,"Travel Expenses", "-"*12)
print("Location: ", " "*12, travel)
print("Initial Budget:"," "*5, budget)
print("Fuel: ", " "*19,  gas)
print("Accomodation: ", " "*1,  hotel)
print("Food: "," "*17,  food)
print("-"*49)
print("Remaining Balance:", budget-(gas+hotel+food))







      
