database = []
day = 1

print("Welcome to Puhlant, your very own plant growth tracker!")
user_action_input = ""
# def add_plant(database, name, height, day):
#     database.append({
#         "name": name, 
#         "height": height, 
#         "day_started_recording": day,
#         "number_of_days_recording": 0,
#         "historical_data": [(day, height)]
#     })
#     return database

# def run_menu(database):
#     user_input = input()

#     if user_input == "1":
#         name = input()
#         height = int(input())


# # main
# run_menu(database)

while user_action_input != "!":
    print("Your possible actions are:")
    print("'0': View Your Plants")
    print("'1': Add a Plant to the Database")
    print("'2': Remove a Plant from the Database")
    print("'3': Edit the Details of a Plant in the Database")
    print("'4': Log Another Day's Data")
    print("'!': Exit the Program")
    user_action_input = input("Enter the corresponding number or symbol to the action you wish to perform: ")

    # view
    if user_action_input == "0":
        print("Printing all plants.")
        print("-"*20)
        print("|  ID  |  Name")
        print("-"*20)
        for i in range(len(database)):
            print("|" + " "*(2 if i>=10 else 3) + str(i) + "  |  " + database[i]['name'])
            print("-"*20)

        id_to_print = int(input("Enter the plant ID of which you want to view the details (Enter '!' to cancel): "))

    # add
    elif user_action_input == "1":
        print("Adding a plant. Enter '!' to cancel.")
        name = input("Enter the name of your new plant: ")
        if name == "!":
            continue

        height = int(input("Enter the current height of your plant (in cm). If you have just planted it, enter 0: "))
        if height == "!":
            continue
        
        database.append({
            "name": name, 
            "starting_height": height, 
            "current_height": height,
            "day_started_recording": day,
            "number_of_days_recording": 0,
            "historical_data": [(day, height)]
        })

    # remove
    elif user_action_input == "2":
        print("Removing a plant. Enter '!' to cancel.")
        id_to_remove = int(input("Enter the ID of the plant you would like to remove: "))
        if id_to_remove == "!":
            continue

        confirmation = input(f"Are you sure you want to remove this plant? Type {database[id_to_remove]['name']} to confirm: ")

        if confirmation == "!":
            continue
        if confirmation.lower() == database[id_to_remove]['name'].lower():
            print(f"Plant {database[id_to_remove]['name']} removed.")
        else:
            print("Deletion aborted.")
    
    # edit
    elif user_action_input == "3":
        pass
    
    # log data
    elif user_action_input == "4":
        pass
    
    # no valid action chosen
    elif user_action_input != "!":
        print("Please enter a valid input!")