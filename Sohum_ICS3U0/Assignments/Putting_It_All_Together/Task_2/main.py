#-----------------------------------------------------------------------------
# Name:        Plant Growth Tracker
# Purpose:     To allow the user to manage their own plant growth database, 
#              where they can update and retrieve data for their own use.
#
# Author:      Sohum Padhye
# Created:     17-Apr-2025
# Updated:     25-Apr-2025
#-----------------------------------------------------------------------------

# initialize database and initialize day
database = []
day = 1

# greet user
print("Welcome to your very own plant growth tracker!")
user_action_input = ""

# program loop, goes until the user fully exits out
while user_action_input != "!":

    # give the user their possible actions when they enter certain characters
    print("Your possible actions are:")
    print("'0': View Your Plants")
    print("'1': Add a Plant to the Database")
    print("'2': Remove a Plant from the Database")
    print("'3': Change the Name of a Plant in the Database")
    print("'4': Log Another Day's Data")
    print("'!': Exit the Program")
    user_action_input = input("Enter the corresponding number or symbol to the action you wish to perform: ")

    # view all plants
    if user_action_input == "0":

        # if there are no plants to view, let the user know
        if len(database) == 0:
            print("Add plants to your database first!")
            continue

        # format the printing so it looks nice
        print("Printing all plants.")
        print("-"*20)
        print("|  ID  |  Name")
        print("-"*20)
        for i in range(len(database)):
            print("|" + " "*(2 if i>=10 else 3) + str(i) + "  |  " + database[i]['name'])
            print("-"*20)

        # ask the user if they would like to see a plant in more detail
        id_to_print = input("Enter the plant ID of which you want to view the details (Enter '!' to go to back to menu): ")

        # only run if the user hasn't exited with '!'
        while id_to_print != "!":

            # only go past this once the user selects a valid ID
            while id_to_print != "!" and (int(id_to_print) < 0 or int(id_to_print) >= len(database)):
                id_to_print = input("Please enter a valid input - either the ID of the plant you want to view or '!' to exit back to the menu: ")
            
            # user wants to go back to menu
            if id_to_print == "!":
                print("Returning to menu...")
                continue

            # print all relevant details of the plant
            plant_to_print = database[int(id_to_print)]
            print(f"Printing details for {plant_to_print['name']}...")
            print(f"Starting height: {plant_to_print['starting_height']} cm")
            print(f"Current height: {plant_to_print['current_height']} cm")

            number_of_days_recorded = day - plant_to_print['day_started_recording'] + 1
            print(f"Days spent recording data for {plant_to_print['name']}: {number_of_days_recorded}")

            overall_growth = plant_to_print['current_height'] - plant_to_print['starting_height']
            print(f"Overall growth since start of recording: {overall_growth} cm")

            print(f"Average growth per day: {overall_growth/number_of_days_recorded} cm/day")

            # loop through the plant's data to display it
            print("Printing historical data:")
            for i in range(len(database[int(id_to_print)]['historical_data'])):
                (day_to_print, height_on_day) = database[int(id_to_print)]['historical_data'][i]
                print(f"Day {day_to_print}: {height_on_day} cm")
            
            # ask if the user would like to view more in-depth details of another plant
            id_to_print = input("If you'd like to view another plant's details, type its ID. Otherwise, enter '!' to return to the menu: ")
    
    # add a plant to the database
    elif user_action_input == "1":
        print("Adding a plant. Enter '!' to cancel.")

        # ask the user details about their new plant and exit if they enter '!' anywherre
        name = input("Enter the name of your new plant: ")
        if name == "!":
            continue

        height = int(input("Enter the current height of your plant (in cm). If you have just planted it, enter 0: "))
        if height == "!":
            continue
        
        # the user hasn't exited, add the details of the plant to the database as a dictionary with some added values
        database.append({
            "name": name, 
            "starting_height": height,
            "current_height": height,
            "day_started_recording": day,
            "historical_data": [(day, height)]
        })

    # remove
    elif user_action_input == "2":

        # if the user doesn't have plants to remove, let them know
        if len(database) == 0:
            print("Add plants to your database first!")
            continue

        # ask the user for the ID they would like to remove and don't proceed in the program until their input makes sense
        print("Removing a plant. Enter '!' to cancel.")
        id_to_remove = input("Enter the ID of the plant you would like to remove: ")
        while id_to_remove != "!" and (int(id_to_remove) < 0 or int(id_to_remove) >= len(database)):
            id_to_remove = input("Please enter a valid ID! Enter '!' to abort deletion: ")
        if id_to_remove == "!":
            continue

        id_to_remove = int(id_to_remove)

        # make the user confirm their deletion in case it was an accident
        confirmation = input(f"Are you sure you want to remove plant '{database[id_to_remove]['name']}'? Type '{database[id_to_remove]['name']}' to confirm: ")

        if confirmation.lower() == database[id_to_remove]['name'].lower():
            print(f"Plant {database[id_to_remove]['name']} removed.")
            database.pop(id_to_remove)
        else:
            print("Deletion aborted.")
            continue
    
    # change name
    elif user_action_input == "3":

        # if the user doesn't have plants in the database to change the name of, let them know
        if len(database) == 0:
            print("Add plants to your database first!")
            continue

        # ask the user for the ID of the plant they want to change the name of
        print("Editing plant name. Enter '!' to return to menu.")
        id_to_edit = input("Enter the ID of the plant whose name you would like to change (note - you cannot edit historical data): ")

        # keep asking the user for an ID until they enter a valid input
        while id_to_edit != "!" and (int(id_to_edit) < 0 or int(id_to_edit) >= len(database)):
            print("Please enter a valid input!")
            id_to_edit = input("Enter the ID of the plant whose name you would like to change: ")

        if id_to_edit == "!":
            print("Aborting name change.")
            continue

        # change the name of the targeted plant
        print(f"Editing name for plant {database[id_to_edit]['name']}.")
        new_plant_name = input("What would you like to change your plant's name to? Enter '!' to cancel: ")

        # user wants to cancel the name change
        if new_plant_name == "!":
            print("Name change aborted.")
            continue
        
        # ask for confirmation from the user, abort if the confirmation isn't valid
        confirmation = input(f"Are you sure you want to change your plant's name to '{new_plant_name}'? Enter 'y' to confirm: ")
        if confirmation.lower() == 'y':
            database[id_to_edit]['name'] = new_plant_name
            print(f"Changed plant with ID {id_to_edit}'s name to {new_plant_name}.")
        else:
            print("Name change aborted.")
            continue
    # log data for another day
    elif user_action_input == "4":

        # if the user has no plants to log data for, let hem know
        if len(database) == 0:
            print("Add plants to your database first!")
            continue

        # for each of the plants, ask the user to enter the new height of the plant at the end of the day
        for i in range(len(database)):
            plant_to_log = database[i]
            data_to_log = float(input(f"Enter the current height of plant '{database[i]['name']}' (in cm), or enter -1 to log the same height as the last day: "))
            while data_to_log < 0 and data_to_log != -1:
                print("Please enter a valid number.")

            # if the user used the shortcut to log the previous day's height, get the previous day's height
            if data_to_log == -1:
                data_to_log = database[i]['historical_data'][1]
            database[i]['historical_data'].append((day, data_to_log))
            database[i]['current_height'] = data_to_log
        
        # increment day counter
        day += 1

    # no valid action chosen
    elif user_action_input != "!":
        print("Please enter a valid input!")