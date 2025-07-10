import validation
from datetime import date
POOR_ATTENDANCE_PERCENTAGE = 40
FILE_FORMAT = ".txt"


def read_from_file(login_file):
    """
    Accessing the username and password from the login file and storing them in a list.
    An error will be displayed if the file is not found.
    :param login_file: str, name of login file
    :return: two lists: the usernames and passwords read from the file
    """

    username = []
    password = []
    try:
        with open(login_file) as connection:
            for line in connection:
                # strips blank space
                line = line.rstrip()

                # splits the line with :
                data = line.split(":")

                # appends data into respective lists:
                username.append(data[0])
                password.append(data[1])

    # Displaying an error message if the login file is not found
    except FileNotFoundError:
        print(f"{login_file} not found")
        exit()

    return username, password


def login(username, password):
    """
    Asking the user for username and password and authenticating them if correct.
    If either the username or password is incorrect the program closes
    :param username: list of str containing valid usernames
    :param password: list of str containing valid passwords
    :return: bool value which indicates if user was able to log on or not
    """

    print("Module Record System - Login\n-------------------------------")
    # getting the username and password and validating that they aren't empty strings
    users_username = validation.get_non_empty_string("Name: ")
    users_password = validation.get_non_empty_string("Password: ")

    # check if the users username is in the list
    if users_username in username:
        # Finding out where the username in the list (index)
        login_index = username.index(users_username)
        # checks the password index and if it's correct
        if users_password == password[login_index]:
            # if the users name and password matches returning true
            return True, login_index
    # if they do not match, returning false
    else:
        return False, None  # there is no login_index to return in this case


def menu(username, login_index):
    """
    Prints the main menu with the users username and receives the users choice.
    This can only be accessed after logging in
    :param username: list of str containing valid usernames
    :param login_index: index int users valid username in the username list
    :return: an int which is the users selection from the menu (1-3)
    """

    # validating the input to ensure that only 1-3 is selected
    user_selection = int(validation.number_range(1, 3, f"\nHello {username[login_index]}\nModule Record System - "
                                                       f"Options\n-------------------------------\n"
                                                       f"1. Record Attendance\n2. Generate Statistics\n3. Exit\n>"))

    return user_selection


def modules_file(module_file):
    """
    This strips information from the module file into 2 lists. It will display an error if the file is not found.
    :param module_file: the file name in str
    :return: two lists: the module codes and module names read from the file
    """

    module_codes = []
    module_name = []
    try:
        with open(module_file) as connection:
            for line in connection:
                # strips blank space
                line = line.rstrip()

                # splits the line with comma
                data = line.split(",")

                # appends data into respective lists:
                module_codes.append(data[0])
                module_name.append(data[1])

    # Displaying an error message if the module file is not found
    except FileNotFoundError:
        print(f"{module_file} not found")
        exit()

    return module_codes, module_name


def module_menu(module_codes):
    """
    This prints the menu to choose between the different modules in the module codes list
    :param module_codes: list of str containing module codes
    :return: the selected module as a file name in str format
    """

    print("\nModule Record System - Attendance - Choose a Module\n"
          f"---------------------------------------------------")

    # Use a for loop to show each item in module_code as a numbered list
    for i in range(len(module_codes)):
        print(f"{i+1}. {module_codes[i]}")
    # making sure the user selects a number from 1 to the last number in module_code
    selection = int(validation.number_range(1, len(module_codes[-1]), ">"))
    # This will create a file name based on the users selection and the file format used
    file_name = module_codes[selection - 1] + FILE_FORMAT  # subtracting 1 from the input as 1 is added in the f string

    return file_name


def get_lists(file_name):
    """
    This strips information from the chosen module file into 3 lists. This is separating all the student data into 3
    separate lists. It will display an error if the file is not found.
    :param file_name: the users module choice as a file name
    :return: three lists: student names (str), days_present (int), days_absent (int) read from the file
    """

    student_names = []
    days_present = []
    days_absent = []

    try:
        with open(file_name) as connection:
            for line in connection:
                # strips blank space
                line = line.rstrip()

                # splits the line with comma
                data = line.split(",")
                # appends data into respective lists
                student_names.append(data[0])
                days_present.append(int(data[1]))
                days_absent.append(int(data[2]))

    # Displaying an error message if a module file is not found
    except FileNotFoundError:
        print(f"{file_name} not found")
        exit()

    return student_names, days_present, days_absent


