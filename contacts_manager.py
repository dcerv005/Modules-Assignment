def add_contact(contacts):
    try:
        name= input("Enter contact name: ")
        phone_number = input("Enter phone number: ")
        
    except Exception as e:
        print(f'Error occurred: {e}')
    contacts[name.title()]={}
    contacts[name.title()]['Phone Number']= phone_number
    print(f"Contact: {name.title()} was added.")

def delete_contact(contacts):
    try:   
        contact= input("Which contact do you want to delete?(Enter Name)").title()
        if contact not in contacts:
            print("Contact does not exist.")
        else:
            del contacts[contact]
            print(f"Contact: {contact} was deleted.")
    except Exception as e:
        print(f"Error: {e}")

def display_contacts(contacts):
    if not contacts:
        print("\n\tContact list is empty.")
    for contact in contacts:
        print(f"{contact}")
        for category, details in contacts[contact].items():
            print(f"\t{category}: {details}")


