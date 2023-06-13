#This program determines budget for an upcoming vacation
#13JUNE2023
#CTI-110 P1HW2-Travel Expense
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
print("Location " + travel)
print("Initial Budget", budget)
print()
print("Fuel: ", gas)
print("Accomodation: ", hotel)
print("Food: ", food)
print()
print("Remaining Balance:", budget-(gas+hotel+food))







      
