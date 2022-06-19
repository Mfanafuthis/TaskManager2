
"""This program works with two text files, user.txt and tasks.txt. tasks.txt
stores a list of all the tasks that the team is working on. user.txt stores the
username and password of each use that has permission to use the program."""

#=====importing libraries===========
#Import datetime library
import datetime 

#============Functions===============
def main_menu():
    # This function displays options and commands a user to select one
    while True:
        menu = menu_options()
        if menu == 'r':
            reg_user()
        elif menu == 'a':
            add_task()
        elif menu == 'va':
            view_all()
        elif menu == 'vm':
            view_mine()
        elif menu == 'ds':
            view_stats()
        elif menu == 'gr':
            generate_reports()
        elif menu == 'e':
            print('Goodbye!!!')
            exit()
            print("\n======================================================\n")
        else:
            print("You have made a wrong choice, Please Try again")
            print("\n======================================================\n")
                        
def user_name_check(user_name):
    # This function checks if the user exist on the 'user.txt' file
    exist = False
    # Create a new object file f
    with open("user.txt", "r") as f:
        # Reads all the lines in a object file
        for line in f:
            # Splits the line where there is ',' charectar
            log_details = line.split(",")
            # Checks if username is the same as the the first element
            if (user_name == log_details[0].strip()):
                exist = True
    return exist

def reg_user():
    # This function adds the user to 'user.txt' file
    # Checkes if the user its 'admin'
    if (main_user_name == "admin"):
        user_name = input("Enter username: ")
        # Calls function 'user_name_check()' to check if the username exist
        while user_name_check(user_name) == True:
            user_name = input(f"""\n{user_name}, already exist enter new\
 username or
'-1' - to return to main menu: """)
            if user_name == "-1":
                break
            
        # The following loop verifies the password until they match
        if user_name != "-1":
            verified = True
            while verified == True:
                pass_word = input("Enter password: ")
                ver_pass_word = input("Re-enter password: ")
                # Checks if the two passwords are the same
                if pass_word == ver_pass_word:
                    # Open a new object file f on an append mode
                    with open("user.txt", "a") as f:
                        # Adds username and password on to the text file
                        f.write("\n{}, {}".format(user_name,pass_word)) 
                        print("\nUsername and password added!") 
                        verified = False
                else:
                    print("\nPasswords do not match!")
    else:
        print("\nONLY ADMIN can register people!!")

    print("\n======================================================\n")

def add_task():
    # This function adds users to'user.txt' file
    # The following loop request the user to enter a username of the person
    # whom the task is to be assigned to
    # Request until the user has entered a correct username
    # Calls 'user_name_check()' to check if the username already exist
    user_name = input("Enter username you wish to assign task to : ")
    while user_name_check(user_name) == False:
        user_name = input(f"""\n{user_name}, does not exist please enter \
correct username or
'-1' - to return to main menu: """)
        if user_name == "-1":
            break
        
    if user_name != "-1":       
        task_title = input("\nEnter task title: ")
        task_discr = input("Enter task description: ")

        with open("tasks.txt","a") as f:
            f.write(write_task(user_name,task_title,task_discr,task_status="No"))
            print("\nTask addedd!!")

    print("\n======================================================\n")
	
def print_user_format (task_details,count = ""):
    # This functions prints the task details
    print(f"""\nTask {count}:\t\t\t{task_details[1].strip()}
Assigned to:\t\t{task_details[0].strip()}
Date assigned:\t\t{task_details[3].strip()}
Due date:\t\t{task_details[4].strip()}
Task Complete?\t\t{task_details[5].strip()}
Task description:\t{task_details[2].strip()}\n""")

def view_all():
    # Displays all the tasks that are in the tasks.txt file
    with open("tasks.txt", "r") as f:
        for line in f:
            task_details = line.split(",")
            print_user_format(task_details)

    print("\n======================================================\n")

