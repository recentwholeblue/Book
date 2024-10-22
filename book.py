import pandas as pd
book=open("book.csv", "w")
book.write("name,"+"phone,"+"email,"+"birthday \n")
book.close
#Import and setup files

#Reads and shows file content
def display():
        df = pd.read_csv('book.csv')
        print(df.to_string(index=False))

#Gets user input and saves entry to file
def add():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    birthday = input("Enter birthday: ")
    book=open("book.csv", "a")
    book.write(f"{name},{phone},{email},{birthday}\n")

#Loads single user, then modifies the entry and saves it.
def update():
    name_to_update = input("Enter the name to update: ").strip()

    df = pd.read_csv('book.csv')

                
    print("\nCurrent entries:")
    print(df['name'].values)
            
    mask = df['name'].str.strip() == name_to_update
    if mask.any():
        entry_index = df[mask].index[0]
        for field in ['name', 'phone', 'email', 'birthday']:
            current_value = df.at[entry_index, field]
            new_value = input(f"Enter new {field} (leave blank to keep '{current_value}'): ").strip()
            df.at[entry_index, field] = new_value if new_value else current_value
                
        df.to_csv('book.csv', index=False)
        print(f"Entry for {name_to_update} updated successfully.")



#If the user selects a valiid entry, then it is removed.
def remove():
    remove = input("Enter name: ")
    df = pd.read_csv('book.csv')
    if remove in df['name'].values:
        df = df[df['name'] != remove]
        df.to_csv('book.csv', index=False)
        print("Remove")

#User interaction and input menu.
available=True
while True:
    #Show available options to user.
    if available:
        print("Options: \n")
        print("Display \n"+"Add \n"+"Update \n"+"Remove")
        choice=input("Select options: ")
        available=False
    
    #Checks if user input is a valid option. If not, shows an error to the user.
    if choice=="Display":
        try:
            display()
        except:
            print("Entry not found")
        available=True
    if choice=="Add":
        add()
        available=True
    if choice=="Update":
        try:
            update()
        except:
            print("Entry not found")
        available=True
    if choice=="Remove":
        try:
            remove()
        except:
            print("Entry not found")
        available=True
    
    #If user input is not valid.
    elif choice != "Remove" or "Update" or "Display" or "Add":
        print("Not a valid option")
        available=True