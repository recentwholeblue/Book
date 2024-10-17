import pandas as pd
book=open("book.csv", "w")
book.write("name,"+"phone,"+"email,"+"birthday \n")
book.close
#Import and setup files


def display():
        df = pd.read_csv('book.csv')
        print(df.to_string(index=False))
def add():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    birthday = input("Enter birthday: ")
    book=open("book.csv", "a")
    book.write(f"{name},{phone},{email},{birthday}\n")
def update():
    return 0
def remove():
    remove = input("Enter name")
    df = pd.read_csv('book.csv')
    if remove in df['name'].values:
        df = df[df['name'] != remove]
        df.to_csv('book.csv', index=False)
        print("Remove")
    
    
    
    
available=True
while True:
    #Show available options
    if available:
        print("Options: \n")
        print("Display \n"+"Add \n"+"Update \n"+"Remove")
        choice=input("Select options: ")
        available=False

    if choice=="Display":
        display()
        available=True
    if choice=="Add":
        add()
        available=True
    if choice=="Update":
        update()
        available=True
    if choice=="Remove":
        remove()
        available=True
