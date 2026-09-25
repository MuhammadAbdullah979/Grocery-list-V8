grocery_list=[]
print("Welcome to the grocery list maker!")
running = True
second_running = True
jik = True

#add items
while running:
    choice=input('Do you want to add something to the list(Y/N): ')
    choice = choice.strip()
    choice = choice.upper()
    if choice == 'Y':
        yes_command = input("Enter the name of the item you want to add you want to add: ")
        yes_command = yes_command.strip()
        yes_command = yes_command.upper()
        grocery_list.append(yes_command)
    elif choice in ('N','X'):
        running = False
    else:
        print("Wrong input recieved")
print(grocery_list)

#remove items
while second_running:
    second_choice=input('Do you want to remove something from the list(Y/N): ')
    second_choice = second_choice.strip()
    second_choice = second_choice.upper()
    if second_choice == 'Y':
        second_yes_command = input("Enter the name of the item you want to add: ")
        second_yes_command = second_yes_command.strip()
        second_yes_command = second_yes_command.upper()
        if second_yes_command in grocery_list:
            jik = True
        else:
            jik = False
            print('Item was not found, double check spellings')
        if jik:
            grocery_list.remove(second_yes_command)
    elif second_choice in ('N','X'):
        second_running = False
    else:
        print("Wrong input recieved")
print(grocery_list)
        