def view_mine():
    # The following loop checks whether username entered exists and
    # then displays all the tasks assigned to the user
    # Repeats until the correct username has been entered
    found = False
    # Initialize user dictionary
    tasks = {}
    file_line_num = 0
    count = 0
    with open("tasks.txt","r") as f:
        for line in f:
            # Tracks the number of lines in a object file
            file_line_num += 1
            task_details = line.split(",")
            if task_details[0] == main_user_name:
                count+=1
                # Adds key and value on the dictionary
                tasks[count] = file_line_num
                found = True
                print_user_format(task_details,count)
    
    if found == False:
        print("\nThere is no task assigned to you!")
    else:
        print("Select on of the following options below: ")
        # Prints tasks obtions
        for task in range(1,count+1):
            print(f"'{task}' - to view Task {task}")
        while True:
            try:
                user_choice = int(input("""'-1' - to return to main menu
: """))
                break
            except ValueError:
                print("That was an invalid number. Please try againg....")
            
        # Checks if the user choice is with the range of task number
        if (user_choice >= 1) and (user_choice <= count):
            with open("tasks.txt", "r") as f:
                lines = f.readlines()
            # Takes user selected element in list 'lines' and convert it
            # to new list 'task_list'
            list_task = lines[tasks[user_choice]-1].split(",")
            # Checks if the task has been completed by checking the value of
            # elements 6 index 5 in a list
            final_string = "\nTask edited!!"
            if(list_task[5].strip() == "No"):
                user_command = input("""\nSelect one of the following \
Options below:
'e' - to edit the task
'c' - to mark the task as complete
: """).lower()
                if user_command == "e":
                    
                    user_command = input("""\nSelect one of the following \
Options below:
'u' - to edit username
'd' - to edit due date
: """).lower()
                    if user_command == "u":
                        user_name = input("Enter username: ")
                        # Checks if the username exist by calling function
                        # user_name_check()
                        if user_name_check(user_name) == True:
                            list_task[0] = user_name
                        else:
                            final_string = "\nUsername does not exist please register before assigning task!"
                    elif user_command == "d":
                        list_task[4] = enter_date()
                    else:
                        final_string = "\nPlease choice a valid character"
                        
                elif user_command == "c":
                    list_task[5] = "Yes\n"
                    print("\nTask completed!")
                else:
                    final_string = "\nInvalid choice...."
                # Overwrights an elements in 'lines' list selected by user 
                lines[tasks[user_choice]-1] = write_task(
                    list_task[0], list_task[1], list_task[2],list_task[5],
                    list_task[3],list_task[4])
                
                with open("tasks.txt", "w") as f:
                    for item in lines:
                        f.write(item)
                        
                print(final_string)
            else:
                    print(f"\nTask {user_choice} has been completed you \
cannot edit!")
                    
        elif user_choice == -1:
            print("\n======================================================\n") 
            main_menu()
        else:
            print(f"\nThe task you chose does'nt not exist")
    print("\n======================================================\n")
    
def enter_date():
    # This functions commands a user to enter date
    user_input_date = input("Enter new due date (in DD/MM/YYYY): ")
    # Converts string into date opject
    converted_date = datetime.datetime.strptime(user_input_date,
                                                "%d/%m/%Y").date()
    # Converts object date to string 
    str_date = converted_date.strftime("%d %b %Y")
    return str_date
	
def write_task(user_name, task_title,task_discr,task_status,date_assigned=0,
               due_date=0):
    # This function writes tasks details in 'tasks.txt' file formart
    if due_date == 0 and date_assigned == 0:
        current_date = (datetime.date.today()).strftime("%d %b %Y")
        str_task ="\n{}, {}, {}, {}, {}, {}".format(
            user_name,task_title,task_discr,current_date, enter_date(),
                task_status)
    else:
        str_task ="{}, {}, {}, {}, {}, {}".format(
            user_name,task_title,task_discr,date_assigned, due_date,task_status)
    return str_task

def tot_num_tasks(file_name):
    # This function calculates the number of line in a files and
    # returns them as a total number of elements in a file
    task_list = []
    with open(file_name,"r") as f: # Create an object file f
        for line in f:
            task_details = line.split(",")
            task_list.append(task_details[0].strip())
            
    # Check if there is empty elements in a list and removes them
    for item in task_list:
        if item == "":
            task_list.remove(item)
            
    tot_num = len(task_list)
    return tot_num
	
def view_stats():
    # This function displays the stats by reading two files
    # 'task_overview.txt' and 'user_overview.txt'
    
    # Checks if it's admin logged in
    if main_user_name == "admin": 
        with open("task_overview.txt", "r") as f:
            task_details = f.readline()
            task_details = task_details.split(":")

        with open("user_overview.txt","r") as f:
            user_details = f.readline()
            user_details = user_details.split(":")

        print("\nTotal number of users: {}".format(user_details[1].strip()))
        print("Total number of tasks: {}\n".format(task_details[1].strip()))
        
    print("\n======================================================\n")
		
