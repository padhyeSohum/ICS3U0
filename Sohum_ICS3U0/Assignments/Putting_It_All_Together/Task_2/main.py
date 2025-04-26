database = []
day = 1

print("Welcome to Puhlant, your very own plant growth tracker!")
user_action_input = ""

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
        if len(database) == 0:
            print("Add plants to your database first!")
            continue
        print("Printing all plants.")
        print("-"*20)
        print("|  ID  |  Name")
        print("-"*20)
        for i in range(len(database)):
            print("|" + " "*(2 if i>=10 else 3) + str(i) + "  |  " + database[i]['name'])
            print("-"*20)

        id_to_print = input("Enter the plant ID of which you want to view the details (Enter '!' to go to back to menu): ")

        while id_to_print != "!":
            while id_to_print != "!" and (int(id_to_print) < 0 or int(id_to_print) >= len(database)):
                id_to_print = input("Please enter a valid input - either the ID of the plant you want to view or '!' to exit back to the menu: ")
            
            if id_to_print == "!":
                print("Returning to menu...")
                continue

            plant_to_print = database[int(id_to_print)]
            print(f"Printing details for {plant_to_print['name']}...")
            print(f"Starting height: {plant_to_print['starting_height']} cm")
            print(f"Current height: {plant_to_print['current_height']} cm")

            number_of_days_recorded = day - plant_to_print['day_started_recording'] + 1
            print(f"Days spent recording data for {plant_to_print['name']}: {number_of_days_recorded}")

            overall_growth = plant_to_print['current_height'] - plant_to_print['starting_height']
            print(f"Overall growth since start of recording: {overall_growth} cm")

            print(f"Average growth per day: {overall_growth/number_of_days_recorded} cm/day")

            print("Printing historical data:")
            for i in range(len(database[int(id_to_print)]['historical_data'])):
                (day_to_print, height_on_day) = database[int(id_to_print)]['historical_data'][i]
                print(f"Day {day_to_print}: {height_on_day} cm")
            
            id_to_print = input("If you'd like to view another plant's details, type its ID. Otherwise, enter '!' to return to the menu: ")
    
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
            "historical_data": [(day, height)]
        })

    # remove
    elif user_action_input == "2":
        print("Removing a plant. Enter '!' to cancel.")
        id_to_remove = int(input("Enter the ID of the plant you would like to remove: "))
        if id_to_remove == "!":
            continue

        confirmation = input(f"Are you sure you want to remove this plant? Type '{database[id_to_remove]['name']}' to confirm: ")

        if confirmation.lower() == database[id_to_remove]['name'].lower():
            print(f"Plant {database[id_to_remove]['name']} removed.")
            database.pop(id_to_remove)
        else:
            print("Deletion aborted.")
            continue
    
    # edit
    elif user_action_input == "3":
        pass
    
    # log data
    elif user_action_input == "4":
        if len(database) == 0:
            print("Add plants to your database first!")
            continue

        for i in range(len(database)):
            plant_to_log = database[i]
            data_to_log = float(input("Enter the current height of the plant (in cm), or enter -1 to log the same height as the last day: "))
            while data_to_log < 0 and data_to_log != -1:
                print("Please enter a valid number.")
            if data_to_log == -1:
                data_to_log = database[i]['historical_data'][1]
            database[i]['historical_data'].append((day, data_to_log))
        day += 1
    # no valid action chosen
    elif user_action_input != "!":
        print("Please enter a valid input!")