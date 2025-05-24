#-----------------------------------------------------------------------------
# Name:        Plant Growth Tracker
# Purpose:     To allow the user to manage their own plant growth database, 
#              where they can update and retrieve data for their own use.
#
# Author:      Sohum Padhye
# Created:     25-Apr-2025
# Updated:     23-May-2025
#-----------------------------------------------------------------------------

def view_plants(database, day):
    """
    Lets the user view their plants.

    Displays the ID and name of all plants in the database in a table, where a user can
    then select to view a plant's details.

    Parameters
    ----------
    database : list of dictionaries
        The current database in use.
    day : int
        The current day in the simulator.

    Raises
    ------
    ValueError
        Raised if the user currently has no plants in the database to use.


    Returns
    -------
    None
    """

    # if there are no plants to view, let the user know
    if len(database) == 0:
        raise ValueError("Please add plants to your database first!")

    # format the printing so it looks nice
    print("Printing all plants.")
    print("-"*20)
    print("|  ID  |  Name")
    print("-"*20)
    for i in range(len(database)):
        print("|" + " "*((1 if i>=100 else 2) if i>=10 else 3) + str(i) + "  |  " + database[i]['name'])
        print("-"*20)

    # ask the user if they would like to see a plant in more detail
    id_to_print = input("Enter the plant ID of which you want to view the details (Enter '!' to go to back to menu): ")

    # only run if the user hasn't exited with '!'
    while id_to_print != "!":

        # only go past this once the user selects a valid ID
        while id_to_print != "!" and (int(id_to_print) < 0 or int(id_to_print) >= len(database)):
            id_to_print = input("Please enter a valid input - either the ID of the plant you want to view or '!' to exit back to the menu: ")
        
        while True:
            if id_to_print.isdigit():
                if int(id_to_print) < 0 or int(id_to_print) >= len(database):
                    id_to_print = input("Please enter a valid input - either the ID of the plant you want to view or '!' to exit back to the menu: ")
                    continue
                break
            elif id_to_print == "!":
                break
            else:
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

def add_plant(database, day):
    """
    Lets the user add a plant to the database.

    Asks the user for input on specifications to give a plant that they would like to add to their database,
    then adds that plant to the database.

    Parameters
    ----------
    database : list of dictionaries
        The current database in use.
    day : int
        The current day in the simulator.


    Raises
    ------
    Exception
        Raised if the user intentionally aborts the addition of a plant to the database.

    Returns
    -------
    list of dictionaries
        The updated database after the plant is added.
    """

    print("Adding a plant. Enter '!' to cancel.")

    # ask the user details about their new plant and exit if they enter '!' anywherre
    name = input("Enter the name of your new plant: ")
    if name == "!":
        raise Exception("Aborted adding plant.")

    height = input("Enter the current height of your plant (in cm). If you have just planted it, enter 0: ")

    while True:
        if height.isdigit():
            if float(height) < 0:
                print("Please input a valid, non-negative integer!")
                height = input("Enter the current height of your plant (in cm). If you have just planted it, enter 0: ")
                continue
            break
        elif height == "!":
            raise Exception("Aborted adding plant.")
        else:
            print("Please input a valid, non-negative integer!")
            height = input("Enter the current height of your plant (in cm). If you have just planted it, enter 0: ")

    
    # the user hasn't exited, add the details of the plant to the database as a dictionary with some added values
    database.append({
        "name": name, 
        "starting_height": int(height),
        "current_height": int(height),
        "day_started_recording": int(day),
        "historical_data": [(int(day), float(height))]
    })

    return database

def remove_plant(database):
    """
    Lets the user remove a plant from the database.

    Asks the user for an ID, then after confirmation from the user, 
    removes the plant with the inputted ID from the database.

    Parameters
    ----------
    database : list of dictionaries
        The current database in use.

    Raises
    ------
    Exception
        Raised if the user intentionally aborts the removal of a plant from the database.
    ValueError
        Raised if the user does not have any plants in their database.

    Returns
    -------
    list of dictionaries
        The updated database after the plant is removed.
    """

    # if the user doesn't have plants to remove, let them know
    if len(database) == 0:
        raise ValueError("Add plants to your database first!")

    # ask the user for the ID they would like to remove and don't proceed in the program until their input makes sense
    print("Removing a plant. Enter '!' to cancel.")
    id_to_remove = input("Enter the ID of the plant you would like to remove: ")
    while True:
        if id_to_remove.isdigit():
            if int(id_to_remove) < 0 or int(id_to_remove) >= len(database):
                id_to_remove = input("Please enter a valid ID! Enter '!' to abort deletion: ")
                continue
            break
        elif id_to_remove == "!":
            raise Exception("Aborted removing plant.")        
        else:
            id_to_remove = input("Please enter a valid ID! Enter '!' to abort deletion: ")

    id_to_remove = int(id_to_remove)

    # make the user confirm their deletion in case it was an accident
    confirmation = input(f"Are you sure you want to remove plant '{database[id_to_remove]['name']}'? Type '{database[id_to_remove]['name']}' to confirm: ")

    if confirmation.lower() == database[id_to_remove]['name'].lower():
        print(f"Plant {database[id_to_remove]['name']} removed.")
        database.pop(id_to_remove)
    else:
        raise Exception("Aborted removing plant.")
    
    return database

