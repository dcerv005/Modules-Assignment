#Question 2
#Task 1

import contacts_manager

contacts={}
while True:
    print("\nWelcome to the Contact Management System!\n\n1. Add a new contact\n2. Display contacts\n3. Delete a contact\n4. Quit\n")

    try:
        user_input = int(input("Please select an option from the menu. (1-4) "))
        if user_input == 4:
            print("\n\tClosing Contact Management System...\n")
            break
        elif user_input == 1:
            contacts_manager.add_contact(contacts)
        elif user_input == 2:
           contacts_manager.display_contacts(contacts)
        elif user_input == 3:
            contacts_manager.delete_contact(contacts)
    except Exception as e:
        print(f"Error occurred: {e}")
        print(f"Please enter a number from 1-4.")

#Task 2

from datetime import datetime

today= datetime.now()
print(today.strftime('%Y-%m-%d'))

try:
    year = int(input("Enter the year(YYY) of the date in question: "))
    month = int(input("Enter the month(MM) of the date in question: "))
    day = int(input("Enter the day(DD) of the date in question: "))
except Exception as e:
    print(f'Error occurred: {e}')

dayoftheweek= datetime(year, month, day)
print(dayoftheweek.strftime('%A'))