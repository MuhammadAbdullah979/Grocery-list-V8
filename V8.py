grocery_list=[]
print("Welcome to the grocery list maker!")
#Add items
while True:
    choice=input('Do you want to add something to the list(Y/N): ')
    choice = choice.strip()
    choice = choice.upper()
    if choice == 'X':
        break
    if choice == 'Y':
        yes_command = input("Enter the name of the item you want to add you want to add: ")
        yes_command = yes_command.strip()
        grocery_list.append(yes_command)
    elif choice == 'N':
        break
    else:
        print("Wrong input recieved")
print(grocery_list)