def change_name_of_plant(database):
    """
    Lets the user change the name of a plant in the database.

    Asks the user for the ID of the plant they would like to change the name of, then 
    presents a prompt to the user to change the name of that plant.

    Parameters
    ----------
    database : list of dictionaries
        The current database in use.

    Raises
    ------
    Exception
        Raised if the user intentionally aborts the addition of a plant to the database.
    ValueError
        Raised if there are no plants in the database.

    Returns
    -------
    list of dictionaries
        The updated database after the plant's name is changed.
    """

    # if the user doesn't have plants in the database to change the name of, let them know
    if len(database) == 0:
        raise ValueError("Add plants to your database first!")

    # ask the user for the ID of the plant they want to change the name of
    print("Editing plant name. Enter '!' to return to menu.")
    id_to_edit = input("Enter the ID of the plant whose name you would like to change: ")

    # keep asking the user for an ID until they enter a valid input    
    while True:
        if id_to_edit.isdigit():
            if int(id_to_edit) < 0 or int(id_to_edit) >= len(database):
                print("Please enter a valid input!")
                id_to_edit = input("Enter the ID of the plant whose name you would like to change: ")
                continue
            break
        elif id_to_edit == "!":
            raise Exception("Aborting name change.")
        else:
            print("Please enter a valid input!")
            id_to_edit = input("Enter the ID of the plant whose name you would like to change: ")


    # change the name of the targeted plant
    print(f"Editing name for plant {database[int(id_to_edit)]['name']}.")
    new_plant_name = input("What would you like to change your plant's name to? Enter '!' to cancel: ")

    # user wants to cancel the name change
    if new_plant_name == "!":
        raise Exception("Aborting name change.")
    
    # ask for confirmation from the user, abort if the confirmation isn't valid
    confirmation = input(f"Are you sure you want to change your plant's name to '{new_plant_name}'? Enter 'y' to confirm: ")
    if confirmation.lower() == 'y':
        database[int(id_to_edit)]['name'] = new_plant_name
        print(f"Changed plant with ID {id_to_edit}'s name to {new_plant_name}.")
    else:
        raise Exception("Aborting name change.")
    
    return database

def log_data(database, day):
    """
    Lets the user log a day's data in the database.

    For each of the plants in the user's database, the user is asked to log the current height of the plant.

    Parameters
    ----------
    database : list of dictionaries
        The current database in use.
    day : int
        The current day in the simulator.

    Raises
    ------
    Exception
        Raised if the user intentionally aborts the addition of a plant to the database.
    ValueError
        Raised if there are no plants in the database.

    Returns
    -------
    tuple with: list of dictionaries and day counter
        The updated database after the plant's name is changed, and the current day number to keep track
        of how may days have been recorded.
    """

    # if the user has no plants to log data for, let them know
    if len(database) == 0:
        raise ValueError("Add plants to your database first!")

    # for each of the plants, ask the user to enter the new height of the plant at the end of the day
    for i in range(len(database)):
        plant_to_log = database[i]
        data_to_log = input(f"Enter the current height of plant '{plant_to_log['name'].upper()}' (in cm), or enter -1 to log the same height as the last day: ")
        while True:
            if data_to_log.isdigit() or (data_to_log[0] == "-" and data_to_log[1:].isdigit()):
                if float(data_to_log) < 0 and int(data_to_log) != -1:
                    print("Please enter a valid number.")
                    data_to_log = input(f"Enter the current height of plant '{plant_to_log['name'].upper()}' (in cm), or enter -1 to log the same height as the last day: ")
                    continue
                break
            else:
                print("Please enter a valid number.")
                data_to_log = input(f"Enter the current height of plant '{plant_to_log['name'].upper()}' (in cm), or enter -1 to log the same height as the last day: ")

        # if the user used the shortcut to log the previous day's height, get the previous day's height
        if float(data_to_log) == -1:
            data_to_log = plant_to_log['historical_data'][-1][1]
        plant_to_log['historical_data'].append((day, data_to_log))
        plant_to_log['current_height'] = data_to_log
    
    # increment day counter
    day += 1
    return (database, day)

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
        try:
            view_plants(database, day)
        except Exception as e:
            print(e)
    
    # add a plant to the database
    elif user_action_input == "1":
        try:
            database = add_plant(database, day)
        except Exception as e:
            print(e)

    # remove
    elif user_action_input == "2":
        try:
            database = remove_plant(database)
        except Exception as e:
            print(e)

    # change name
    elif user_action_input == "3":
        try:
            database = change_name_of_plant(database)
        except Exception as e:
            print(e)
        
    # log data for another day
    elif user_action_input == "4":
        try:
            database, day = log_data(database, day)
        except Exception as e:
            print(e)
    # no valid action chosen
    elif user_action_input != "!":
        print("Please enter a valid input!")