def get_all_lists(module_codes):
    """
    This strips data from all the module files. It strips the days present and absent into 2 lists.
    For each module it adds all days present into a tuple in one list and all days absent in the other.
    :param module_codes: list of str containing module codes
    :return: 2 lists of tuples: all days students were present, all days students were absent
    """

    all_present = []
    all_absences = []
    # using a for loop to loop though each module
    for module in module_codes:
        with open(module + FILE_FORMAT) as connection:
            all_student_present = []
            all_student_absences = []
            for line in connection:
                # strips blank space
                line = line.rstrip()

                # splits the line with comma
                data = line.split(",")

                # organising where the data can be found
                days_present = int(data[1])
                days_absent = int(data[2])

                # appending the days absent and present to module list and wrapping integer in a tuple
                all_student_absences.append(days_absent)
                all_student_present.append(days_present)

            # appending to final lists
            all_absences.append(tuple(all_student_absences))
            all_present.append(tuple(all_student_present))

    return all_absences, all_present


def attendance(file_name, student_names, days_present, days_absent):
    """
    Printing the attendance menu that takes gives the user the option to mark each student as present or absent.
    If the user chooses a number over the allowed number range they will be prompted to enter again.
    The days_present and days_absent lists are updated depending on user input.
    :param file_name: the selected module as a file name in str format
    :param student_names: a list of student names in str format read from relevant module file
    :param days_present: a list of number of days present in int format read from relevant module file
    :param days_absent: a list of number of days absent in int format read from relevant module file
    :return: It does not return anything. days_present and days_absent are updated.
    """

    print(f"\nModule Record System - Attendance - {file_name[:-len(FILE_FORMAT)]}\n"  # prints file name without .txt
          f"---------------------------------------------------\n"
          f"There are {len(student_names)} students enrolled.")

    # Use a for loop to print each student and take attendance
    for i, name in enumerate(student_names):
        print(f"Student #{i+1}: {name}\n"
              f"1. Present\n2. Absent")
        # getting the user input for each student and if they are present or not, only 1/2 is accepted input.
        student_attendance = int(validation.number_range(1, 2, ">"))
        # marking them as present
        if student_attendance == 1:
            days_present[i] += + 1  # this adds 1 to the students present days
        # marking them as absent
        elif student_attendance == 2:
            days_absent[i] += + 1  # this adds 1 to the students absent days


def update_attendance_file(student_names, days_present, days_absent, file_name):
    """
    This rewrites the student name, and updates days present/absent to the chosen module file.
    It prints a message to let the user know when the file has been updates
    :param student_names: a list of student names in str format read from relevant module file
    :param days_present: a list of number of days present in int format which was updated from the attendance function
    :param days_absent: a list of number of days absent in int format which was updated from the attendance function
    :param file_name: the selected module as a file name in str format
    """

    new_file = open(file_name, "w")
    with open(file_name, 'w'):
        # looping though al of the students and updating the data
        for i in range(len(student_names)):
            print(f"{student_names[i]},{days_present[i]},{days_absent[i]}", file=new_file)

    print(f"{file_name} was updated with the latest attendance records")