def generate_reports():
    # This functions generates reports and writes the two files
    num_completed_tasks = 0
    num_uncompleted_tasks = 0
    num_overdue_tasks = 0
    with open("tasks.txt", "r") as f:
        for line in f:
            task_details = line.split(",")
            if task_details[5].strip() == "Yes":
                num_completed_tasks+=1
            else:
                num_uncompleted_tasks+=1
            # Checks if overdue date has passed by comparing current date and
            # overdue date from the list
            if datetime.datetime.strptime(
                task_details[4].strip(),"%d %b %Y").date() < datetime.date.today() \
                and task_details[5].strip() == "No":
                num_overdue_tasks += 1
                
    num_tasks = tot_num_tasks("tasks.txt")
    with open("task_overview.txt","w") as f:
        f.write(f"""Total number of tasks:\t\t\t\t{num_tasks}
Total number of completed tasks:\t\t{num_completed_tasks}
Total number of uncompleted tasks:\t\t{num_uncompleted_tasks}
Total number of overdue tasks:\t\t\t{num_overdue_tasks}
The percentage of uncompleted tasks:\t\t\
{round((num_uncompleted_tasks/num_tasks)*100,0)}
The percentage of tasks that are overdue is:\t\
{round((num_overdue_tasks/num_tasks)*100,0)}""")

    user_dictionary = {}
    with open("user.txt", "r") as f:
        for line in f:
            user_details = line.split(",")
            # Checkes if the elements is empty
            if user_details[0] != '':
                user_dictionary[user_details[0]] = 0
    
    for item in user_dictionary:
        with open("tasks.txt", "r") as f:
            for line in f:
                user_details = line.split(",")
                if item == user_details[0].strip():
                    user_dictionary[item]+=1
    
    with open("user_overview.txt","w") as f:
        f.write(f"""Total number of users:\t\t{len(user_dictionary)}
Total number of tasks:\t\t{num_tasks}
\n""")
    

    num_user_completed_tasks = 0
    num_user_uncompleted_tasks = 0
    num_user_overdue_tasks = 0

    for item in user_dictionary:
        with open("tasks.txt", "r") as f:
            for line in f:
                task_details = line.split(",")
                if item == task_details[0] and task_details[5].strip() == "Yes":
                    num_user_completed_tasks += 1
                    
                if item == task_details[0] and task_details[5].strip() == "No":
                    num_user_uncompleted_tasks += 1
                    
                if item == task_details[0] and datetime.datetime.strptime(
                    task_details[4].strip(),"%d %b %Y").date()\
                < datetime.date.today() and task_details[5].strip() == "No":
                    num_user_overdue_tasks += 1
                    
        if user_dictionary[item] != 0:
            perc_completed_task\
            = round((num_user_completed_tasks/user_dictionary[item])*100,0)
            perc_uncompleted_task\
            = round((num_user_uncompleted_tasks/user_dictionary[item])*100,0)
            perc_overdue_task\
            = round((num_user_overdue_tasks/user_dictionary[item])*100,0)
        else:
            perc_completed_task = 0
            perc_uncompleted_task = 0
            perc_overdue_task = 0
            
        with open("user_overview.txt","a") as f:
            f.write(f"""USER: {item}
Task assigned:\t\t\t{user_dictionary[item]}
Assigned task percentage:\t{round((user_dictionary[item]/num_tasks)*100,0)}
Completed tasks percentage:\t{perc_completed_task}
Uncompleted tasks percentage:\t{perc_uncompleted_task}
Overdue task percentage:\t{perc_overdue_task}
\n""")
        num_user_uncompleted_tasks = 0
        num_user_completed_tasks = 0
        num_user_overdue_tasks = 0

    user_choice = input("""Reports generated!!
\nPress:
'v' - to view reports
'-1' - to return to main menu
: """)
    if user_choice == "v":
        print("\n==============TASK OVERVIW===========================")
        with open("task_overview.txt", "r") as f:
            print(f.read())

        print("\n==============USER OVERVIW===========================")
        with open("user_overview.txt", "r") as f:
            print(f.read())
            
    print("\n======================================================\n")
    
def menu_options():
    # This function displays the main menu obtion as per user logged in
    if(main_user_name == "admin") and (logins == False):
        menu = input('''\nSelect one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
ds - To view stats
e - Exit
: ''').lower()
        print("\n======================================================\n")
    else:
        menu = input('''\nSelect one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
e - Exit
: ''').lower()
        print("\n======================================================\n")
        
    return menu

#====Login Section====

"""The following loop request the user to enter password
and user name until the corret credintials"""
# Controlling variable
logins = True 
while logins:
    main_user_name = input("\nEnter user name: ")
    pass_word = input("Enter password: ")

    # Opens a new object file f
    with open("user.txt", "r") as f:
        # Goes through all the line in f
        for line in f:
            # Splits the lines into the list wherever the "," charecter is
            log_details = line.split(",")
            # Checks if the username and password match with existing in the file
            # Remove all the new line and space charectors before checking
            if (main_user_name == log_details[0].strip())\
            and (pass_word == log_details[1].strip()): 
                # Print if the above true                                                                                     
                print("\nWelcome {}!!\n".format(main_user_name))
                # Update the controlling variable to false
                logins = False 
                break

    if logins == True:
        print("\nPlease enter correct username or password!!")

    print("\n======================================================\n")
    
# Calls function main menu after the user has logged in
main_menu()



# Read on c-sharpcorner website about datetime libray
# https://www.c-sharpcorner.com/UploadFile/75a48f/working-with-date-and-time-python/
