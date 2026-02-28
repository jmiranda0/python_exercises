"""
#3 Crea una agenda de contactos por terminal.
    - Debes implementar funcionalidades de búsqueda, inserción, actualización
      y eliminación de contactos.
    - Cada contacto debe tener un nombre y un número de teléfono.
    - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
      y a continuación los datos necesarios para llevarla a cabo.
    - El programa no puede dejar introducir números de teléfono no numéricos y con más
      de 11 dígitos (o el número de dígitos que quieras).
    - También se debe proponer una operación de finalización del programa.
 """
contacts = {
    "albert":"12556655551",
    "johan":"12556345552",
    "john":"12557855533",
    "abel":"12552225594",
    "sara":"45552225505"
    }
loop = True

def insert_num(label:str):
   while True:
              num = input(label)
              if num.isnumeric()!=True:
                  print("Please insert a number")
              elif len(num) != 11:
                  print("Please enter an 11-digit number") 
              else:
                return num
def show_contacts(contacts:dict):
    print("\t Contacts List:")
    for contac,num in contacts.items():
                print(f"\t{contac}:{num}")
    
def search(contacts:dict) ->str:
    while True:
      contact = input("Search the contact :")
      if contact not in contacts.keys():
        search = input("The contact doesn't exist.\nIf you want to try again press 1 else press any thing: ")
        if search == "1":
            pass
        else:
            print("Returning to menu")
            break
      else:
          return contact

while loop:
    try:
        status = int(input("""What do you want to do?
              01 Press 1 to insert a contact
              02 Press 2 to update a contact
              03 Press 3 to search a contact
              04 Press 4 to delete a contact
              05 Press 5 to exit
              """))
    except ValueError:
        print("Insert a correct number")
        continue
    
    match status:
        case 1:
            print("Create a new contact:")
            contact = input("Contact Name: ")
            
            contacts[contact] = insert_num("Contact number: ")

            show_contacts(contacts)
            
        case 2:
            print("Update contact information:")
            show_contacts(contacts)

            contact = search(contacts)
            if contact not in contacts.keys():
                pass
            else:
                update_status = int(input(f"""What would you like to change about {contact}?
                                      01 Contact name
                                      02 phone number
                                      """))
                if update_status == 1:
                    new_contact = input("Update the contact name: ")
                    if new_contact not in contacts:
                        contacts[new_contact] = contacts.pop(contact)
                elif update_status ==2:
                    contacts[contact] = insert_num("Insert the new number: ")
                    
                else:
                    print("Please select a valid option (1 or 2). Returning to menu")
                    
        case 3:
            show_contacts(contacts)
            contact = search(contacts)
            if contact in contacts:
              print(f"Name: {contact} | Phone: {contacts[contact]}")

        case 4:
            show_contacts(contacts)
            contact = search(contacts)
            if contact in contacts:
              print(f"Name: {contact} | Phone: {contacts[contact]} has been deleted")
              contacts.pop(contact)
              show_contacts(contacts)
            

        case 5:
            print("Bye")
            loop = False
        
        