def statistics(all_absences, all_present, module_name, module_codes):
    """
    This calculates the average attendance percentage for every module. It prints this information in a table
    along with the module name, code and bar graph. It also calculates modules with attendance rate below 40% and
    the module with the best attendance percentage.
    All of this information is written to a file named with the current date. When the information is written
    to a file a message informs the user of that.
    After the statistics have been displayed a message will prompt the user to press enter to be brought to the menu.
    :param all_absences: A list of tuples (int), each module contains a tuple of the days missed by each student
    :param all_present: A list of tuples (int), each module contains a tuple of the days a student was present
    :param module_name: A list of str containing module names
    :param module_codes: A list of str containing module codes
    """

    print(f"\nModule Record System - Average Attendance Data\n"
          f"----------------------------------------------")
    attendance_table = ""  # creating an accumulator to add the attendance data to

    # creating blank lists to store the sum total of the absences and presences for each module
    absence_sum = []
    presence_sum = []

    # creating a blank lists to store the worst attended modules
    poor_attendance = []

    all_attendance_percentage = []  # empty list to store all the module percentages
    all_attendance_module_name = []  # empty list to store all the module names
    module_attendance = {}  # dictionary to store attendance data

    # getting current date
    date_today = str(date.today())

    # creating the file name with today's date
    statistics_file_name = "average-attendance-" + date_today + FILE_FORMAT

    # finding the sum of each tuple in the all_absences list
    for absence in all_absences:
        absence_sum.append(sum(absence))

    # finding the sum of each tuple in the all_present list
    for presence in all_present:
        presence_sum.append(sum(presence))

    # Use a for loop to print the average attendance data
    for i, module_code in enumerate(module_codes):
        # calculate the average attendance for the current module
        module_attendance[module_code] = (presence_sum[i] / (presence_sum[i] + absence_sum[i])) * 100

        # creating the bar chart for the attendance percentage
        chart = "*" * int(module_attendance[module_code] // 10)
        # A table with the module name, code, attendance percentage and bar chart
        attendance_table += f"{module_name[i]:25} {module_codes[i]:12} {module_attendance[module_code]:4.2f}% " \
                            f"{chart:<10}\n"

        # if attendance rate is below 40% store the module name in a list
        if module_attendance[module_code] < POOR_ATTENDANCE_PERCENTAGE:
            poor_attendance.append(module_name[i])

        # appending to 2 lists to have a list with all attendance and module names
        all_attendance_percentage.append(module_attendance[module_code])
        all_attendance_module_name.append(module_name[i])

    # finding out which module was the best attended overall
    # finding the highest percentage overall
    highest_attendance_percentage = max(all_attendance_percentage)
    # finding the index of the highest percentage overall
    highest_attendance_percentage_index = all_attendance_percentage.index(highest_attendance_percentage)

    # printing the statistics breakdown
    print(attendance_table)

    print(f"The best attended module is {module_name[highest_attendance_percentage_index]} with a "
          f"{highest_attendance_percentage:.2f}% "
          f"attendance rate.")

    # printing a list of all the modules with attendance under 40%
    print(f"There are {len(poor_attendance)} modules with attendance under 40%:")
    for module in poor_attendance:
        print(module)  # printing the module and looping again until done

    print(f"\nThe above data is also stored at {statistics_file_name}")

    # writing the data to the file
    stats_file = open(statistics_file_name, "w")
    with stats_file:
        print(attendance_table, file=stats_file)
        print(f"The best attended module is {module_name[highest_attendance_percentage_index]} with a "
              f"{highest_attendance_percentage:.2f}% attendance rate.", file=stats_file)
        print(f"There are {len(poor_attendance)} modules with attendance under 40%:", file=stats_file)
        for module in poor_attendance:
            print(module, file=stats_file)  # printing the module in the txt file and looping again until done

    # pressing enter will bring you back to the main menu
    input("Press Enter to continue")


def main():
    login_file = "login" + FILE_FORMAT  # name of the login file and the file format eg .txt
    module_file = "module" + FILE_FORMAT  # name of the module file and the file format eg .txt
    username, password = read_from_file(login_file)  # username + password is retrieved from the read_from_file function

    # list of module codes and module names is retrieved from modules_file function reading it from the modules_file
    module_codes, module_name = modules_file(module_file)
    # ask user the username and password
    success, login_index = login(username, password)
    # if login returns true then the user logs in
    if success:
        user_selection = menu(username, login_index)

        run_program = True
        # This menu will keep looping until the user chooses option 3 (exit)
        while run_program:
            # if the user chooses record attendance on the menu
            if user_selection == 1:
                # user chooses the module they want and a variable for this modules filename is created
                file_name = module_menu(module_codes)
                # 3 lists of the students details is extracted from the selected module file
                student_names, days_present, days_absent = get_lists(file_name)

                # The user can take attendance for the module and update the days present/absent for each student
                attendance(file_name, student_names, days_present, days_absent)
                # This updates the selected module file with the new attendance data
                update_attendance_file(student_names, days_present, days_absent, file_name)
                # returning to the menu when done
                user_selection = menu(username, login_index)

            # if the user chooses generate statistics on the menu
            elif user_selection == 2:
                # This gets all days present/absent for every module
                all_absences, all_present = get_all_lists(module_codes)
                # this creates statistics based on the data provided
                statistics(all_absences, all_present, module_name, module_codes)
                # returning to the menu when done
                user_selection = menu(username, login_index)

            # if the user chooses exit on the menu
            elif user_selection == 3:
                print("Exiting Module Record System")
                break  # break out of outer while loop

    # otherwise the user was not able to log on if false was returned, tell them and close the program
    else:
        print("Login Failed.\nExiting Module Record System.")
        exit()


main()
